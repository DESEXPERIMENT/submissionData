import os
import time
import json
# toronto scripts
import ast


full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'



cityServices = {}
#cylce y/n
#circ, Lime ,Jump, LyftScooter, Bird, Skip, Spin, Voi, Tier, Wind ,Movo, Scoot
# n  , y    , y  , n          , n    , n ,   n   , n ,  n  ,  n  ,  n , n
cityServices['DC'] = 'usa/washington-dc'
cityServices['SanFrancisco'] = 'usa/san-francisco'
cityServices['TelAviv'] = 'israel/tel-avi'
cityServices['MexicoCity'] = 'mexico/mexico-city'
cityServices['Brussels'] = 'belgium/brussels'
cityServices['Chicago'] = 'usa/chicago'
cityServices['Zurich'] = 'switzerland/zurich'
cityServices['Detroit'] = 'usa/detroit'
cityServices['Lisbon'] = 'portugal/lisbon'
cityServices['Paris'] = 'france/paris'
cityServices['Madrid'] = 'spain/madrid'
import requests




URL = 'https://www.timeanddate.com/scripts/cityajax.php?n=usa/raleigh&mode=historic&hd=20191001&month=10&year=2019&json=1'
weatherData = {}

for city in cityServices:
	weatherData[city] = {}
	month = 6
	day = 19
	year = 2019
	cityText = cityServices[city]
	while month < 11:
		print(month,day, city)
		urlTemp = URL.replace('month=10','month='+str(month))
		urlTemp = urlTemp.replace('usa/raleigh',cityText)
		# urlTemp = urlTemp.replace('month=6','month='+str(month))
		monthString = str(month)
		dayString = str(day)
		if len(monthString)==1:
			monthString = '0'+monthString

		if len(dayString)==1:
			dayString = '0'+dayString


		urlTemp = urlTemp.replace('hd=20191001','hd=2019'+str(monthString)+str(dayString))

		# print(urlTemp)
		# time.sleep(10000)
		r = requests.get(url = urlTemp)
		data = r.text
		if r.status_code == 200:
			if 'No data available' not in data:
				data = data.replace('c:','"c":')
				data = data.replace('h:','"h":')
				data = data.replace('s:','"s":')
				#fx = open('tempData.txt','w')
				#fx.write(data)
				#fx.close()
				weatherData[city]['2019-'+monthString+'-'+dayString] = json.loads(data)
		else:
			print('ERROR!! ',r.status_code)
			print('\t',urlTemp)
		# print(data)
		# time.sleep(10000)
		day += 1
		if day == 32:
			day = 1
			month += 1

fx = open('weatherData.txt','w')
fx.write(json.dumps(weatherData))
fx.close()
