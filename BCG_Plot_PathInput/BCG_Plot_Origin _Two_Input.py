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

from numba import jit
from numpy import arange
import time


# @jit
def BCG_CsV_File_Plot():
    
    BCGFile=input('please input the BCGFilePath:')
    print(BCGFile)
   

    BCGxlabel=BCGFile.split('\\')
    BCGxlabel=BCGxlabel[(len(BCGxlabel)-1)]
    BCGxlabel=BCGxlabel.split('.')

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


    BCGX = BCGdataX
    BCGY = BCGdataY


    return BCGX,BCGY,BCGxlabel


def FigPlot(BCGX1,BCGY1,BCGxlabel1,BCGX2,BCGY2,BCGxlabel2):
    fig=plt.figure()
    #fig1
    ax1=fig.add_subplot(2,1,1)  
    # ax1=fig.add_subplot(1,1,1)  
    ax1.plot(BCGX1,BCGY1)
    ax1.grid(color='black', linestyle='--', linewidth=1,alpha=0.3)
    ax1.set_title(BCGxlabel1[0])

    # fig2
    ax2=fig.add_subplot(2,1,2)
    ax2.plot(BCGX2,BCGY2)
    ax2.grid(color='black', linestyle='--', linewidth=1,alpha=0.3)
    ax2.set_title(BCGxlabel2[0])




    end_time = time.time()
    print (end_time - start_time)
    
    # plt.savefig('output.jpg', format='jpg')
    plt.show()
    

if __name__ == '__main__':

    while(1):
        start_time = time.time()
        BCGX1,BCGY1,BCGxlabel1=BCG_CsV_File_Plot()
        BCGX2,BCGY2,BCGxlabel2=BCG_CsV_File_Plot()
        FigPlot(BCGX1,BCGY1,BCGxlabel1,BCGX2,BCGY2,BCGxlabel2)
        