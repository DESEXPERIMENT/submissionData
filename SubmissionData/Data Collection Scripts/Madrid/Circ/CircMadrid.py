import os 
import http.client
import time
import gzip
from io import BytesIO
import zlib, base64
import json
from threading import Thread
import threading
from time import sleep
import time
import http.client
import time
import gzip
from io import BytesIO
import zlib, base64
import json
import random
conn= ''
headersDynamic= []
import _thread
import datetime
from multiprocessing import Process, Lock, Manager, Value
import os
import http.client
import time
import gzip
from io import BytesIO
import zlib, base64
from ctypes import c_char_p
import json
import _thread
import datetime
headersDynamic = {}
cityCoords = []
leftCol = [40.473134, -3.751210 ,40.387168, -3.742894]
rightCol = [40.480627, -3.642151 ,40.388023, -3.646654]

leftCols = []
rightCols = []


full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'


urlsList = [
'/api/Mobile/Scooters?userLatitude=40.41670608520508&userLongitude=-3.7035820484161377&lang=en&latitude=40.40411207678149&longitude=-3.707305211573839&latitudeDelta=0.16279727771530617&longitudeDelta=0.12092370539903685',
'/api/Mobile/Scooters?userLatitude=40.41670608520508&userLongitude=-3.7035820484161377&lang=en&latitude=40.385882534660425&longitude=-3.681821543723345&latitudeDelta=0.16284135817638656&longitudeDelta=0.12092370539903685',
'/api/Mobile/Scooters?userLatitude=40.41670608520508&userLongitude=-3.7035820484161377&lang=en&latitude=40.41177297607259&longitude=-3.6770247481763363&latitudeDelta=0.1627787481422871&longitudeDelta=0.12092370539903641',
'/api/Mobile/Scooters?userLatitude=40.41670608520508&userLongitude=-3.7035820484161377&lang=en&latitude=40.43912457139304&longitude=-3.671684470027685&latitudeDelta=0.1627125685419415&longitudeDelta=0.12092370539903641',
'/api/Mobile/Scooters?userLatitude=40.41670608520508&userLongitude=-3.7035820484161377&lang=en&latitude=40.432521289309996&longitude=-3.714348692446947&latitudeDelta=0.16272854916203983&longitudeDelta=0.12092370539903685',
'/api/Mobile/Scooters?userLatitude=40.41670608520508&userLongitude=-3.7035820484161377&lang=en&latitude=40.45574525085337&longitude=-3.706713113933802&latitudeDelta=0.16267233522692237&longitudeDelta=0.12092370539903641',
'/api/Mobile/Scooters?userLatitude=40.41670608520508&userLongitude=-3.7035820484161377&lang=en&latitude=40.463137532360825&longitude=-3.6698555387556553&latitudeDelta=0.16265443649459144&longitudeDelta=0.12092370539903685',
'/api/Mobile/Scooters?userLatitude=40.41670608520508&userLongitude=-3.7035820484161377&lang=en&latitude=40.42276344430324&longitude=-3.6938019655644894&latitudeDelta=0.16275216019111127&longitudeDelta=0.12092370539903641',
'/api/Mobile/Scooters?userLatitude=40.41670608520508&userLongitude=-3.7035820484161377&lang=en&latitude=40.4157217973745&longitude=-3.715235833078623&latitudeDelta=0.1627691959112454&longitudeDelta=0.12092370539903685'
]

def CityCoordinates():
	global cityCoords
	global leftCol
	global rightCol
	global rightCols
	global leftCols
	mycityCoordinates= [

	40.486824, -3.752791, #upper left
	40.486078, -3.660125, #upper right
	40.380847, -3.752254, # lower left 
	40.381168, -3.658961, #lower right
	]


	numberOfThreadsInRow = 5
	x1 = leftCol[0]
	y1 = leftCol[1]
	x2 = leftCol[2]
	y2 = leftCol[3]

	yRatio = y2 - y1
	xRatio = x2 - x1
	#print("Row 1:\n\n")
	i = 0
	cindex =0

	while i<= 1.000000000001:
		#print("%.6f" % (x1+((i) * xRatio)), ",", "%.6f" % (y1+((i) * yRatio)), "-", i)
		str3 = "%.6f" % (x1+((i) * xRatio))
		
		#coords[cindex] = float(str3)
		#cindex += 1
		str4 = "%.6f" % (y1+((i) * yRatio))
		#coords[cindex] = float(str3)

		#coords[cindex] += 0.0000003
		cindex += 1
		#print('Left ',str3, ",", str4, "-", cindex)
		leftCols.append(float(str3))
		leftCols.append(float(str4))
		i = i + (1/(numberOfThreadsInRow))

	numberOfThreadsInRow = 5
	x1 = rightCol[0]
	y1 = rightCol[1]
	x2 = rightCol[2]
	y2 = rightCol[3]

	yRatio = y2 - y1
	xRatio = x2 - x1
	#print("Row 1:\n\n")
	i = 0
	cindex =0

	while i<= 1.000000000001:
		#print("%.6f" % (x1+((i) * xRatio)), ",", "%.6f" % (y1+((i) * yRatio)), "-", i)
		str3 = "%.6f" % (x1+((i) * xRatio))
		
		#coords[cindex] = float(str3)
		#cindex += 1
		str4 = "%.6f" % (y1+((i) * yRatio))
		#coords[cindex] = float(str3)

		#coords[cindex] += 0.0000003
		cindex += 1
		#print('Right ',str3, ",", str4, "-", cindex)
		rightCols.append(float(str3))
		rightCols.append(float(str4))
		i = i + (1/(numberOfThreadsInRow))


	maxRows = 5
	currRow = 1
	for k in range (0,int(len(rightCols)/2)):

		numberOfThreadsInRow = 5
		x1 = leftCols[2*k]
		y1 = leftCols[2*k+1]
		x2 = rightCols[2*k]
		y2 = rightCols[2*k+1]

		yRatio = y2 - y1
		xRatio = x2 - x1
	#	print("Row 1:\n\n")
		i = 0
		cindex =0
		coor = 0
		while i<= 1.000000000001:
			#print("%.6f" % (x1+((i) * xRatio)), ",", "%.6f" % (y1+((i) * yRatio)), "-", i)
			str3 = "%.6f" % (x1+((i) * xRatio))
		
			#coords[cindex] = float(str3)
			#cindex += 1
			str4 = "%.6f" % (y1+((i) * yRatio))
			#coords[cindex] = float(str3)

			#coords[cindex] += 0.0000003
			cindex += 1
			#print('Row ',currRow,':  ',cindex, '-', str3, ",", str4, "-", cindex)
			cityCoords.append(float(str3))
			cityCoords.append(float(str4))
			
			i = i + (1/(numberOfThreadsInRow))
		currRow +=1
		
	print('Done finding coords')


def fillHeaders():
	global headersDynamic
	listHeaders = ''

	
	file = open(dpath +"CircHeaders.txt", "r") 
	i =0
	for line in file: 
		line = line.replace('\n','')
		tempVals = line.split(': ')
		headersDynamic[tempVals[0]] = tempVals[1]
		listHeaders = listHeaders + line;
		i = 1+i


def worker(tid, reqContent):
	global cityCoords
	global dpath
	global urlsList
	#global headersDynamic
	conn = http.client.HTTPSConnection('api.goflash.com', 443)
	tempDict = headersDynamic
	#print(len(cityCoords)/2/21)

	
	latitude = cityCoords[tid*2]
	longitude =  cityCoords[(tid*2) + 1]

	#print(latitude,',',longitude)
	#'/v2/boards?latitude='+str(latitude)+'&longitude='+str(longitude)+''
	milis = int(round(time.time() * 1000))
	conn.request('GET',urlsList[tid],'',tempDict)
	#print('came here at least')
	#current_milli_time = int(round(time.time() * 1000)) - current_milli_time
	response = conn.getresponse()

	#print('came here at least')
	#print(response.status, response.reason,response.headers)
	content_raw = ''
	content_raw = response.read()


	if response.status == 200:

		content = str(tid)+'--'+str(milis)+'--'+content_raw.decode()

		reqContent[tid] = (content_raw)

		print(tid, len(content_raw))
		zCompressed = zlib.compress(content_raw)

		nowf2 = datetime.datetime.now()
		filenm = dpath+"Madrid/P-"+str(tid)+"-responseEncoded-"+nowf2.strftime("%Y-%m-%d")+".txt"
		logFile = open(filenm, "ab")
		toBeWrittenData = ""
		logFile.write(zCompressed)
		logFile.write(b'0x0A')
		logFile.close()
		#f = open('rcdData.txt','w')
		#f.write(content_raw.decode())
		#f.close()
		#print(tid, 'Exception', e)
	else:
		print(tid, content_raw)
		print(response.status)
		jkk = 10
	conn.close()
	

if __name__ == "__main__":
	
	#fillHeaders()
	CityCoordinates()
	numberOfThreads = len(urlsList)#int(len(cityCoords)/2)
#	for i in range(int(len(cityCoords)/2)):
#		print(2*i,(2*i)+1)
		#i+=1
	
	ietc = 0
	print('MY THREADS :',numberOfThreads)
	nowf3 = datetime.datetime.now()
	while  1:

		with Manager() as manager:
			#set 1
			procs = []
			reqContent = manager.dict()
			for i in range(numberOfThreads):
				#print(i)
				p = Process(target=worker, args=(i,reqContent,))
				procs.append(p)
			current_milli_timeLife2 = int(round(time.time() * 1000))
			for i in range(numberOfThreads):
				procs[i].start()
				time.sleep(1)

			for i in range(numberOfThreads):
				procs[i].join()
			current_milli_timeLife2 = int(round(time.time() * 1000)) - current_milli_timeLife2
			# print(d)
			doneHOst = 0
			i =0
			print(ietc, 'Done Circ- Madrid'+str((len(cityCoords)/2))+' reqs in ', current_milli_timeLife2/1000)	
			ietc +=1
			time.sleep(30)