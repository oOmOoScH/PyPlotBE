import numpy as np
import matplotlib.pyplot as plt  # plot function  library
import matplotlib.ticker as ticker
import sys
import pandas as pd  # csv file deal function library
import os
from datetime import datetime
from datetime import timedelta
import time, datetime

# example:
# python fourchann_real.py BB40000400000000 12

# SelfDef Function Library
from Download import Dataload
from Ti2TiStamp import Time2Timestamp
from TiStamp2Time import TStamp2Time

# #Define Array
# PlotData=np.zeros((0))
# PlotWholeData=np.zeros((0))

# Define Flag
PlotFailflag = 1

Now_Timestamp = Time2Timestamp("s")
dd1 = TStamp2Time("s", Now_Timestamp, "False")

DeviceID = sys.argv[1]

timelen = int(sys.argv[2])

first = True

fig = plt.figure()
# fig1
ax1 = fig.add_subplot(4, 1, 1)

# fig2
ax2 = fig.add_subplot(4, 1, 2)

# fig3
ax3 = fig.add_subplot(4, 1, 3)

# fig4
ax4 = fig.add_subplot(4, 1, 4)

plt.ion()

while True:
    # AD1_Low   AD0_Main  AD4_High   *list*
    Data_AD1 = []
    Data_AD0 = []
    Data_AD4 = []
    Data_AD5 = []
    Data_Time = []
    # Define List
    WholeData = []
    SingleDataTime = []

    timeend = int(time.time())
    StartTimeStamp = timeend - timelen
    End_Timestamp = timeend

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
        ORGBCGDataTemp_NewLen = len(ORGBCGDataTemp_New) - 1
        print("数据长度:" + str(ORGBCGDataTemp_NewLen), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        for i in range(ORGBCGDataTemp_NewLen):
            BCGDataTemp = ORGBCGDataTemp_New[i]
            BCGDataTemp = BCGDataTemp.split("_")
            SingleDataTemp = BCGDataTemp[1:2]
            SingleDataTimeTemp = BCGDataTemp[0:1]
            SingleDataTime.append(SingleDataTimeTemp[0])

            SingleDataTemp = ''.join(SingleDataTemp)  # 把序列中的元素以指定的字符连接成一个新的字符串,也就是把列转成字符串

            SingleData_New = SingleDataTemp.split(",")
            rowDataLen = len(SingleData_New)
            # print(SingleData_New)
            # print(rowDataLen)
            for i2 in range(rowDataLen):
                if i2 % 4 == 0:
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
        print('数据个数:', Data_AD0_Lenth)

        if Data_AD1_Lenth == Data_AD0_Lenth == Data_AD4_Lenth == Data_AD5_Lenth:
            print('Lenth_Check_Success')
        else:
            continue

        BCGDataTimeTemp = SingleDataTime[0]
        BCGDataTimeTemp = int(BCGDataTimeTemp)
        Data_Time.append(BCGDataTimeTemp)

        print('生成时间坐标...', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        for i in range(Data_AD0_Lenth - 1):
            BCGDataTimeTemp = BCGDataTimeTemp + 8
            Data_Time.append(BCGDataTimeTemp)

        utc_time = pd.to_datetime(Data_Time, unit='ms')  # UTC Standard Time
        Data_Time = utc_time + timedelta(hours=8)  # UTC Convert BeiJingTime
        print('Data_time_len', len(Data_Time))
        print('开始画图...', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        if not first:
            ax1.lines.remove(lines1[0])
            ax2.lines.remove(lines2[0])
            ax3.lines.remove(lines3[0])
            ax4.lines.remove(lines4[0])

        # ax1.plot(Data_Time,Data_AD1,marker='o')
        # lines1 = ax1.plot(Data_Time, Data_AD1,'r-')
        # ax1 = fig.add_subplot(4, 1, 1)
        lines1 = ax1.plot(Data_AD1, 'r-')
        # ax1_start, ax1_end = ax1.get_ylim()
        # ax1_step = (ax1_end - ax1_start) / 8
        # ax1.yaxis.set_ticks(np.arange(ax1_start, ax1_end, ax1_step))
        # ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))
        # ax1.grid(color='black', linestyle='--', linewidth=1, alpha=0.1)
        ax1.set_title(DeviceID + " " + "Data_AD1")

        # ax2.plot(Data_Time,Data_AD0,marker='o')
        # lines2 = ax2.plot(Data_Time, Data_AD0,'r-')
        lines2 = ax2.plot(Data_AD0, 'b-')
        # ax2_start, ax2_end = ax2.get_ylim()
        # ax2_step = (ax2_end - ax2_start) / 8
        # ax2.yaxis.set_ticks(np.arange(ax2_start, ax2_end, ax2_step))
        # ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))
        # ax2.grid(color='black', linestyle='--', linewidth=1, alpha=0.1)
        ax2.set_title(DeviceID + " " + "Data_AD2")

        # ax3.plot(Data_Time,Data_AD4,marker='o')
        # lines3 = ax3.plot(Data_Time, Data_AD4,'r-')
        lines3 = ax3.plot(Data_AD4, 'r-')
        # ax3_start, ax3_end = ax3.get_ylim()
        # ax3_step = (ax3_end - ax3_start) / 8
        # ax3.yaxis.set_ticks(np.arange(ax3_start, ax3_end, ax3_step))
        # ax3.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))
        # ax3.grid(color='black', linestyle='--', linewidth=1, alpha=0.1)
        ax3.set_title(DeviceID + " " + "Data_AD3")

        # ax4.plot(Data_Time,Data_AD4,marker='o')
        # lines4 = ax4.plot(Data_Time, Data_AD5,'r-')
        lines4 = ax4.plot(Data_AD5, 'b-')
        # ax4_start, ax4_end = ax4.get_ylim()
        # ax4_step = (ax4_end - ax4_start) / 8
        # ax4.yaxis.set_ticks(np.arange(ax4_start, ax4_end, ax4_step))
        # ax4.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.0f'))
        # ax4.grid(color='black', linestyle='--', linewidth=1, alpha=0.1)
        ax4.set_title(DeviceID + " " + "Data_AD4" + " ")
        # print(Data_AD4)


        first = False

        if PlotFailflag:
            plt.pause(2)
        else:
            print("Check the Data")
