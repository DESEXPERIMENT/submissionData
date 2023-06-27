import os
import time
import json
# toronto scripts
import ast


fx = open('weatherData.txt','r')
content = fx.read()
fx.close()

content = json.loads(content)
print(content.keys())

weatherTitleToNumber = {'heavy rain': 3, 'sleet': 5, 'clear': 7, 'broken clouds': 11, 'extremely hot': 13, 'dense fog': 17, 'sprinkles': 19, 'fog': 23, 'scattered clouds': 29, 'cool': 31, 'haze': 37, 'rain': 41, 'ice fog': 43, 'warm': 47, 'partly cloudy': 53, 'cloudy': 59, 'light rain': 61, 'hot': 67, 'light fog': 71, 'thunderstorms': 73, 'passing clouds': 79, 'rain showers': 83, 'light snow': 89, 'partly sunny': 97, 'pleasantly warm': 101, 'strong thunderstorms': 103, 'more clouds than sun': 107, 'high level clouds': 109, 'hail': 113, 'quite cool': 127, 'drizzle': 131, 'refreshingly cool': 137, 'snow': 139, 'low clouds': 149, 'mostly cloudy': 151, 'sunny': 157, 'mild': 163, 'thundershowers': 167, 'scattered showers': 173, 'overcast': 179}

weatherPossibilities = []

def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x-1):
	   if x % i == 0:
		   print(i)
num = 21

# print_factors(num)




newData = {}
newData['weatherTitleToNumber'] = weatherTitleToNumber
for city in content:
	newData[city]= {}
	for date in content[city]:
		newData[city][date] = {}
		for hourData in content[city][date]:
			# print(city,date,hourData)

			ctime = hourData['c'][0]['h']
			print('\n',ctime)
			if '<br>' in ctime:
				ctime = ctime[:ctime.index('<br>')]

			ctime = ctime.split(' ')
			ctime[0] = ctime[0][:ctime[0].index(':')]

			chr = int(ctime[0])
			chr = chr%12
			if 'pm' in ctime[1]:
				chr +=12
			chr = str(chr)
			print(chr)
			try:
				val = newData[city][date][chr]
			except:
				newData[city][date][chr] = []
			if 'No' in hourData['c'][4]['h']:
				hourData['c'][4]['h'] = '0'
			hourData['c'][4]['h'] = hourData['c'][4]['h'].replace(' mph','')
			hourData['c'][8]['h'] = hourData['c'][8]['h'].replace('&nbsp;mi','')
			hourData['c'][7]['h'] = hourData['c'][7]['h'].replace(' "Hg','')
			hourData['c'][6]['h'] = hourData['c'][6]['h'].replace('%','')
			hourData['c'][2]['h'] = hourData['c'][2]['h'].replace('&nbsp;°F','')

			# print([hourData['c'][2]['h'],hourData['c'][3]['h'],hourData['c'][4]['h'],hourData['c'][6]['h'],hourData['c'][7]['h'],hourData['c'][8]['h']])


			weatherNumber = 1
			for item in hourData['c'][3]['h'].split('.'):
				item = item.replace('.','')
				item = item.replace('. ','')
				if item != '':
					if item[0] ==' ':
						item= item[1:]
					weatherPossibilities.append(item.lower())
					weatherNumber = weatherNumber*weatherTitleToNumber[item.lower()]

			#temp,clouds,wind,humidity,Barometer pressure,visibility,weatherNumber

			newData[city][date][chr].append([hourData['c'][2]['h'],hourData['c'][3]['h'],hourData['c'][4]['h'],hourData['c'][6]['h'],hourData['c'][7]['h'],hourData['c'][8]['h'],weatherNumber])

		# time.sleep(1000)

fx = open('weatherDataDict.txt','w')
fx.write(json.dumps(newData))
fx.close()
# primes = [ 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
#
#
# weatherPossibilities = list(set(weatherPossibilities))
# print(weatherPossibilities,len(weatherPossibilities))
#
# weatherNumbers = {}
# for i in range(0,len(weatherPossibilities)):
#     weatherNumbers[weatherPossibilities[i]] = primes[i]
#
# print(weatherNumbers)
