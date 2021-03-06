from ctypes import Structure, windll, c_uint, sizeof, byref
import time
import requests
import os
import json
import sys

conf={}


try:
    with open(os.path.dirname(os.path.realpath(__file__))+'\\config.json', 'r') as c:
        data=c.read()
        conf = json.loads(data)
except IOError:
    sys.exit()

class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0

def home_assistant(status):
    url = conf['url']
    body = {
        "state": status
    }

    headers = {
	    "Authorization": "Bearer "+conf['auth'],
    }
    try:
        response = requests.request("POST", url, headers=headers, data=json.dumps(body))
    except:
    	pass
    
while True:
	if get_idle_duration() >= conf['consider_afk']:
		home_assistant('off')
	else:
		home_assistant('on')
	time.sleep(conf['interval'])