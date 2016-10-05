import requests
import json
from datetime import timedelta
from datetime import datetime

def initialPost():
    url = 'http://challenge.code2040.org/api/dating'
    payload = {'token':'f13b411e75521c7338e9e553d0c197e9'}
    original = requests.post(url, params=payload)
    return original.json()

def finalPost(datestamp):
    url = 'http://challenge.code2040.org/api/dating/validate'
    payload = {'token':'f13b411e75521c7338e9e553d0c197e9', 'datestamp':datestamp}
    original = requests.post(url, json=payload)

def getYMD(datestamp):
    ymd = [] #year, month, day list
    ymd.append(int(datestamp[0:4]))
    ymd.append(int(datestamp[5:7]))
    ymd.append(int(datestamp[8:10]))
    return ymd

def getHMS(datestamp):
    hms = [] #hour, minute, second list
    hms.append(int(datestamp[11:13]))
    hms.append(int(datestamp[14:16]))
    hms.append(int(datestamp[17:19]))
    return hms

def datetimeToISO(datetimeObj):
    datetimeObj = datetimeObj.isoformat() + "Z"
    return datetimeObj

############################ Main ############################

datestampAndInterval = initialPost()

originDS = datestampAndInterval['datestamp']
interval = datestampAndInterval['interval']

#place elements into lists for easier accessibility
ymd = getYMD(originDS)
hms = getHMS(originDS)

#object stores elements in ymdhms format
datetimeObj = datetime(year = ymd[0], month = ymd[1], day = ymd[2],
                        hour = hms[0], minute = hms[1], second = hms[2])
#allows for addition of datetime objects
seconds = timedelta(seconds=interval)

#new time from adding original iso time and interval
datetimeNew = datetimeObj + seconds

#convert datetime to iso format
finalDS = datetimeToISO(datetimeNew)

finalPost(finalDS)
