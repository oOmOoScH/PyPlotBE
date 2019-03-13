import numpy as np
import matplotlib.pyplot as plt  # plot function  library
import matplotlib.ticker as ticker
import sys
import pandas as pd  # csv file deal function library
import os
from datetime import datetime
from datetime import timedelta
import time, datetime

# BB40000200000000 "2019-01-22 05:20:00" "2019-01-22 05:30:00"

# example:
# python fourchann.py BB40000300000000 '2019-01-22 20:20:00' '2019-01-22 23:00:00'

# SelfDef Function Library
from Download import Dataload
from Ti2TiStamp import Time2Timestamp
from TiStamp2Time import TStamp2Time

# AD1_Low   AD0_Main  AD4_High   *list*
Data_AD1 = []
Data_AD0 = []
Data_AD4 = []
Data_AD5 = []
Data_Time = []
# Define List
WholeData = []
SingleDataTime = []

# #Define Array
# PlotData=np.zeros((0))
# PlotWholeData=np.zeros((0))

# Define Flag
PlotFailflag = 1

Now_Timestamp = Time2Timestamp("s")
dd1 = TStamp2Time("s", Now_Timestamp, "False")

if len(sys.argv) == 4:
    DeviceID = sys.argv[1]
    NewStartTime = sys.argv[2]
    NewEnd_Time = sys.argv[3]
else:
    DeviceID = "BB4000040000000"
    NewStartTime = "2019-02-28 13:50:00"
    NewEnd_Time =  "2019-02-28 14:01:00"

print(NewStartTime)
NewStartTime = time.strptime(NewStartTime, "%Y-%m-%d %H:%M:%S")
StartTimeStamp = int(time.mktime(NewStartTime))


NewEnd_Time = time.strptime(NewEnd_Time, "%Y-%m-%d %H:%M:%S")
End_Timestamp = int(time.mktime(NewEnd_Time))

print(StartTimeStamp)
print(End_Timestamp)

print('开始下载............', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
try:
    ORGBCGData_New = Dataload(str(DeviceID), str(StartTimeStamp) + "000", str(End_Timestamp) + "000")
except:
    ORGBCGData_New = Dataload(str(DeviceID), str(StartTimeStamp) + "000", str(End_Timestamp) + "000")

if str(ORGBCGData_New) == "no data":
    print("error: no data")

else:
    # print(ORGBCGData_New)
    print('下载成功...', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    ORGBCGDataTemp_New = ORGBCGData_New.split("\n")
    ORGBCGDataTemp_NewLen = len(ORGBCGDataTemp_New) -1
    print("数据长度:" + str(ORGBCGDataTemp_NewLen), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    for i in range(ORGBCGDataTemp_NewLen):
        BCGDataTemp = ORGBCGDataTemp_New[i]
        BCGDataTemp = BCGDataTemp.split("_")
        SingleDataTemp = BCGDataTemp[1:2]
        SingleDataTimeTemp = BCGDataTemp[0:1]
        # SingleDataTime.append(SingleDataTimeTemp[0])

        SingleDataTemp = ''.join(SingleDataTemp)   #把序列中的元素以指定的字符连接成一个新的字符串,也就是把列转成字符串

        SingleData_New = SingleDataTemp.split(",")
        rowDataLen = len(SingleData_New)
        # print(SingleData_New)
        # print(rowDataLen)
        BCGDataTimeTemp = int(SingleDataTimeTemp[0])
        for i2 in range(rowDataLen):

            if i2 % 4 == 0:
                BCGDataTimeTemp = BCGDataTimeTemp + 8
                Data_Time.append(BCGDataTimeTemp)
                Data_AD1.append(int(SingleData_New[i2]))
            elif i2 % 4 == 1:
                Data_AD0.append(int(SingleData_New[i2]))
            elif i2 % 4 == 2:
                Data_AD4.append(int(SingleData_New[i2]))
            elif i2 % 4 == 3:
                Data_AD5.append(int(SingleData_New[i2]))

    print('切割完成...', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    Data_AD1_Lenth = len(Data_AD1)
    Data_AD0_Lenth = len(Data_AD0)
    Data_AD4_Lenth = len(Data_AD4)
    Data_AD5_Lenth = len(Data_AD5)
    if Data_AD1_Lenth == Data_AD0_Lenth == Data_AD4_Lenth:
        print('Lenth_Check_Success')
    else:
        print('Lenth_Check_Fail')
        PlotFailflag = 0

    # BCGDataTimeTemp = SingleDataTime[0]
    # BCGDataTimeTemp = int(BCGDataTimeTemp)
    # Data_Time.append(BCGDataTimeTemp)

    # print('生成时间坐标...', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # for i in range(Data_AD0_Lenth - 1):
    #     BCGDataTimeTemp = BCGDataTimeTemp + 8
    #     Data_Time.append(BCGDataTimeTemp)

    utc_time = pd.to_datetime(Data_Time, unit='ms')  # UTC Standard Time
    Data_Time = utc_time + timedelta(hours=8)  # UTC Convert BeiJingTime


    print('开始画图...', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    fig = plt.figure()
    # fig1
    ax1 = fig.add_subplot(4, 1, 1)
    # ax1.plot(Data_Time,Data_AD1,marker='o')
    ax1.plot(Data_Time, Data_AD1)
    ax1_start, ax1_end = ax1.get_ylim()
    ax1_step = (ax1_end - ax1_start) / 8
    ax1.yaxis.set_ticks(np.arange(ax1_start, ax1_end, ax1_step))
    ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))
    ax1.grid(color='black', linestyle='--', linewidth=1, alpha=0.1)
    # ax1.set_title(DeviceID + " " + "Data_AD1" + " " + "MainChannel")

    # fig2
    ax2 = fig.add_subplot(4, 1, 2)
    # ax2.plot(Data_Time,Data_AD0,marker='o')
    ax2.plot(Data_Time, Data_AD0)
    ax2_start, ax2_end = ax2.get_ylim()
    ax2_step = (ax2_end - ax2_start) / 8
    ax2.yaxis.set_ticks(np.arange(ax2_start, ax2_end, ax2_step))
    ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))
    ax2.grid(color='black', linestyle='--', linewidth=1, alpha=0.1)
    # ax2.set_title(DeviceID + " " + "Data_AD2" + " " + "High")

    # fig3
    ax3 = fig.add_subplot(4, 1, 3)
    # ax3.plot(Data_Time,Data_AD4,marker='o')
    ax3.plot(Data_Time, Data_AD4)
    ax3_start, ax3_end = ax3.get_ylim()
    ax3_step = (ax3_end - ax3_start) / 8
    ax3.yaxis.set_ticks(np.arange(ax3_start, ax3_end, ax3_step))
    ax3.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))
    ax3.grid(color='black', linestyle='--', linewidth=1, alpha=0.1)
    # ax3.set_title(DeviceID + " " + "Data_AD3" + " " + "Low")
    # print(Data_AD4)

    # fig4
    ax4 = fig.add_subplot(4, 1, 4)
    # ax3.plot(Data_Time,Data_AD4,marker='o')
    ax4.plot(Data_Time, Data_AD5)
    ax4_start, ax4_end = ax4.get_ylim()
    ax4_step = (ax4_end - ax4_start) / 8
    ax4.yaxis.set_ticks(np.arange(ax4_start, ax4_end, ax4_step))
    ax4.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))
    ax4.grid(color='black', linestyle='--', linewidth=1, alpha=0.1)
    # ax4.set_title(DeviceID + " " + "Data_AD4" + " " + "Low")
    # print(Data_AD4)

    if PlotFailflag:
        plt.show()
    else:
        print("Check the Data")

