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
leftCol = [38.749212, -9.166035, 38.703958, -9.169850]
rightCol = [38.763380, -9.129958, 38.733096, -9.106309]

leftCols = []
rightCols = []

full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'




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


	numberOfThreadsInRow = 20
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

	numberOfThreadsInRow = 20
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


	maxRows = 41
	currRow = 1
	for k in range (0,int(len(rightCols)/2)):

		numberOfThreadsInRow = 20
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

	
	file = open(dpath+"WindHeaders.txt", "r") 
	i =0
	for line in file: 
		line = line.replace('\n','')
		tempVals = line.split(': ')
		headersDynamic[tempVals[0]] = tempVals[1]
		listHeaders = listHeaders + line;
		i = 1+i


def worker(tid, reqContent):
	global cityCoords
	#global headersDynamic
	conn = http.client.HTTPSConnection('api-prod.ibyke.io', 443)
	tempDict = headersDynamic
	#print(len(cityCoords)/2/21)

	
	latitude = cityCoords[tid*2]
	longitude =  cityCoords[(tid*2) + 1]

	#print(latitude,',',longitude)
	conn.request('GET', '/v2/boards?latitude='+str(latitude)+'&longitude='+str(longitude)+'','',tempDict)
	#print('came here at least')
	#current_milli_time = int(round(time.time() * 1000)) - current_milli_time
	response = conn.getresponse()

	#print('came here at least')
	#print(response.status, response.reason,response.headers)
	content_raw = ''
	content_raw = response.read()


	if response.status == 200:
		if len(content_raw) == 58:
			#print(content_raw)
			reqContent[tid] = (content_raw)
		#	print(tid, len(content_raw))
		
		try:
			content = gzip.GzipFile(fileobj=BytesIO(content_raw)).read().decode('utf-8')
			reqContent[tid] = (content)
			#print(tid, len(content))
		except Exception as e:
			reqContent[tid] = (content_raw.decode())
			#print(tid, 'Exception', e)

		milis = int(round(time.time() * 1000))
		reqContent[tid] = str(latitude)+','+str(longitude)+'--'+str(milis)+'--'+reqContent[tid] 


		zCompressed = zlib.compress(reqContent[tid].encode())
		nowf2 = datetime.datetime.now()
		filenm = dpath+"Lisbon/P-"+str(tid)+"-responseEncoded-"+nowf2.strftime("%Y-%m-%d")+".txt"
		logFile = open(filenm, "ab")
		toBeWrittenData = ""
		logFile.write(zCompressed)
		logFile.write(b'0x0A')
		logFile.close()
	else:
		#print(tid, content_raw)
		print(response.status)
	conn.close()
	


if __name__ == "__main__":
	
	fillHeaders()
	CityCoordinates()
	numberOfThreads = int(len(cityCoords)/2)
#	for i in range(int(len(cityCoords)/2)):
#		print(2*i,(2*i)+1)
		#i+=1
	
	print('MY THREADS :',numberOfThreads)


	ietc = 0
	nowf3 = datetime.datetime.now()
#	while  1:
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
			time.sleep(0.0001)

		for i in range(numberOfThreads):
			procs[i].join()

		bikeNotFound = 0
		for i in range(numberOfThreads):
			if len(reqContent[i]) == 58:
				bikeNotFound +=1

	print('0 board calls:', bikeNotFound)
	current_milli_timeLife2 = int(round(time.time() * 1000)) - current_milli_timeLife2
	# print(d)
	doneHOst = 0
	i =0
	print('Done ', int(len(cityCoords)/2),' reqs in ', current_milli_timeLife2/1000)
	print(ietc,'Starterd at:',nowf3.strftime('%I:%M %p'),': Wind Lisbon')
	ietc +=1