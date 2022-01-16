import subprocess as sp
import requests as rq
from bs4 import BeautifulSoup

class Weather:
    responce = None
    soup = None
    targetData = None
    timeday = None
    thisweather=None
    def __init__(self):
        try:
            self.responce = rq.get("https://www.jma.go.jp/jp/yoho/319.html")
            self.soup = BeautifulSoup(self.responce.text,'html.parser')
            self.targetData = self.soup.html.body.find('th',class_="weather")
            self.timeday = str(self.targetData.text).strip()
            self.thisweather = str(self.targetData.img.get("title")).strip()
            return
        except rq.ConnectionError:
            print('インターネットに接続していません')
            self.timeday = 'None'
            self.thisweather = 'None'
            return
            
    def getTimeDay(self):
        return self.timeday
    
    def getThisWeather(self):
        return self.thisweather
