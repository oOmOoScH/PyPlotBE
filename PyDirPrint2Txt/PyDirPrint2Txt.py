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
DirsData=[]



def Config_Write(FileDataNum):   
        
        # Data=open(r"C:\Users\ScHWorkStation\Desktop\DataMark_ZJYY_FilePath.txt","w")
        print(FileDataNum)
        Data=open(r"C:\Users\ScHWorkStation\Desktop\DataMark_ZJYY.txt","w")

        Data.write('Data_Mark'+'\n')
        Data.write('Total：'+str(FileDataNum)+'\n')
        for i in range(FileDataNum):
            
            Data.write(DirsData[0][i][0:10]+'\n')
            

        Data.close()  


def file_name(file_dir):   
        
    for root, dirs, files in os.walk(file_dir):
            # print(root) #当前目录路径
            # print(dirs) #当前路径下所有子目录  
            # print(files) #当前路径下所有非目录子文件  
            root
            dirs
            DirsData.append(dirs)
            files
    
    # print(len(DirsData[0]))
    # print(DirsData[0][1][0:10])


    Config_Write(len(DirsData[0]))
     
        





def Download_ConfigFile_Input():
    FileDirPath=input('Please Input the FileDirPath:')
    print(FileDirPath)


    file_name(FileDirPath)
  
    


   

if __name__ == '__main__':

    # while(1):
    Download_ConfigFile_Input()
    