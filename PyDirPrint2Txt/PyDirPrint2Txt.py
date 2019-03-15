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

def file_name(file_dir):   
        
        Data=open(r"C:\Users\ScHWorkStation\Desktop\DataMark_ZJYY_FilePath.txt","w")
        for root, dirs, files in os.walk(file_dir):
            print(root) #当前目录路径
            # print(dirs) #当前路径下所有子目录  
            # print(files) #当前路径下所有非目录子文件  

            Data.write(root+'\n')

        Data.close()  



def BCG_CsV_FilePath_Input():
    FileDirPath=input('Please Input the FileDirPath:')
    print(FileDirPath)


    file_name(FileDirPath)
  
    


   

if __name__ == '__main__':

    # while(1):
        BCG_CsV_FilePath_Input()