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


#Define List
DeviceID_One_CH_List=[]
Time_One_CH_List=[]
DeviceID_Two_CH_List=[]
Time_Two_CH_List=[]



DeviceNum_List="B7"
FileData=[]
HumanData=[]
StrConvertList=['00','01','02','03','04','05','06','07','08','09']


def StrCovertAll(Head_M,Head_D,Tail_M,Tail_D):

    if int(Head_M)<10:
        Temp=StrConvertList[int(Head_M)]
        Head_M=Temp

    if int(Head_D)<10:
        Temp=StrConvertList[int(Head_D)]
        Head_D=Temp

    if int(Tail_M)<10:
        Temp=StrConvertList[int(Tail_M)]
        Tail_M=Temp

    if int(Tail_D)<10:
        Temp=StrConvertList[int(Tail_D)]
        Tail_D=Temp

    return Head_M,Head_D,Tail_M,Tail_D





def StrCombine(DeviceID_List,Time_List,NumSer):
   
    StrIDTemp=str(DeviceID_List[NumSer])
    StrID=StrIDTemp[2:18]
    StrTimeTemp=Time_List[NumSer]

    StrHead_Y=StrTimeTemp[1:5]
    StrHead_M=StrTimeTemp[5:7]
    StrHead_D=StrTimeTemp[7:9]
    
    if(StrHead_D=="31"):
        Strtail_D="01"
        Strtail_M=int(StrHead_M)+1
    else:
        Strtail_D=int(StrHead_D)+1
        Strtail_M=StrHead_M

    StrHead_M,StrHead_D,Strtail_M,Strtail_D=StrCovertAll(StrHead_M,StrHead_D,Strtail_M,Strtail_D)


    PreStr=str(StrID)+','+str(StrHead_Y)+'-'+str(StrHead_M)+'-'+str(StrHead_D)+'-21-00'
    TailStr=str(StrHead_Y)+'-'+str(Strtail_M)+'-'+str(Strtail_D)+'-08-00'
    TotalStr=PreStr+','+TailStr


    return TotalStr

def Config_Write(DeviceID_List,Time_List):   
        
        # Data=open(r"C:\Users\ScHWorkStation\Desktop\DataMark_ZJYY_FilePath.txt","w")
        IDtemp=DeviceID_List[0]
        if(str(int(IDtemp[4])+int(IDtemp[5]))=='1'):
            Data=open(r"C:\Users\ScHWorkStation\Desktop\DataDownLoad_DeviceID_One_CH__Config.txt","w")
        if(str(int(IDtemp[4])+int(IDtemp[5]))=='2'):
            Data=open(r"C:\Users\ScHWorkStation\Desktop\DataDownLoad_DeviceID_Two_CH__Config.txt","w")

        Data.write('http://data.91ganlu.com'+'\n')
        Data.write('http://10.248.248.61:9100'+'\n')
        for i in range(len(DeviceID_List)):
            
            DataPathTemp=StrCombine(DeviceID_List,Time_List,i)
            Data.write(DataPathTemp+'\n')
            

        Data.close()  





def SelectProgram(ID,Time):
    
    for i in range(len(ID)):
        IDtemp=str(ID[i])
        if(IDtemp[4]=='1'):
           DeviceID_One_CH_List.append(str(IDtemp))
           Time_One_CH_List.append(str(Time[i]))
        if(IDtemp[5]=='1'):
           DeviceID_One_CH_List.append(str(IDtemp)) 
           Time_One_CH_List.append(str(Time[i]))
        if(IDtemp[4]=='2'):
           DeviceID_Two_CH_List.append(str(IDtemp))
           Time_Two_CH_List.append(str(Time[i]))
        if(IDtemp[5]=='2'):
           DeviceID_Two_CH_List.append(str(IDtemp))
           Time_Two_CH_List.append(str(Time[i]))

    Config_Write(DeviceID_One_CH_List,Time_One_CH_List)
    Config_Write(DeviceID_Two_CH_List,Time_Two_CH_List)

  
    
def FileDataReader():
    IDTimeFile=input('please input the IDTimeFile:')
    print(IDTimeFile)
   


    pwd = os.getcwd()
    os.chdir(os.path.dirname(IDTimeFile))
    IDTimeFileData = pd.read_csv(os.path.basename(IDTimeFile))
    os.chdir(pwd)



    
    IDTimeFileData_rows = len(IDTimeFileData)
    IDTimeFileData_line = len(IDTimeFileData.columns)
    # IDTimeFileDataID=IDTimeFileData.iloc[0:IDTimeFileData_rows,0:1]         #read the BCGdata matched rows   //ID
    # IDTimeFileDataTime=IDTimeFileData.iloc[0:IDTimeFileData_rows,1:2]         #read the BCGdata matched rows   //Time 
    print(IDTimeFileData_rows)
    IDTimeFileDataID=[]
    IDTimeFileDataTime=[]

    
    for i in range(IDTimeFileData_rows):
        IDTimeFileDataID.append(list(IDTimeFileData.iloc[i][0:1]))
        IDTimeFileDataTime.append(list(IDTimeFileData.iloc[i][1:2]))

    # print(IDTimeFileDataTime)
    return IDTimeFileDataID,IDTimeFileDataTime

   

if __name__ == '__main__':

     
    ID,Time=FileDataReader()
    SelectProgram(ID,Time)
    # MkDirPath=Download_ConfigFile_Input()
    # Config_Write(len(FileData),MkDirPath)
