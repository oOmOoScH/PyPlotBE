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

#Define Path
MkDirPath='H:/zjyy/三墩院区A6/Marked/20190222_20190307'

#Define List
DeviceNum_List="B2-B6-B7"
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



def StrCombine(NumSer):
    global StrHead_Y,StrHead_M,StrHead_D
    global StrTail_Y,StrTail_M,StrTail_D

    StrHead_Y=FileData[NumSer][0]
    StrHead_M=FileData[NumSer][1]
    StrHead_D=FileData[NumSer][2]

    StrTail_Y=StrHead_Y
    if int(StrHead_D)==31:
        StrTail_M=int(StrHead_M)+1
    else:
        StrTail_M=StrHead_M


    if int(StrHead_D)==31: 
        StrTail_D=1
    else:
        StrTail_D=int(StrHead_D)+1


    StrHead_M,StrHead_D,StrTail_M,StrTail_D=StrCovertAll(StrHead_M,StrHead_D,StrTail_M,StrTail_D)

    StrHead=DeviceNum_List+','+str(StrHead_Y)+'-'+str(StrHead_M)+'-'+str(StrHead_D)+'-21-00,'
    StrTail=str(StrTail_Y)+'-'+str(StrTail_M)+'-'+str(StrTail_D)+'-09-00'
    TotalStr=StrHead+StrTail

    DirStr=str(StrHead_Y)+'-'+str(StrHead_M)+'-'+str(StrHead_D)+'-21-00-'+StrTail


    return DirStr,TotalStr

def Config_Write(FileDataNum):   
        
        # Data=open(r"C:\Users\ScHWorkStation\Desktop\DataMark_ZJYY_FilePath.txt","w")
        print(FileDataNum)
        Data=open(r"C:\Users\ScHWorkStation\Desktop\DataMark_ZJYY_Config.txt","w")

        Data.write('http://data.91ganlu.com'+'\n')
        Data.write('http://10.248.248.61:9100'+'\n')
        for i in range(FileDataNum):
            
            PathStrTemp,DataPathTemp=StrCombine(i)
            Data.write(DataPathTemp+'\n')
            TempPath=MkDirPath+'/'+PathStrTemp+'/'
            os.makedirs(TempPath)

        Data.close()  




def file_name(file_dir):   
        
        for root, dirs, files in os.walk(file_dir):
            # print(root) #当前目录路径
            # print(dirs) #当前路径下所有子目录  
            # print(files) #当前路径下所有非目录子文件  
            root
            dirs
            files

            
        for i in range(len(files)):
            temp=files[i].split('-')
            FileData.append(temp[0:3])
            HumanData.append(temp[3:4])





def Download_ConfigFile_Input():
    FileDirPath=input('Please Input the FileDirPath:')
    print(FileDirPath)


    file_name(FileDirPath)
  
    


   

if __name__ == '__main__':

    # while(1):
    Download_ConfigFile_Input()
    Config_Write(len(FileData))
