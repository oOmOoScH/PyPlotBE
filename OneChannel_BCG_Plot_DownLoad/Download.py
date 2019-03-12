import requests


def Dataload(sn, start, end):
    try:
        url = "http://10.248.248.61:9100/data/download"
        #url = "http://data.91ganlu.com/data/download"
        querystring = {"sn": sn, "start": start, "end": end}
        response = requests.get( url, params=querystring, timeout = 500)
    except Exception as e:
       url = "http://data.91ganlu.com/data/download"
       querystring = {"sn": sn, "start": start, "end": end}
       response = requests.get( url, params=querystring, timeout = 500)
       e=url
       print(e)
    
    return response.text




# data = Dataload("BB1000c600000000", "1543338000000", "1543338600000")
# print(data)
# 1543338000000
# 1543732356
