import Weather
import sys

args=sys.argv
areacode=args[1]
order = 0
wd = Weather.Weather(areacode)
Say =  wd.getLocation()+'の'+wd.getDate(order)+'の天気は['+wd.getWeathers(order)+']だよ'
if(wd.getDate(0)=='None' or wd.getWeathers(order)=='None'):
    Say = '何もみえないよ。'
    print(Say)
    sys.exit(1)

print(Say)
sys.exit(0)

    

