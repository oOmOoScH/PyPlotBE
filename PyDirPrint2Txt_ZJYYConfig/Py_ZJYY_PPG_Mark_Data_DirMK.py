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
FileData=[]
DirsData=[]
StrConvertList=['00','01','02','03','04','05','06','07','08','09']

def StrCovertAll(Head_M,Head_D):

    if int(Head_M)<10:
        Temp=StrConvertList[int(Head_M)]
        Head_M=Temp

    if int(Head_D)<10:
        Temp=StrConvertList[int(Head_D)]
        Head_D=Temp


    return Head_M,Head_D



def StrCombine(NumSer):
    global StrHead_Y,StrHead_M,StrHead_D
    global StrTail_Y,StrTail_M,StrTail_D

    StrHead_M=FileData[NumSer][0]
    StrHead_D=FileData[NumSer][1]

    StrHead_M,StrHead_D=StrCovertAll(StrHead_M,StrHead_D)

    DirStr=str(StrHead_M)+'-'+str(StrHead_D)


    return DirStr

def PathStrMKdirs(FileDataNum,OutPutDirPath):   
        
        print(FileDataNum)
        for i in range(FileDataNum):
            
            PathStrTemp=StrCombine(i)
            TempPath=OutPutDirPath+'/'+PathStrTemp+'/'
            os.makedirs(TempPath)





def file_name(file_dir):   
        
        for root, dirs, files in os.walk(file_dir):
            # print(root) #当前目录路径
            # print(dirs) #当前路径下所有子目录  
            # print(files) #当前路径下所有非目录子文件  
            root
            dirs
            DirsData.append(dirs)
            files
        
            
        for i in range(len(DirsData[0])):
            temp=DirsData[0][i].split('-')
            FileData.append(temp[1:3])

        print(FileData)
        print(len(FileData))

        return len(FileData)
     





def FileDirPath_Input():
    FileDirPath=input('Please Input the FileDirPath:')
    print(FileDirPath)

    OutPutDirPath=input('Please Input the OutPutDirPath:')
    print(OutPutDirPath)

    FileDataNum=file_name(FileDirPath)

    return FileDataNum,OutPutDirPath
  
    


   

if __name__ == '__main__':

    # while(1):
    FileDataNum,OutPutDirPath=FileDirPath_Input()
    PathStrMKdirs(FileDataNum,OutPutDirPath)
