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

myCitiesList = [           'Brussels',         'Berlin',             'Chicago',                 'DC',               'Detroit',            'Lisbon',             'Paris',              'SanFrancisco']
myCityCoordinates = [50.847140, 4.352107, 52.519362, 13.405874, 41.875854, -87.636110, 38.913201, -77.011789, 42.374334, -83.077858, 38.722195, -9.139227, 48.864884, 2.340593 , 37.753861, -122.442754 ]
myCityRadii = [100,100,100, 100, 100, 500, 100,100 ]
myJumpTokens = ['249ca2c37d2ba293c0a1c0bd71734db9','16d1f3db8515a1023335f7f5f6e35c4e','8da2b72d208c703988bdac52ad4c165c','f3e9079914227d17c7e734394448a45d','3fa93752734f4911656efb886458122c','766551ce1fc5ee19b729fce096921b3e','93b8f51d34d6cd9b0b30f7192b5a457a','b28a92fb794f63cc1feafdf465479439']
headersDynamic= []

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
	file = open(dpath +"JumpHeaders.txt", "r")
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

	headersDynamicThread['x-uber-token'] = myJumpTokens[tid]
	headersDynamic[tid] = headersDynamicThread


def worker(tid, dataArrayLock, d, reqContent, pLat, pLong, City, ietNumber):
	#print(tid, City, pLat, pLong)

	reqHost = 'cn-dca1.cfe.uber.com'
	x = None
	conn = http.client.HTTPSConnection(reqHost, 443)

	tempDict = headersDynamic[tid]
	latitude = pLat
	longitude =  pLong


	current_milli_time = int(round(time.time() * 1000))

	#new should be added everywhere 
	milis = int(round(time.time() * 1000))


	conn.request('GET', '/rt/hourly-rentals/search-assets?radius=500&vehicleType=BIKE&vehicleTypes=BIKE&vehicleTypes=SCOOTER&longitude='+str(pLong)+'&latitude='+str(pLat),'',tempDict)
	#print('came here at least')
	current_milli_time = int(round(time.time() * 1000)) - current_milli_time
	response = conn.getresponse()

	#print('came here at least')
	#print(response.status, response.reason,response.headers)
	content_raw = ''
	content_raw = response.read()


	if response.status == 200:
		content = gzip.GzipFile(fileobj=BytesIO(content_raw)).read().decode('utf-8')
		print(ietNumber,'-', City,latitude,longitude,'- Length:', len(content))

		#new should be added everywhere 
		content = City+'--'+str(latitude)+','+str(longitude)+'--'+str(milis)+'--'+content

		reqContent[tid] = (content)
		#if(tid == 0):
		#	file = open('Data.txt', "w")
		#	file.write(content)
		#	file.close()

		d[tid] = 200
		readResponseUber(tid,content)
		jkk = 10
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
	filenm = dpath +myCitiesList[tid]+"/P-"+str(tid)+"-responseEncoded-"+nowf2.strftime("%Y-%m-%d")+".txt"
	logFile = open(filenm, "ab")
	toBeWrittenData = ""
	logFile.write(zCompressed)
	logFile.write(b'0x0A')
	logFile.close()
	i = 1
	#file1.close()'''


numberOfThreadsInRow = 3
hostId = 0

maxSleep = 5
statusThreads = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]





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
	numberOfThreads = 1

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

	time.sleep(1.5)
	while 1:
		procs = []

		with Manager() as manager:

			# reqHost = reqHosts[ietNumber % numberOfHosts]
			d = manager.dict()
			reqContent = manager.dict()
			for i in range(numberOfThreads):
				p = Process(target=worker, args=(2,dataArrayLock,d,reqContent,myCityCoordinates[2*2],myCityCoordinates[(2*2) + 1], myCitiesList[2], ietNumber))
				procs.append(p)
			current_milli_timeLife2 = int(round(time.time() * 1000))
			for i in range(numberOfThreads):
				procs[i].start()
				time.sleep(0.01)

			for i in range(numberOfThreads):
				procs[i].join()
						
			#print(reqContent)	
			print(ietNumber,"-Started at:",nowf.strftime('%I:%M %p'),"-In Time M:", int(((int(round(time.time() * 1000)) - current_milli_timeLife)/1000)/60),"-S:", int(((int(round(time.time() * 1000)) - current_milli_timeLife)/1000)%60))	
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
			time.sleep(38)

			

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