import subprocess as sp
import random
import os
import Weather
import datetime

# test
t_delta = datetime.timedelta(hours=9)
JST = datetime.timezone(t_delta, 'JST')
now = datetime.datetime.now(JST)
print(now)
#

print('直近の天気を調べるね')
order = 0
wd = Weather.Weather()
Say =  wd.getLocation()+'の'+wd.getDate(order)+'の天気は['+wd.getWeathers(order)+']だよ'
if(wd.getDate(0)=='None' or wd.getWeathers(order)=='None'):
    Say = '何もみえないよ。'
#Say = '天気予報機能は現在メンテナンス中だよ'
Num = str(random.randint(0,1))

#Python3;.9~
#dirname=os.path.dirname(__file__)
#Python~3.8
dirname=os.path.dirname(os.path.abspath(__file__))
shellpath=dirname+'/ShikimiShellArt.sh'
sp.Popen([shellpath,Num,Say],cwd=dirname)

