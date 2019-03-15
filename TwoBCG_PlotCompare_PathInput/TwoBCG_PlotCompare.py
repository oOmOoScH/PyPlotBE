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






BCGFile=input('Please Input The BCGFilePath:')
print(BCGFile)
BCGFile2=input('Please Input The BCGFilePath2:')
print(BCGFile2)




BCGxlabel=BCGFile.split('\\')
BCGxlabel=BCGxlabel[(len(BCGxlabel)-1)]
BCGxlabel=BCGxlabel.split('.')

pwd = os.getcwd()
os.chdir(os.path.dirname(BCGFile))
BCGData = pd.read_csv(os.path.basename(BCGFile))
os.chdir(pwd)


utc_time=pd.to_datetime(BCGData['time'],unit='ms')  #UTC Standard Time
BCGData['time'] = utc_time + timedelta(hours=8)     #UTC Convert BeiJingTime




BCG_total_rows = len(BCGData)
BCG_total_line = len(BCGData.columns)
BCGdataX=BCGData.iloc[0:BCG_total_rows,0:1]         #read the BCGdata matched rows   //StrTime
BCGdataY=BCGData.iloc[0:BCG_total_rows,1:2]         #read the BCGdata matched rows   //Value 



BCGxlabel2=BCGFile2.split('\\')
BCGxlabel2=BCGxlabel2[(len(BCGxlabel2)-1)]
BCGxlabel2=BCGxlabel2.split('.')

pwd = os.getcwd()
os.chdir(os.path.dirname(BCGFile2))
BCGData2 = pd.read_csv(os.path.basename(BCGFile2))
os.chdir(pwd)


utc_time=pd.to_datetime(BCGData2['time'],unit='ms')  #UTC Standard Time
BCGData2['time'] = utc_time + timedelta(hours=8)     #UTC Convert BeiJingTime




BCG_total_rows2 = len(BCGData2)
BCG_total_line2 = len(BCGData2.columns)
BCGdataX2=BCGData2.iloc[0:BCG_total_rows2,0:1]         #read the BCGdata matched rows   //StrTime
BCGdataY2=BCGData2.iloc[0:BCG_total_rows2,1:2]         #read the BCGdata matched rows   //Value 




BCGX = BCGdataX
BCGY = BCGdataY


BCGX2=BCGdataX2
BCGY2=BCGdataY2




fig=plt.figure()
#fig1
ax1=fig.add_subplot(2,1,1)  
ax1.plot(BCGX,BCGY)
ax1.grid(color='black', linestyle='--', linewidth=1,alpha=0.3)
ax1.set_title(BCGxlabel[0])

# #fig2
# ax2=fig.add_subplot(4,1,2)
# ax2.plot(BCGY)
# ax2.grid(color='black', linestyle='--', linewidth=1,alpha=0.3)
# ax2.set_title(BCGxlabel[0])

# fig3
ax3=fig.add_subplot(2,1,2)  
ax3.plot(BCGX2,BCGY2)
# ax3.plot(BCGX, BCGY, color='red', label=BCGxlabel[0])
ax3.grid(color='black', linestyle='--', linewidth=1,alpha=0.3)
ax3.set_title(BCGxlabel2[0])



# # fig4
# ax4=fig.add_subplot(4,1,4)  
# ax4.plot(BCGY2)
# ax4.grid(color='black', linestyle='--', linewidth=1,alpha=0.3)
# ax4.set_title(BCGxlabel2[0])



plt.show()

