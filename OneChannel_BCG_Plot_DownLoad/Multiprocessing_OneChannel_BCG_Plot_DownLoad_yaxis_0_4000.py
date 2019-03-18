import numpy as np
import multiprocessing
import matplotlib.pyplot as plt          #plot function  library 
import matplotlib.ticker as ticker
import sys
import pandas as pd                      #csv file deal function library 
import os
from datetime import datetime
from datetime import timedelta
import time,datetime

# import vthread 
import tkinter as tk                     #obtain the file path library 
from tkinter import filedialog           #obtain the file path library 

import easygui as fgui                   #obtain the file path library with easygui

#SelfDef Function Library 
from Download import Dataload
from Ti2TiStamp import Time2Timestamp
from TiStamp2Time import TStamp2Time




#Define List
DeviceID=[]

# #Define Array
# PlotData=np.zeros((0))
# PlotWholeData=np.zeros((0))





# @vthread.pool(2)
# @vthread.atom
def OneChannel_BCG_Plot(DeviceID,TimeYM,TimeDay,StartTime,End_Time):

    #AD1_Low   AD0_Main  AD4_High   *list*
    Data_Time=[]
    #Define List
    WholeData=[]
    SingleDataTime=[]

    #Define Flag
    PlotFailflag=1
    WholeDataTemp=""



    TimeDayTemp=TimeDay.split('-')

    StartTimeTemp=StartTime.split('-')
    NewStartTime=TimeYM+'-'+str(TimeDayTemp[0])+' '+str(StartTimeTemp[0])+':'+str(StartTimeTemp[1])+':'+'00'
    print(NewStartTime)
    NewStartTime=time.strptime(NewStartTime, "%Y-%m-%d %H:%M:%S")
    StartTimeStamp=int(time.mktime(NewStartTime))

    End_TimeTemp=End_Time.split('-')
    NewEnd_Time=TimeYM+'-'+str(TimeDayTemp[1])+' '+str(End_TimeTemp[0])+':'+str(End_TimeTemp[1])+':'+'00'
    print(NewEnd_Time)
    NewEnd_Time=time.strptime(NewEnd_Time, "%Y-%m-%d %H:%M:%S")
    End_Timestamp=int(time.mktime(NewEnd_Time))


    print(DeviceID+":"+str(StartTimeStamp))
    print(DeviceID+":"+str(End_Timestamp))


    print(DeviceID+":"+'Download_ING............')
    try:
        ORGBCGData_New=Dataload(str(DeviceID), str(StartTimeStamp)+"000", str(End_Timestamp)+"000")
    except:
        ORGBCGData_New=Dataload(str(DeviceID), str(StartTimeStamp)+"000", str(End_Timestamp)+"000")
    

    while str(ORGBCGData_New)=="no data":
        print(DeviceID+":"+"Wait for Seconds The Internet is not good")
        ORGBCGData_New=Dataload(str(DeviceID), str(StartTimeStamp)+"000", str(End_Timestamp)+"000")


    
    start_time = time.time()
    print(DeviceID+":"+'Download_Sucess')
    ORGBCGDataTemp_New=ORGBCGData_New.split("\n") 
    ORGBCGDataTemp_NewLen=len(ORGBCGDataTemp_New)-1
    print(DeviceID+":"+"Seconds_Total:"+str(ORGBCGDataTemp_NewLen))
    for i in range (ORGBCGDataTemp_NewLen):
        BCGDataTemp=ORGBCGDataTemp_New[i]
        BCGDataTemp=BCGDataTemp.split("_")
        SingleDataTemp=BCGDataTemp[1:2]
        SingleDataTimeTemp=BCGDataTemp[0:1]
        SingleDataTime.append(SingleDataTimeTemp[0])
        SingleDataTemp=''.join(SingleDataTemp)
        SingleData_New=SingleDataTemp.split(",")
            

        DataTemp = "-".join(SingleData_New)
        WholeDataTemp=WholeDataTemp+"-"+DataTemp
      
        if(i%(ORGBCGDataTemp_NewLen/5)==0):
            print('i is %d of %s' %(i,str(ORGBCGDataTemp_NewLen)+"_"+DeviceID))
       

    WholeData=WholeDataTemp.split("-")
    WholeData.pop(0)
    WholeData=[int(t) for t in WholeData]

    print(DeviceID+":"+str(SingleDataTime[0]))

    WholeDataLength=len(WholeData)
    print(DeviceID+":"+str(WholeDataLength))


    BCGDataTimeTemp=SingleDataTime[0]
    BCGDataTimeTemp=int(BCGDataTimeTemp)
    Data_Time.append(BCGDataTimeTemp)

    for i in range(WholeDataLength-1):
        BCGDataTimeTemp=BCGDataTimeTemp+8
        Data_Time.append(BCGDataTimeTemp)
    

    utc_time=pd.to_datetime(Data_Time,unit='ms')  #UTC Standard Time
    Data_Time= utc_time + timedelta(hours=8)     #UTC Convert BeiJingTime


    fig=plt.figure()
    #fig1
    ax1=fig.add_subplot(1,1,1)  
    ax1.plot(Data_Time,WholeData)
    # ax1_start, ax1_end = ax1.get_ylim()
    ax1_start=0
    ax1_end=4400
    ax1_step=(ax1_end-ax1_start)/10
    ax1.yaxis.set_ticks(np.arange(ax1_start, ax1_end, ax1_step))
    ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))
    ax1.grid(color='black', linestyle='--', linewidth=1,alpha=0.1)
    ax1.set_title(DeviceID+" "+"AD0"+" "+"Main_One")

    

    if PlotFailflag:
        end_time = time.time()
        print (end_time - start_time)
        plt.show()
    else:
        print(DeviceID+"Check the Data")


def BCG_Time_Input():
    print("Please Input the Number of DeviceID")
    print("The example  is: 4")
    PlotNum=input('Input the Number Like the Form Above:\n')



    print("Please Input the DeviceID")
    print("The example  is: bb30000200000000")
    for i in range(int(PlotNum)):
        print('Input the DeviceID_%d Like the Form Above:' %(i))
        DeviceIDTemp=input()
        DeviceID.append(DeviceIDTemp)

    print("Input StartTime Year & Month")
    # print("The example  is: 2019-02")
    # TimeYM=input('Input the Year-Month:\n')
    TimeYM=time.strftime('%Y-%m',time.localtime(time.time()))
    print(TimeYM)

    print("The StartTime Day & The EndTime Day")
    print("If (The StartTime Day) < (The EndTime Day),Input the 1.")
    TimeDayFlag=input()
    TimeDayTemp=time.strftime('%d',time.localtime(time.time()))
    print(TimeDayFlag)
        # print("The example  is: 01-02")
    if(TimeDayFlag=="1"):
        TimeDay=str(int(TimeDayTemp))+'-'+str(int(TimeDayTemp)+1)
    elif (TimeDayFlag=="2"):
        TimeDay=str(int(TimeDayTemp)-1)+'-'+str(int(TimeDayTemp))
    else:
        TimeDay=TimeDayTemp+'-'+TimeDayTemp
    
    print(TimeDay)


    print("Input StartTime Hour & Minute: 15-18")
    StartTime=input('Input StartTime Hour-Minute:\n')

    print("Input EndTime Hour & Minute: 21-25")
    End_Time=input('Input EndTime Hour-Minute:\n')
    

    return PlotNum,TimeYM,TimeDay,StartTime,End_Time



def DeviceProcesses(PlotNum):
    DeviceProcesses=[]
    for i in range(int(PlotNum)):
        t =multiprocessing.Process(target=OneChannel_BCG_Plot, args=(DeviceID[i],TimeYM,TimeDay,StartTime,End_Time))
        DeviceProcesses.append(t)
        t.start()

    for res in DeviceProcesses:
        res.join()  





if __name__ == '__main__':


    while 1:
            
        PlotNum,TimeYM,TimeDay,StartTime,End_Time=BCG_Time_Input()
            
        DeviceProcesses(PlotNum)



        





