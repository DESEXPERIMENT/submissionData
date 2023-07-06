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
leftCol = [38.934187, -77.119395 ,38.857503, -77.022578]
rightCol = [38.995775, -77.041174 , 38.912384, -76.934187]

leftCols = []
rightCols = []

full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'



spinToken = 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyVW5pcXVlS2V5IjoiMmE2ZGYyNzRmODRhNWFlODJjMWZhM2M3MGY5MmFlNTYiLCJyZWZlcnJhbENvZGUiOiJIMUhBU1NBTiIsImlzQXBwbGVQYXlEZWZhdWx0IjpmYWxzZSwiaXNBZG1pbiI6ZmFsc2UsImlzQ2hhcmdlciI6ZmFsc2UsImlzQ29ycG9yYXRlIjpmYWxzZSwiYXV0b1JlbG9hZCI6ZmFsc2UsImNyZWRpdEJhbGFuY2UiOjAsInRvdGFsVHJpcENvdW50IjowLCJzcGluVW5saW1pdGVkIjpmYWxzZSwic3BpblVubGltaXRlZE5leHRCaWxsaW5nQ3ljbGUiOm51bGwsInNwaW5VbmxpbWl0ZWRNZW1iZXJzaGlwIjpudWxsLCJpc1F1YWxpZmllZEZvclJpZGUiOmZhbHNlLCJyYXRlRGlzY291bnRQZXJjZW50YWdlIjowLCJ0eXBlIjoiZW1haWwiLCJuYW1lIjoiaDEuaGFzc2FuYWxpa2hhbkBnbWFpbC5jb20iLCJleHAiOjE1NjA4NTUwODZ9.0gkY-886atNUgTq8aYXaOmaftBEjIAlXQpYH_pGyG3s'
def CityCoordinates():
	global cityCoords
	global leftCol
	global rightCol
	global rightCols
	global leftCols


	numberOfThreadsInRow = 10
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

	numberOfThreadsInRow = 10
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


	maxRows = 20
	currRow = 1
	for k in range (0,int(len(rightCols)/2)):

		numberOfThreadsInRow = 10
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

	
	file = open(dpath+"SpinHeaders.txt", "r") 
	i =0
	for line in file: 
		line = line.replace('\n','')
		tempVals = line.split(': ')
		headersDynamic[tempVals[0]] = tempVals[1]
		listHeaders = listHeaders + line;
		i = 1+i


def worker(tid, reqContent,d):
	global cityCoords
	global spinToken
	#global headersDynamic
	conn = http.client.HTTPSConnection('web.spin.pm', 443)
	tempDict = headersDynamic
	#print(len(cityCoords)/2/21)

	
	latitude = cityCoords[tid*2]
	longitude =  cityCoords[(tid*2) + 1]

	tempDict['authorization'] = spinToken

	milis = int(round(time.time() * 1000))
	#print(latitude,',',longitude)
	conn.request('GET', '/api/v3/vehicles?lng='+str(longitude)+'&lat='+str(latitude)+'&distance=1&mode=undefined','',tempDict)
	#print('came here at least')
	#current_milli_time = int(round(time.time() * 1000)) - current_milli_time
	response = conn.getresponse()

	#print('came here at least')
	#print(response.status, response.reason,response.headers)
	content_raw = ''
	content_raw = response.read()


	if response.status == 200:
		try:
			#print(tid,len(content_raw))
			content = gzip.GzipFile(fileobj=BytesIO(content_raw)).read().decode('utf-8')
			content = str(milis)+'--'+ content
			#print(tid,(content))
			reqContent[tid] = (content)
			#write the response 
			zCompressed = zlib.compress(content.encode());
			nowf2 = datetime.datetime.now()
			filenm = dpath +'DC'+"/P-"+str(tid)+"-responseEncoded-"+nowf2.strftime("%Y-%m-%d")+".txt"
			logFile = open(filenm, "ab")
			toBeWrittenData = ""
			logFile.write(zCompressed)
			logFile.write(b'0x0A')
			logFile.close()
		#	print(tid, len(content))
		except Exception as e:
			reqContent[tid] = (content_raw)
			content = content_raw.decode()
			content = str(milis)+'--'+ content
			zCompressed = zlib.compress(content.encode());
			nowf2 = datetime.datetime.now()
			filenm = dpath +'DC'+"/P-"+str(tid)+"-responseEncoded-"+nowf2.strftime("%Y-%m-%d")+".txt"
			logFile = open(filenm, "ab")
			toBeWrittenData = ""
			logFile.write(zCompressed)
			logFile.write(b'0x0A')
			logFile.close()
			#print(tid, 'Exception', e)
	else:
		if(response.status != 403):
			print(tid, content_raw)
			print(response.status)
	d[tid] = response.status
	conn.close()
	
def getToken():
	global spinToken
	conn = http.client.HTTPSConnection('web.spin.pm', 443)
	listHeaders = ''
	headersDynamic = {}
	file = open(dpath+"AuthHeaders.txt", "r") 
	i =0
	for line in file: 
		line = line.replace('\n','')
		tempVals = line.split(': ')
		headersDynamic[tempVals[0]] = tempVals[1]
		listHeaders = listHeaders + line;
		i = 1+i

	# Fill in the entries one by one
	current_milli_time = int(round(time.time() * 1000))
	conn.request('POST', '/api/v1/auth_tokens','{"email":{"email":"h1.hassanalikhan@gmail.com","password":"baboon123"},"isApplePayDefault":false,"grantType":"email"}',headersDynamic)

	#print('came here at least')

	response = conn.getresponse()

	content_raw = ''
	content_raw = response.read()
	content = gzip.GzipFile(fileobj=BytesIO(content_raw)).read().decode('utf-8')

	jsonContent = json.loads(content)
	#print(jsonContent['jwt'])
	spinToken = 'Bearer '+jsonContent['jwt']

	#print(spinToken)

def mainProc():

	global spinToken
	global numberOfThreads
	global cityCoords

	getToken()
	fillHeaders()
	
	CityCoordinates()
	numberOfThreads = int(len(cityCoords)/2)
#	for i in range(int(len(cityCoords)/2)):
#		print(2*i,(2*i)+1)
		#i+=1
	
	#print('MY THREADS :',numberOfThreads)

	ietc = 0
	nowf3 = datetime.datetime.now()
	while 1:
		with Manager() as manager:
			d = manager.dict()
			#set 1
			procs = []
			reqContent = manager.dict()
			for i in range(numberOfThreads):
				#print(i)
				p = Process(target=worker, args=(i,reqContent,d,))
				procs.append(p)
			current_milli_timeLife2 = int(round(time.time() * 1000))
			for i in range(numberOfThreads):
				procs[i].start()
				time.sleep(0.0001)

			for i in range(numberOfThreads):
				procs[i].join()
			current_milli_timeLife2 = int(round(time.time() * 1000)) - current_milli_timeLife2
			# print(d)
			doneHOst = 0
			i =0
			#print('Done '+str(len(cityCoords)/2)+' reqs in ', current_milli_timeLife2/1000)	
			print(ietc,'(started at '+nowf3.strftime('%I:%M %p')+'): Spin - DC')
			ietc +=1
			if(ietc % 20 == 0):
				getToken()
			outofrgn = 0
			#for x in range(len(d)):
			#	if(d[x] != 200):
			#		outofrgn += 1
			#print('Out of rgn', outofrgn, int(len(cityCoords)/2))
			time.sleep(45)
	

import signal, psutil
def kill_child_processes(parent_pid, sig=signal.SIGTERM):
    try:
      parent = psutil.Process(parent_pid)
    except psutil.NoSuchProcess:
      return
    children = parent.children(recursive=True)
    for process in children:
      process.send_signal(sig)


testFile = 'doneTests.txt'


if __name__ == "__main__":
	filetest = open(dpath+testFile,'w')
	filetest.write('open')
	filetest.close()
	while 1:
		mainproc = Process(target=mainProc, args=())
		mainproc.start()
		time.sleep(0.01)
		time.sleep(6000)
		#print('Killer woke up')
		line = ''
		filetest = open(dpath+testFile,'w')
		filetest.write('ready')
		filetest.close()
		time.sleep(0.1)
		
		waitTime = 0
		while line != 'close':
			time.sleep(1)
			waitTime += 1
			if waitTime >=300:
				break;
			#print('Looking for close')
			filetest = open(dpath+testFile,'r')
			line = filetest.read()
			filetest.close()

		kill_child_processes(os.getpid())
		print("Stopped processes")
		filetest = open(dpath+testFile,'w')
		filetest.write('open')
		filetest.close()
		print('Opening file')
		time.sleep(20)