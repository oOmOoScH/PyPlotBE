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


DeviceNum_List="B2-B6-B7"
#Define List
Config_StartTime=[]
Config_EndTime=[]
StrConvertList=['00','01','02','03','04','05','06','07','08','09']


#Define Array
# arr_StartTime=np.zeros((0))
# arr_EndTime=np.zeros((0))

#Define tuple
# tup_StartTime=()
# tup_EndTime=()

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

    if NumSer==0:
        StrHead_Y=Config_StartTime[0]
        StrHead_M=Config_StartTime[1]
        StrHead_D=ConInt_StartTime(2)+NumSer

        StrTail_Y=StrHead_Y
        StrTail_M=StrHead_M
        StrTail_D=int(StrHead_D)+1

    elif int(StrHead_D)==30:
       
        StrHead_D=StrTail_D

        StrTail_M=int(StrHead_M)+1
        StrTail_D=1
    
    elif int(StrHead_D)>30:
        StrHead_M=StrTail_M
        StrHead_D=StrTail_D

        StrTail_D=int(StrHead_D)+1

    else :
        StrHead_D=StrTail_D

        StrTail_D=int(StrHead_D)+1
    


    StrHead_M,StrHead_D,StrTail_M,StrTail_D=StrCovertAll(StrHead_M,StrHead_D,StrTail_M,StrTail_D)

    StrHead=DeviceNum_List+','+str(StrHead_Y)+'-'+str(StrHead_M)+'-'+str(StrHead_D)+'-21-00,'
    StrTail=str(StrTail_Y)+'-'+str(StrTail_M)+'-'+str(StrTail_D)+'-09-00'
    TotalStr=StrHead+StrTail

    return TotalStr


def ConInt_StartTime(NumberSerial):

    return int(Config_StartTime[NumberSerial])

def ConInt_EndTime(NumberSerial):

    return int(Config_EndTime[NumberSerial])

def Config_Write(TotalDays):   
        
        # Data=open(r"C:\Users\ScHWorkStation\Desktop\DataMark_ZJYY_FilePath.txt","w")
        Data=open(r"C:\Users\ScHWorkStation\Desktop\DataMark_ZJYY_Config.txt","w")

        Data.write('http://data.91ganlu.com'+'\n')
        Data.write('http://10.248.248.61:9100'+'\n')
        for i in range(TotalDays):
            
           
            Data.write(StrCombine(i)+'\n')

        Data.close()  



def Download_ConfigFile_Input():
    StartTime=input('Please Input the StartTime:')
    EndTime=input('Please Input the  EndTime :')
    print(StartTime+"_"+"To"+"_"+EndTime)


    print(int(StartTime[5:7]))
    print(int(EndTime[5:7]))

    
    
    #0_Year   1_Month  2_Day
    Config_StartTime.append(StartTime[0:4])
    Config_StartTime.append(StartTime[5:7])
    Config_StartTime.append(StartTime[8:10])
    Config_EndTime.append(EndTime[0:4])      
    Config_EndTime.append(EndTime[5:7])       
    Config_EndTime.append(EndTime[8:10])  




    TotalDays=(ConInt_EndTime(0)-ConInt_StartTime(0))*365+(ConInt_EndTime(1)-ConInt_StartTime(1))*30+(ConInt_EndTime(2)-ConInt_StartTime(2))+2
    print(TotalDays)


    Config_Write(TotalDays)
  
    


   

if __name__ == '__main__':

    
    # while(1):
    
    Download_ConfigFile_Input()