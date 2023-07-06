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

full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'

birdToken =  'Bird eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJBVVRIIiwidXNlcl9pZCI6IjJlMGM1ZTQyLTc1YjItNDkxNi05M2U4LWY5Yjg4MGQ1NTdlOSIsImRldmljZV9pZCI6IjdjMmEzMTVlZjRjNTg4OTIiLCJleHAiOjE1OTIyNDc4NjJ9.DkvUuvjEajZg9365SxjCyoVm1fShGXFiRN-Kkyoalvg'
myCitiesList = [           'Paris',         'Paris',         'Paris', 'Paris', 'Paris']


headersDynamic= []






#Bird Stuff
myCityUrl = [
#DC
'/bird/nearby?latitude=48.86727523803711&longitude=2.3597280979156494&radius=100000.0',
'/bird/nearby?latitude=48.848989&longitude=2.290957&radius=100000.0',
'/bird/nearby?latitude=48.862949&longitude=2.342451&radius=100000.0',
'/bird/nearby?latitude=48.855945&longitude=2.373373&radius=100000.0',
'/bird/nearby?latitude=48.851060&longitude=2.341917&radius=100000.0'
]
myCityLoc = [
#DC
'{"accuracy":1.4115355014801025,"altitude":57.0,"heading":null,"latitude":48.86727523803711,"longitude":2.3597280979156494,"mocked":false,"speed":0.0}',
'{"accuracy":1.226274013519287,"altitude":57.0,"heading":null,"latitude":48.848989,"longitude":2.290957,"mocked":false,"speed":0.0}',
'{"accuracy":1.6441841125488281,"altitude":57.0,"heading":null,"latitude":48.862949,"longitude":2.342451,"mocked":true,"speed":0.0}',
'{"accuracy":1.5051865577697754,"altitude":57.0,"heading":null,"latitude":48.855945,"longitude":2.373373,"mocked":true,"speed":0.0}',
'{"accuracy":1.5797275304794312,"altitude":57.0,"heading":null,"latitude":48.851060,"longitude":2.341917,"mocked":true,"speed":0.0}',
]
serverNumber = 0;
tid1= None
procs=[]
#40 threads for toronto
numberOfThreads = 15
numberOfHeaders = 6
reqHost = "cn-phx2.uber.com"

reqHosts = ["cn-phx2.uber.com","cn-dca1.uber.com"]

def fillHeaders(tid):
	# Fill in the entries one by one
	global headersDynamic
	global myJumpTokens


	headersDynamicThread= {}
	listHeaders = []
	fileNameHeader = int(tid%numberOfHeaders);
	#generalHeader
	file = open(dpath +"BirdHeaders.txt", "r")
	#file = open("mu"+str(fileNameHeader)+".txt", "r")
	i = 0
	for line in file: 
		listHeaders.append(line)
		i = 1+i
	for item in listHeaders:
		item = item.replace("\n","")
		item = item.replace(":","")
		item = item.split()
		#print (item)
		headersDynamicThread[""+item[0]] = item[1]
	file.close()
	headersDynamic[tid] = headersDynamicThread


def worker(tid, dataArrayLock, d, reqContent, City, ietNumber):
	#print(tid, City, pLat, pLong)

	global myCityUrl
	global myCityLoc
	reqHost = 'api.birdapp.com'
	x = None
	conn = http.client.HTTPSConnection(reqHost, 443)

	tempDict = headersDynamic[tid]


	current_milli_time = int(round(time.time() * 1000))

	#new should be added everywhere 
	milis = int(round(time.time() * 1000))

	#print(tempDict)
	tempDict['authorization'] =birdToken
	tempDict['location'] = myCityLoc[tid]
	
	conn.request('GET', myCityUrl[tid],'',tempDict)
	#print('came here at least')
	current_milli_time = int(round(time.time() * 1000)) - current_milli_time
	response = conn.getresponse()

	#print('came here at least')
	#print(response.status, response.reason,response.headers)
	content_raw = ''
	content_raw = response.read()


	if response.status == 200:
		try:
			content = gzip.GzipFile(fileobj=BytesIO(content_raw)).read().decode('utf-8')
			print(ietNumber,'-', City,'- Length:', len(content))
			content = City+'--'+str(milis)+'--'+content
			reqContent[tid] = (content)
			d[tid] = 200
			readResponseUber(tid,content)
			jkk = 10
		except Exception as e:
			#print(e,content_raw)
			print(ietNumber,'-', City,'- Length:', len(content_raw))
			readResponseUber(tid,content_raw.decode())
	else:
		if response.status !=307 and response.status!=429:
			print(tid, content_raw)
			print(response.status)
		# if(response.status == 307)
		d[tid] = response.status
	

def readResponseUber(tid, response):
	global nowf
	global toBeWrittenData
	global logFile
	global myCitiesList
	data= response
	
	toBeWrittenData = data
	#i mb
	#if (len(toBeWrittenData)) > 100000:
	zCompressed = zlib.compress(toBeWrittenData.encode());
	nowf2 = datetime.datetime.now()
	filenm = dpath +'Paris'+"/P-"+str(tid)+"-responseEncoded-"+nowf2.strftime("%Y-%m-%d")+".txt"
	logFile = open(filenm, "ab")
	toBeWrittenData = ""
	logFile.write(zCompressed)
	logFile.write(b'0x0A')
	logFile.close()
	i = 1
	#file1.close()'''


numberOfThreadsInRow = 3
hostId = 0


def mainProc():
	#v = Value('i', 0)
	      #  l = manager.list(range(50))

	global headersDynamic
	global serverNumber
	global tid1
	global procs
	global numberOfThreads
	global numberOfHeaders
	global reqHost
	global reqHosts
	global numberOfThreadsInRow
	global hostId
	global maxSleep
	global statusThreads
	global myCityCoordinates
	global myCitiesList

	#Number of cities 
	numberOfThreads = 5

	manager = Manager()
	exestring = manager.Value(c_char_p, "")

	#FILL UP THE HEADERS FOR THE REQUESTS 
	for k in range(8):
	 	headersDynamic.append({})
	for i in range(8):
		fillHeaders(i)
	#done with the headers 

	# locks of shared array 
	dataArrayLock = Lock()

	nowf = datetime.datetime.now()
	current_milli_timeLife = 0
	#logFileLock = threading.Lock()
	current_milli_timeLife2 = int(round(time.time() * 1000))
	mainCount = 0
	current_milli_timeLife = int(round(time.time() * 1000))
	ietNumber = 0


	while 1:
		procs = []

		with Manager() as manager:

			# reqHost = reqHosts[ietNumber % numberOfHosts]
			d = manager.dict()
			reqContent = manager.dict()
			for i in range(numberOfThreads):
				p = Process(target=worker, args=(i,dataArrayLock,d,reqContent, myCitiesList[i], ietNumber))
				procs.append(p)
			current_milli_timeLife2 = int(round(time.time() * 1000))
			for i in range(numberOfThreads):
				procs[i].start()
				time.sleep(0.1)

			for i in range(numberOfThreads):
				procs[i].join()
						
			#print(reqContent)	
			print(ietNumber," ~~[Paris]~~ - Started at:",nowf.strftime('%I:%M %p'),"-In Time M:", int(((int(round(time.time() * 1000)) - current_milli_timeLife)/1000)/60),"-S:", int(((int(round(time.time() * 1000)) - current_milli_timeLife)/1000)%60))	
			ietNumber += 1
			mainCount += 1

			#close when all reqs are done 
			filetest = open(dpath+testFile,'r')
			line3 = filetest.read()
			filetest.close()
			if line3 == 'ready':
				filetest = open(dpath+testFile,'w')
				filetest.write('close')
				filetest.close()
				print('Closing file')
				time.sleep(1000)
			current_milli_timeLife2 = int(round(time.time() * 1000)) - current_milli_timeLife2
			time.sleep(30)

			

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