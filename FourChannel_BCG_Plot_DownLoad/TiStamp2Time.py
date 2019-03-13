import time,datetime
import pandas as pd   
from datetime import timedelta

def TStamp2Time(SecondStyles,timestamp,UTC):

    if (SecondStyles== "ms")&(UTC=="False"):
        utc_time=pd.to_datetime(timestamp,unit='ms')     #UTC Standard Time _ms_level 
        Time = utc_time + timedelta(hours=8)             #UTC Convert BeiJingTime 
        return  Time

    elif (SecondStyles=="s")&(UTC=="False"):
        utc_time=pd.to_datetime(timestamp,unit='s')       #UTC Standard Time_S_level 
        Time = utc_time + timedelta(hours=8)              #UTC Convert BeiJingTime
        return  Time

    elif (SecondStyles== "ms")&(UTC=="True"):
        utc_time=pd.to_datetime(timestamp,unit='ms')       #UTC Standard Time_ms_level 
        return  utc_time

    elif (SecondStyles=="s")&(UTC=="True"):
        utc_time=pd.to_datetime(timestamp,unit='s')        #UTC Standard Time_ms_level 
        return  utc_time
