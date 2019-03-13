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
from numba import jit

import tkinter as tk                     #obtain the file path library 
from tkinter import filedialog           #obtain the file path library 

import easygui as fgui                   #obtain the file path library with easygui

#SelfDef Function Library 
from Download import Dataload
from Ti2TiStamp import Time2Timestamp
from TiStamp2Time import TStamp2Time

# @jit


#AD1_Low   AD0_Main  AD4_High   *list*
Data_AD1=[]
Data_AD0=[]
Data_AD4=[]
Data_Time=[]
#Define List
WholeData=[]
SingleDataTime=[]
WholeDataPlotTemp=[]
Xtemp=[]
# #Define Array
# PlotData=np.zeros((0))
# PlotWholeData=np.zeros((0))

#Define Flag
PlotFailflag=1


# WholeDataPlotTemp.append(0)

Now_Timestamp=Time2Timestamp("s")
dd1=TStamp2Time("s",Now_Timestamp,"False")


print("Please Input the DeviceID")
print("The example  is: bb30000200000000")
DeviceID=input('Input the DeviceID Like the Form Above:\n')

print("Input StartTime Year & Month")
print("The example  is: 2018-12")
TimeYM=input('Input the Year-Month:\n')

print("The StartTime Day & The EndTime Day")
print("The example  is: 12-13")
TimeDay=input('Input the Day-Day:\n')

print("Input StartTime Hour & Minute: 10-12")
StartTime=input('Input StartTime Hour-Minute:\n')

print("Input EndTime Hour & Minute: 10-12")
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
# print(ORGBCGData_New)
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
    # WholeData=WholeData+SingleData_New
    print(i)
    WholeDataPlotTemp.append(SingleData_New)
    
    # print(len(WholeData))

# print(WholeData)
print(SingleDataTime[0])
print(type(WholeDataPlotTemp))
for i in  range (len(WholeDataPlotTemp)):
    WholeDataPlotTemp[i]=[ int(t) for t in WholeDataPlotTemp[i] ]


print(WholeDataPlotTemp[0])
SinglelenDataPlotLen=int(len(WholeDataPlotTemp[0])/3)
print(SinglelenDataPlotLen)


########################################################
fig=plt.figure()
#fig1
ax1=fig.add_subplot(3,1,1)
ax2=fig.add_subplot(3,1,2)
ax3=fig.add_subplot(3,1,3)  
for i  in  range (int(len(WholeDataPlotTemp))):
    print('i is %d of %d' %(i,int(len(WholeDataPlotTemp))))
    
    for p in range (SinglelenDataPlotLen):
        temp=SinglelenDataPlotLen*i+p
        Xtemp.append(temp)

   
     
    for x in range(len(WholeDataPlotTemp[0])):
        if (x%3==0):
            Data_AD1.append(int(WholeDataPlotTemp[i][x]))
        elif(x%3==1):
            Data_AD0.append(int(WholeDataPlotTemp[i][x]))
        elif(x%3==2):
            Data_AD4.append(int(WholeDataPlotTemp[i][x]))
    
    

    if i>0:
        Xtemp.insert(0,Xtemp[0]-1)
        Data_AD1.insert(0,Data_AD1_EndDataTemp)
        Data_AD0.insert(0,Data_AD0_EndDataTemp)
        Data_AD4.insert(0,Data_AD4_EndDataTemp)
    

    Data_AD1_EndDataTemp=Data_AD1[len(Data_AD1)-1]
    Data_AD0_EndDataTemp=Data_AD0[len(Data_AD0)-1]
    Data_AD4_EndDataTemp=Data_AD4[len(Data_AD4)-1]




    ax1.plot(Xtemp,Data_AD1,color='blueviolet')
    ax2.plot(Xtemp,Data_AD0,color='blueviolet')
    ax3.plot(Xtemp,Data_AD4,color='blueviolet')
    Xtemp=[]
    Data_AD1=[]
    Data_AD0=[]
    Data_AD4=[]


ax1_start, ax1_end = ax1.get_ylim()
ax1_step=(ax1_end-ax1_start)/8
ax1.yaxis.set_ticks(np.arange(ax1_start, ax1_end, ax1_step))
ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))
ax1.grid(color='black', linestyle='--', linewidth=1,alpha=0.1)
ax1.set_title(DeviceID+" "+"Data_AD1"+" "+"MainChannel")


ax2_start, ax2_end = ax2.get_ylim()
ax2_step=(ax2_end-ax2_start)/8
ax2.yaxis.set_ticks(np.arange(ax2_start, ax2_end, ax2_step))
ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))
ax2.grid(color='black', linestyle='--', linewidth=1,alpha=0.1)
ax2.set_title(DeviceID+" "+"Data_AD0"+" "+"High")




ax3_start, ax3_end = ax3.get_ylim()
ax3_step=(ax3_end-ax3_start)/8
ax3.yaxis.set_ticks(np.arange(ax3_start, ax3_end, ax3_step))
ax3.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))
ax3.grid(color='black', linestyle='--', linewidth=1,alpha=0.1)
ax3.set_title(DeviceID+" "+"Data_AD4"+" "+"Low")



if PlotFailflag:
    end_time = time.time()
    print (end_time - start_time)
    plt.show()
else:
    print("Check the Data")
##########################################################



BCGDataTimeTemp=SingleDataTime[0]
BCGDataTimeTemp=int(BCGDataTimeTemp)
Data_Time.append(BCGDataTimeTemp)

# for i in range(Data_AD0_Lenth-1):
#     BCGDataTimeTemp=BCGDataTimeTemp+8
#     Data_Time.append(BCGDataTimeTemp)

# print(Data_Time)


utc_time=pd.to_datetime(Data_Time,unit='ms')  #UTC Standard Time
Data_Time= utc_time + timedelta(hours=8)     #UTC Convert BeiJingTime

# print(Data_Time)









# if __name__ == '__main__':












# BCGFile=input('Please Input The BCGFilePath:')
# print(BCGFile)
# BCGFile2=input('Please Input The BCGFilePath2:')
# print(BCGFile2)




# BCGxlabel=BCGFile.split('\\')
# BCGxlabel=BCGxlabel[(len(BCGxlabel)-1)]
# BCGxlabel=BCGxlabel.split('.')

# pwd = os.getcwd()
# os.chdir(os.path.dirname(BCGFile))
# BCGData = pd.read_csv(os.path.basename(BCGFile))
# os.chdir(pwd)


# utc_time=pd.to_datetime(BCGData['time'],unit='ms')  #UTC Standard Time
# BCGData['time'] = utc_time + timedelta(hours=8)     #UTC Convert BeiJingTime




# BCG_total_rows = len(BCGData)
# BCG_total_line = len(BCGData.columns)
# BCGdataX=BCGData.iloc[0:BCG_total_rows,0:1]         #read the BCGdata matched rows   //StrTime
# BCGdataY=BCGData.iloc[0:BCG_total_rows,1:2]         #read the BCGdata matched rows   //Value 



# BCGxlabel2=BCGFile2.split('\\')
# BCGxlabel2=BCGxlabel2[(len(BCGxlabel2)-1)]
# BCGxlabel2=BCGxlabel2.split('.')

# pwd = os.getcwd()
# os.chdir(os.path.dirname(BCGFile2))
# BCGData2 = pd.read_csv(os.path.basename(BCGFile2))
# os.chdir(pwd)


# utc_time=pd.to_datetime(BCGData2['time'],unit='ms')  #UTC Standard Time
# BCGData2['time'] = utc_time + timedelta(hours=8)     #UTC Convert BeiJingTime




# BCG_total_rows2 = len(BCGData2)
# BCG_total_line2 = len(BCGData2.columns)
# BCGdataX2=BCGData2.iloc[0:BCG_total_rows2,0:1]         #read the BCGdata matched rows   //StrTime
# BCGdataY2=BCGData2.iloc[0:BCG_total_rows2,1:2]         #read the BCGdata matched rows   //Value 




# BCGX = BCGdataX
# BCGY = BCGdataY


# BCGX2=BCGdataX2
# BCGY2=BCGdataY2




# fig=plt.figure()
# #fig1
# ax1=fig.add_subplot(2,1,1)  
# ax1.plot(BCGX,BCGY)
# ax1.grid(color='black', linestyle='--', linewidth=1,alpha=0.3)
# ax1.set_title(BCGxlabel[0])

# # #fig2
# # ax2=fig.add_subplot(4,1,2)
# # ax2.plot(BCGY)
# # ax2.grid(color='black', linestyle='--', linewidth=1,alpha=0.3)
# # ax2.set_title(BCGxlabel[0])

# # fig3
# ax3=fig.add_subplot(2,1,2)  
# ax3.plot(BCGX2,BCGY2)
# # ax3.plot(BCGX, BCGY, color='red', label=BCGxlabel[0])
# ax3.grid(color='black', linestyle='--', linewidth=1,alpha=0.3)
# ax3.set_title(BCGxlabel2[0])



# # # fig4
# # ax4=fig.add_subplot(4,1,4)  
# # ax4.plot(BCGY2)
# # ax4.grid(color='black', linestyle='--', linewidth=1,alpha=0.3)
# # ax4.set_title(BCGxlabel2[0])



# plt.show()

