import numpy as np
# import minpy.numpy as np
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



# @vthread.pool(2)
# @vthread.atom
def OneChannel_BCG_Plot():

    #AD1_Low   AD0_Main  AD4_High   *list*
    Data_Time=[]
    #Define List
    WholeData=[]
    SingleDataTime=[]





    # #Define Array
    # PlotData=np.zeros((0))
    # PlotWholeData=np.zeros((0))

    #Define Flag
    PlotFailflag=1
    WholeDataTemp=""
    


    print("Please Input the DeviceID")
    print("The example  is: bb30000200000000")
    DeviceID=input('Input the DeviceID Like the Form Above:\n')

    print("Input StartTime Year & Month")
    print("The example  is: 2019-01")
    TimeYM=input('Input the Year-Month:\n')

    print("The StartTime Day & The EndTime Day")
    print("The example  is: 08-09")
    TimeDay=input('Input the Day-Day:\n')

    print("Input StartTime Hour & Minute: 08-08")
    StartTime=input('Input StartTime Hour-Minute:\n')

    print("Input EndTime Hour & Minute: 20-25")
    End_Time=input('Input EndTime Hour-Minute:\n')



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


    print(StartTimeStamp)
    print(End_Timestamp)


    print('Data_Download_ING............')
    try:
        ORGBCGData_New=Dataload(str(DeviceID), str(StartTimeStamp)+"000", str(End_Timestamp)+"000")
    except:
        ORGBCGData_New=Dataload(str(DeviceID), str(StartTimeStamp)+"000", str(End_Timestamp)+"000")
    

    while str(ORGBCGData_New)=="no data":
        print("Wait for Seconds The Internet is not good")
        ORGBCGData_New=Dataload(str(DeviceID), str(StartTimeStamp)+"000", str(End_Timestamp)+"000")


    
    start_time = time.time()
    print('BCGData_Download_Sucess')
    ORGBCGDataTemp_New=ORGBCGData_New.split("\n") 
    ORGBCGDataTemp_NewLen=len(ORGBCGDataTemp_New)-1
    print("BCGData_Seconds_Total:"+str(ORGBCGDataTemp_NewLen))
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
        
        print('i is %d of %d' %(i,ORGBCGDataTemp_NewLen))
       

    WholeData=WholeDataTemp.split("-")
    WholeData.pop(0)
    WholeData=[ int(t) for t in WholeData ]

    print(SingleDataTime[0])

    WholeDataLength=len(WholeData)
    print(WholeDataLength)


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
    ax1_start, ax1_end = ax1.get_ylim()
    ax1_step=(ax1_end-ax1_start)/8
    ax1.yaxis.set_ticks(np.arange(ax1_start, ax1_end, ax1_step))
    ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))
    ax1.grid(color='black', linestyle='--', linewidth=1,alpha=0.1)
    ax1.set_title(DeviceID+" "+"AD0"+" "+"Main_One")

    

    if PlotFailflag:
        end_time = time.time()
        print (end_time - start_time)
        plt.show()
    else:
        print("Check the Data")


print("Next Begins")






if __name__ == '__main__':

   
   while 1:
        OneChannel_BCG_Plot()


