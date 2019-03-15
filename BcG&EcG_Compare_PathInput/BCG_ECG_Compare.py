import numpy as np
import matplotlib.pyplot as plt          #plot function  library 
import sys
import pandas as pd                      #csv file deal function library 
import os
from datetime import datetime
from datetime import timedelta

import tkinter as tk                     #obtain the file path library 
from tkinter import filedialog           #obtain the file path library 

import easygui as fgui                   #obtain the file path library with easygui

ModLabel = ['WindowsMod','ConsoleMod','Thank~U']
ModLabelReturn = fgui.choicebox('Select The Mod ？',choices=ModLabel)
if ModLabelReturn=='WindowsMod':
    title = fgui.msgbox(msg='Select the BCGFile', title=' ', ok_button='OK', image=None, root=None)
    BCGFile = fgui.fileopenbox()
    title = fgui.msgbox(msg='Select the ECGFile', title=' ', ok_button='OK', image=None, root=None)
    ECGFile = fgui.fileopenbox()
    print(BCGFile)
    print(ECGFile)

elif ModLabelReturn=='ConsoleMod':
    BCGFile=input('please input the BCGFilePath:')
    ECGFile=input('please input the ECGFilePath:')
   

else:
     title = fgui.msgbox(msg='Hope U Nice Day~', title=' ', ok_button='OK', image=None, root=None)
     exit()


BCGxlabel=BCGFile.split('\\')
BCGxlabel=BCGxlabel[(len(BCGxlabel)-1)]
BCGxlabel=BCGxlabel.split('.')
ECGxlabel=ECGFile.split('\\')
ECGxlabel=ECGxlabel[(len(ECGxlabel)-1)]
ECGxlabel=ECGxlabel.split('.')


pwd = os.getcwd()
os.chdir(os.path.dirname(BCGFile))
BCGData = pd.read_csv(os.path.basename(BCGFile))
os.chdir(pwd)
# print(BCGData.shape) #show the row&line of the data

utc_time=pd.to_datetime(BCGData['time'],unit='ms')  #UTC Standard Time
BCGData['time'] = utc_time + timedelta(hours=8)     #UTC Convert BeiJingTime
# print(BCGData['time'])



BCG_total_rows = len(BCGData)
BCG_total_line = len(BCGData.columns)
BCGdataX=BCGData.iloc[0:BCG_total_rows,0:1]         #read the BCGdata matched rows   //StrTime
BCGdataY=BCGData.iloc[0:BCG_total_rows,1:2]         #read the BCGdata matched rows   //Value 


pwd = os.getcwd()
os.chdir(os.path.dirname(ECGFile))
ECGData = pd.read_csv(os.path.basename(ECGFile))
os.chdir(pwd)
# print(ECGData.shape) #show the row&line of the data
# ECGData.info()
ECGData['time']=pd.to_datetime(ECGData['time'],infer_datetime_format=True)


ECG_total_rows = len(ECGData)
ECG_total_line = len(ECGData.columns)

ECGdataX=ECGData.iloc[0:ECG_total_rows,0:1]         #read the ECGdata matched rows   //StrTime
ECGdataY=ECGData.iloc[0:ECG_total_rows,1:2]         #read the ECGdata matched rows   //Value 



# print(BCG_total_rows)
# print(ECG_total_rows)


# BCGdataX=BCGdataX.tz_convert('Asia/Shanghai')


BCGX = BCGdataX
BCGY = BCGdataY
ECGX = ECGdataX
ECGY = ECGdataY

# print(BCGdataX)
# print(ECGdataX)
# print(BCG_total_line)
# print(ECG_total_line)



fig=plt.figure()
#fig1
ax1=fig.add_subplot(2,1,1)  
ax1.plot(BCGX,BCGY)
ax1.set_title(BCGxlabel[0])

#fig2
ax2=fig.add_subplot(2,1,2)
ax2.plot(ECGX,ECGY)
ax2.set_title(ECGxlabel[0])


plt.show()

