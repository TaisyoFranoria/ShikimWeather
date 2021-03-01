import subprocess as sp
import random
import os
import Weather

print('直近の天気を調べるね')
order = 0
wd = Weather.Weather()
Say =  wd.getLocation()+'の'+wd.getDate(order)+'の天気は['+wd.getWeathers(order)+']だよ'
if(wd.getDate(0)=='None' or wd.getWeathers(order)=='None'):
    Say = '何もみえないよ。'
#Say = '天気予報機能は現在メンテナンス中だよ'
Num = str(random.randint(0,1))
sp.Popen(['./ss.sh',Num,Say],cwd=os.path.dirname(__file__))

