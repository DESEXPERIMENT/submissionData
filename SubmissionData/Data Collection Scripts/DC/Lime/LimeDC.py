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


washingtonZones = [38.920405]

cityCoords = []
leftCol = [38.917595, -77.068120 ,38.871129, -77.057126]
rightCol = [38.927256, -76.971184,38.876399, -76.977088]

leftCols = []
rightCols = []


numberOfCoordsInRow = 5
numberOfRows = 5


class citySquare:
    upperRight_ne_x = 0.0
    upperRight_ne_y = 0.0
    loweRLeft_sw_x = 0.0
    loweRLeft_sw_y = 0.0
    
def CityCoordinates():
	global cityCoords
	global leftCol
	global rightCol
	global rightCols
	global leftCols


	#dividing left col in multiple rows 
	numberOfThreadsInRow = numberOfRows
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

	#dividing right col in multiple rows 
	numberOfThreadsInRow = numberOfRows
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


	#dividing each row in multiple coords 

	maxRows = 41
	currRow = 1
	ind1 = 0
	file = open(dpath+'coors.txt','w')
	for k in range (0,int(len(rightCols)/2)):

		numberOfThreadsInRow = numberOfCoordsInRow
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
			#if currRow < 3:
			#print('Row ',currRow,'[',ind1,']:  ',cindex, '-', str3, ",", str4, "-", cindex)
			file.write('Row '+str(currRow)+'['+str(ind1)+']:  '+str(cindex)+ '-'+str(str3)+ ","+str(str4)+ "-"+ str(cindex)+'\n')
			cityCoords.append(float(str3))
			cityCoords.append(float(str4))
			ind1 +=1
			
			i = i + (1/(numberOfThreadsInRow))
		currRow +=1
	file.close()
	print('Done finding coords')




citySquares = []
def findSquares():
	global cityCoords
	global citySquares
	i = 0
	j = 0
	
	file = open(dpath+'squares.txt','w')
	while i < numberOfRows:
		j = (i*(numberOfCoordsInRow+1)*2)
		jCheck = j
		firstCheck = 1
		sqCount = 0
		while j < jCheck+((numberOfCoordsInRow+1)*2):
		#if(i< 2):
		#	print('Row',i,': Index',(j-(i*(numberOfCoordsInRow+1)*2))/2,':',cityCoords[j])
			if firstCheck !=1:
				s = citySquare()
				s.upperRight_ne_x = cityCoords[j]
				s.upperRight_ne_y = cityCoords[j+1]
				s.loweRLeft_sw_x = cityCoords[j+((numberOfCoordsInRow)*2)]
				s.loweRLeft_sw_y = cityCoords[j+((numberOfCoordsInRow)*2)+1]

				file.write(str(i)+"="+ str(sqCount)+str(s.__dict__)+'\n')
				citySquares.append(s)
				sqCount +=1
			else:
				firstCheck = 0
			j+=2
			

		i+=1
	file.close()





headersDynamic= {}

serverNumber = 0;
tid1= None
procs=[]
#40 threads for toronto
numberOfThreads = 20
numberOfHeaders = 6
reqHost = "cn-phx2.uber.com"

reqHosts = ["cn-phx2.uber.com","cn-dca1.uber.com"]

authCodes = ['Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX3Rva2VuIjoiNkM3TUhCUEJES0xEMyIsImxvZ2luX2NvdW50IjoxfQ.eYksM5f2w9wblSsBdTk7zzH6EtEcwVDGKkC1_4-6YsM']
def fillHeaders(tid):
	# Fill in the entries one by one
	global headersDynamic
	

	listHeaders = ''
	file = open(dpath+"LimeHeaders.txt", "r") 
	i =0
	for line in file: 
		line = line.replace('\n','')
		tempVals = line.split(': ')
		headersDynamic[tempVals[0]] = tempVals[1]
		listHeaders = listHeaders + line;
		i = 1+i


def worker(tid, dataArrayLock, d, reqContent, authCode):
	#print(tid, City, pLat, pLong)

	global headersDynamic
	global citySquares



	reqHost = 'web-production.lime.bike'
	x = None
	conn = http.client.HTTPSConnection(reqHost, 443)

	tempDict = headersDynamic
	tempDict['Authorization']= authCode

	current_milli_time = int(round(time.time() * 1000))

	#new should be added everywhere 
	milis = int(round(time.time() * 1000))


	conn.request('GET', '/api/rider/v1/views/map?ne_lat='+str(citySquares[tid].upperRight_ne_x)+'&ne_lng='+str(citySquares[tid].upperRight_ne_y)+'&sw_lat='+str(citySquares[tid].loweRLeft_sw_x)+'&sw_lng='+str(citySquares[tid].loweRLeft_sw_y)+'&user_latitude='+str(citySquares[tid].upperRight_ne_x)+'&zoom=15&user_longitude='+str(citySquares[tid].upperRight_ne_y)+'','',tempDict)
	#print('came here at least')
	current_milli_time = int(round(time.time() * 1000)) - current_milli_time
	with dataArrayLock:
		response = conn.getresponse()

	#print('came here at least')
	#print(response.status, response.reason,response.headers)
	content_raw = ''
	content_raw = response.read()


	if response.status == 200:
		content = gzip.GzipFile(fileobj=BytesIO(content_raw)).read().decode('utf-8')
		content = str(milis)+'--'+ content
		readResponseUber(tid,content)
		#print(tid, '-',len(content))
		
	else:
		#if response.status !=307 and response.status!=429:
		content = gzip.GzipFile(fileobj=BytesIO(content_raw)).read().decode('utf-8')
		print(tid, content)

		print(response.status)
		# if(response.status == 307)
		d[tid] = response.status
	
	conn.close()

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
	#print('writing response')
	filenm = dpath +'DC'+"/P-"+str(tid)+"-responseEncoded-"+nowf2.strftime("%Y-%m-%d")+".txt"
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



def mainProc():
	CityCoordinates()
	findSquares()
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

	
	manager = Manager()
	exestring = manager.Value(c_char_p, "")

	#FILL UP THE HEADERS FOR THE REQUESTS 
	
	fillHeaders(0)
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

	ik = 0
	while ik < 24:
		procs = []

		with Manager() as manager:

			# reqHost = reqHosts[ietNumber % numberOfHosts]
			d = manager.dict()
			reqContent = manager.dict()
			tempTCount = 3
			for i in range(tempTCount):
				p = Process(target=worker, args=(ik +i,dataArrayLock,d,reqContent,authCodes[0]))
				procs.append(p)
			current_milli_timeLife2 = int(round(time.time() * 1000))
			for i in range(tempTCount):
				procs[i].start()
			#	time.sleep(1)

			for i in range(tempTCount):
				procs[i].join()
						
			#print(reqContent)	
			print(ietNumber,"- ~~[WASHINGTON DC]~~ Started at:",nowf.strftime('%I:%M %p'),"-In Time M:", int(((int(round(time.time() * 1000)) - current_milli_timeLife)/1000)/60),"-S:", int(((int(round(time.time() * 1000)) - current_milli_timeLife)/1000)%60))	
			ietNumber += 1
			mainCount += 1

			ik += 3
	ik = 10
	filetest = open(dpath+testFile,'r')
	line3 = filetest.read()
	filetest.close()
	print(line3)
	if line3 == 'ready':
		filetest = open(dpath+testFile,'w')
		filetest.write('close')
		filetest.close()
		print('Closing file')
		time.sleep(1000)


import signal, psutil
def kill_child_processes(parent_pid, sig=signal.SIGTERM):
    try:
      parent = psutil.Process(parent_pid)
    except psutil.NoSuchProcess:
      return
    children = parent.children(recursive=True)
    for process in children:
      process.send_signal(sig)


testFile = 'doneTestsDC.txt'


if __name__ == "__main__":
	filetest = open(dpath+testFile,'w')
	filetest.write('ready')
	filetest.close()

	mainproc = Process(target=mainProc, args=())
	mainproc.start()
	
	time.sleep(0.01)
	time.sleep(30)
	#print('Killer woke up')
	#line = ''
	#filetest = open(dpath+testFile,'w')
	#filetest.write('ready')
	#
	time.sleep(0.1)
	line = ''
	waitTime = 0
	while line != 'close':
		time.sleep(1)
		waitTime += 1
		if waitTime >=5:
			break;
		#print('Looking for close')
		filetest = open(dpath+testFile,'r')
		line = filetest.read()
		filetest.close()

	kill_child_processes(os.getpid())
	print("Stopped processes")
	filetest = open(dpath+testFile,'w')
	filetest.write('ready')
	filetest.close()
	
	