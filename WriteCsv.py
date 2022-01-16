import csv
import Weather

path = 'wd.csv'
wd = Weather.Weather()
with open(path,mode='w') as f:
    f.write(wd.getTimeDay())
    f.write(',')
    f.write(wd.getThisWeather()) 
f.close()

