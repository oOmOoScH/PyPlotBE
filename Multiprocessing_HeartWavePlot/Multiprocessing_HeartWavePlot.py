import numpy as np
import multiprocessing
from multiprocessing import Queue
from multiprocessing import Manager
from psutil import cpu_count,virtual_memory

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




# Splice Parameters
SpliceFactor=2

# List 
heartwave = []

HRWaveTemp= []
HRWaveDateProcessNum=[]
heartwaveDateProcess=[]
heartwaveDateProcessTemp=[]




def CPU_Mem_Information_Initial():
   
    global SpliceFactor
   
    # CPU_Info_Initial
    if cpu_count()<4:
        SpliceFactor=2
    else:
        SpliceFactor=cpu_count()-2
    
    
     # Mem_Info_Initial
    phymem=virtual_memory()
    print('MultiProcesses_CPU_Enable:'+str(SpliceFactor))
    print('Used_Mem :',str(round(phymem.used/1024/1024/1024,1))+'G')
    print('Total_Mem:',str(round(phymem.total/1024/1024/1024,1))+'G')
    print('Free_Mem :',str(round(phymem.free/1024/1024/1024,5))+'G')

    

def DateProcess(DataBlock_total_rows,BCG_DataBlock,DataBlock_NumSer,M_queue,heartwaveDateProcess):
    #  12bit Heartbeat Signal  parameters
    ave_hrData = 2050.0
    std_hrData = 100.0
    ave_std_hrData=400.0
    factor=12.0
    DataBlock_NumSer_Temp=[]  
    for i in range(DataBlock_total_rows):
        ave_hrData = ((factor-1) * ave_hrData + BCG_DataBlock.at[(i+DataBlock_NumSer*DataBlock_total_rows),'value'])/factor
        std_hrData = ((factor-1)*std_hrData + abs(BCG_DataBlock.at[(i+DataBlock_NumSer*DataBlock_total_rows),'value']-ave_hrData))/factor
        ave_std_hrData = ((factor-1) * ave_std_hrData + 1 * std_hrData) / factor
        DataBlock_NumSer_Temp.append(ave_std_hrData)

    
    print('MultiProcesses'+'_'+str(DataBlock_NumSer)+'_'+str(len(DataBlock_NumSer_Temp)))
    DataBlock_NumSer_Temp.append(DataBlock_NumSer)
    M_queue.put(DataBlock_NumSer_Temp)
    print('MultiProcesses'+'_'+str(DataBlock_NumSer)+'_'+'M_queue.Put'+'_'+str(M_queue.qsize())) 
    
    

def DataObtain():


    BCGFile=input('Please Input The BCGFilePath:\n')
    print(BCGFile)

    # BCGFile2=input('Please Input The BCGFilePath2:')
    # print(BCGFile2)



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


    # BCGxlabel2=BCGFile2.split('\\')
    # BCGxlabel2=BCGxlabel2[(len(BCGxlabel2)-1)]
    # BCGxlabel2=BCGxlabel2.split('.')

    # pwd = os.getcwd()
    # os.chdir(os.path.dirname(BCGFile2))
    # BCGData2 = pd.read_csv(os.path.basename(BCGFile2))
    # os.chdir(pwd)

    BCGX = BCGdataX
    BCGY = BCGdataY

    return BCGxlabel,BCGX,BCGY,BCG_total_rows



def MultiProcesses(SpliceFactor,DataBlock_total_rows,BCG_DataBlock,M_queue,heartwaveDateProcess):
    # with Manager() as mg:
    #     heartwaveDateProcessTemp = mg.list()
    DeviceProcesses=[]
    for i in range(int(SpliceFactor)):
        t =multiprocessing.Process(target=DateProcess, args=(DataBlock_total_rows,BCG_DataBlock[i],i,M_queue,heartwaveDateProcess))
        DeviceProcesses.append(t)
        t.start()
    
    # for res in DeviceProcesses:  
    #     res.join()  

    while(M_queue.qsize()<(SpliceFactor)) :
        if i ==(SpliceFactor-1) :
            print('Waiting_For_the_M_queue_To_be_Filled.............\n')
            i=(SpliceFactor+2)
    



def OneChannel_BCG_Plot(BCGX,BCGY,BCGxlabel,heartwave):

    fig=plt.figure()
    #fig1
    ax1=fig.add_subplot(2,1,1)  
    ax1.plot(BCGX,BCGY)
    ax1.grid(color='black', linestyle='--', linewidth=1,alpha=0.3)
    ax1.set_title(BCGxlabel[0])



    # fig2
    ax2=fig.add_subplot(2,1,2)  
    ax2.plot(BCGX,heartwave)
    # ax3.plot(BCGX2,heartwave, color='red', label="16bit")
    # ax3.plot(BCGX, BCGY, color='red', label=BCGxlabel[0])
    ax2.grid(color='black', linestyle='--', linewidth=1,alpha=0.3)
    ax2.set_title('Python'+'_'+"Heartbeat")

    #fig3
    # ax3=fig.add_subplot(3,1,3)  
    # ax3.plot(MatHeartYWave)
    # ax3.grid(color='black', linestyle='--', linewidth=1,alpha=0.3)
    # ax3.set_title('MatLab'+'_'+"Heartbeat")


    plt.show()






if __name__ == '__main__':

    M_queue=Queue()                                 # M_queue_Initial
    
    CPU_Mem_Information_Initial()

    heartwaveDateProcess=[0]*SpliceFactor
    # Initial_Complete
    print('Initial_HeartWaveDateProcess_List'+':'+str(heartwaveDateProcess))
    
    BCGxlabel,BCGX,BCGY,BCG_total_rows=DataObtain()
    DataBlock_total_rows=int((BCG_total_rows)/SpliceFactor)
  
    for i in range (SpliceFactor):
        Temp=BCGY.iloc[(i*DataBlock_total_rows):(DataBlock_total_rows*(i+1)),0:1] 
        HRWaveTemp.append(Temp)



    print('DataBlock_total_rowslen'+'_'+str(len(HRWaveTemp[1])))
    print('MultiProcesses_Start')

    MultiProcesses(SpliceFactor,DataBlock_total_rows,HRWaveTemp,M_queue,heartwaveDateProcess)
   
   
    while((M_queue.qsize())!=SpliceFactor):
        pass  
    
    if ((M_queue.qsize())==SpliceFactor):
        for x in range (SpliceFactor):
            heartwaveDateProcess[x]=M_queue.get() 
    else:
        print('M_queue_Size_Not_Correct\n')

    for x in range (SpliceFactor):
        HRWaveDateProcessNum.append(heartwaveDateProcess[x][DataBlock_total_rows])
        
    
    print('HRWaveDateProcessNum_Index'+'_'+str(HRWaveDateProcessNum))
    
    for N in range (SpliceFactor):
        NumTemp=HRWaveDateProcessNum.index(N)
        print('HRWaveDateProcessNum_Index'+'_'+str(NumTemp)+'_Match_To_Num_'+str(N))
        DataTemp=heartwaveDateProcess[NumTemp]
        print('heartwaveDateProcess'+'_'+str(NumTemp)+'_'+str(len(DataTemp)))
        DataTemp.pop()
        print('heartwaveDateProcess_PoP.last'+'_'+str(NumTemp)+'_'+str(len(DataTemp)))
        heartwave.extend(DataTemp)
        print('heartwave_Len'+'_'+str(len(heartwave)))

    OneChannel_BCG_Plot(BCGX,BCGY,BCGxlabel,heartwave)