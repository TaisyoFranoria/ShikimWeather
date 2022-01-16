import subprocess as sp
import requests as rq
import json
from bs4 import BeautifulSoup

class Weather:
    responce = None
    data = None
    date_str = None
    date = None

    location = None
    weathers = None
    winds = None
    waves = None
    date_YMD = None
    thisweather=None
    def __init__(self):
        try:
            #新ホームページではエリアコードの値で場所が違うようだ
            self.responce = rq.get("https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json")
            
            self.data=json.loads(self.responce.text)
            self.location=self.data[0]['timeSeries'][0]['areas'][0]['area']['name']
            self.weathers=self.data[0]['timeSeries'][0]['areas'][0]['weathers']
            self.winds=self.data[0]['timeSeries'][0]['areas'][0]['winds']
            self.waves=self.data[0]['timeSeries'][0]['areas'][0]['waves']
            self.date_str=self.data[0]['reportDatetime']
            self.date=self.date_str.split('T')
            self.date_YMD=self.date[0].split('-')
            
            return
        except rq.ConnectionError:
            print('インターネットに接続していません')
            self.timeday = 'None'
            self.thisweather = 'None'
            return
    def getLocation(self):
        return self.location
    def getWeathers(self,order):
        return self.weathers[order]
    def getWaves(self,order):
        return self.waves[order]
    def getWinds(self,order):
        return self.winds[order]
    def getDate(self,order):
        if(order == 1):
            return str(self.date_YMD[0]+'年'+self.date_YMD[1]+'月'+str(int(self.date_YMD[2])+1).zfill(2)+'日')
        elif(order == 2):    
            return str(self.date_YMD[0]+'年'+self.date_YMD[1]+'月'+str(int(self.date_YMD[2])+2).zfill(2)+'日')
        else:
            return str(self.date_YMD[0]+'年'+self.date_YMD[1]+'月'+self.date_YMD[2]+'日')



