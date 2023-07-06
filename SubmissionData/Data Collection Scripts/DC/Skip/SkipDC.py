import requests
import json
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

import json

#available only in washington 
authBody = 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjU0OGYzZjk4N2IxNzMxOWZlZDhjZDc2ODNmNTIyNWEyOTY0YzY5OWQiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiaGFzc2FuIGFsaSBraGFuIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hLS9BQXVFN21DWVlhMGdpenhUMktoaVprZmx4eE5KNHhyV3dPTWY0eVpyd00tRENRIiwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL3dheWJvdHMtcHJvZHVjdGlvbiIsImF1ZCI6IndheWJvdHMtcHJvZHVjdGlvbiIsImF1dGhfdGltZSI6MTU2MDcxOTE3MSwidXNlcl9pZCI6IjB5Qmw1bDVHQW5OYUhxbXRYWUgyd3BMUGhMcjIiLCJzdWIiOiIweUJsNWw1R0FuTmFIcW10WFlIMndwTFBoTHIyIiwiaWF0IjoxNTYwNzE5MTc1LCJleHAiOjE1NjA3MjI3NzUsImVtYWlsIjoiaC5oYXNzYW5hbGlraGFuQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJoLmhhc3NhbmFsaWtoYW5AZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.YQgS8sV-J31JPH0tb1HzaSIYlQFrongFYJd8pUGn_BYUxnsR6XivWVlTpK-7WNTkeVUASbiwdozLT0S6zm8rL2SEdXVo0PY3JynGNlbqd1m_-qYtr0eQk9ndS5HFftJV4D8j0APzqRESQP0K_6KBlCsbDHdB-KMIv-hYOmLZ7x9hHvk0vNT1P6eW407EwvlYT6pD919smTXK2Ubb3xZSx0wT_A9XGuLo6Z_RiF10Bx-3OnT2BpCOibZ2BWgVQ-2fWc6Y45XTAU7WE7cKFyCfDTKBgn6kuSazg4XemPNKYPFrgvh-qDpzXRHBIooqIdhr0WWl8yVD52V2P3hDv5l1fw'
full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'



def mainProc():
	global testFile
	global dpath
	global authBody
	nowf3 = datetime.datetime.now()
	ietc = 0
	conn = http.client.HTTPSConnection('us-central1-waybots-production.cloudfunctions.net', 443)
	listHeaders = ''

	headersDynamic = {}
	file = open(dpath+"SkipHeaders.txt", "r") 
	i =0
	for line in file: 
		line = line.replace('\n','')
		tempVals = line.split(': ')
		headersDynamic[tempVals[0]] = tempVals[1]
		listHeaders = listHeaders + line;
		i = 1+i
	headersDynamic['authorization'] =  authBody

	while 1:
		# Fill in the entries one by one
		current_milli_time = int(round(time.time() * 1000))
		
		conn.request('POST', '/pinsApi-getPinsForRider','{"lat":38.908050537109375,"lon":-77.03137969970703,"pins":{},"radiusMeters":100000}',headersDynamic)
		response = conn.getresponse()
		current_milli_time = int(round(time.time() * 1000)) - current_milli_time
		#print('came here at least')
		#print(current_milli_time, response.status)
		milis = int(round(time.time() * 1000))

		content_raw = ''
		content_raw = response.read()
		response_headers = response.info()

		nowf2 = datetime.datetime.now()
		
		if response.status == 200:
			content = gzip.GzipFile(fileobj=BytesIO(content_raw)).read().decode('utf-8')
			content = str(milis)+'--'+ content
			print(ietc,'(started at '+nowf3.strftime('%I:%M %p')+'): Skip- Response Length (gzip compressed): ',len(content))
			#write the response 
			zCompressed = zlib.compress(content.encode());
			nowf2 = datetime.datetime.now()
			filenm = dpath +'DC'+"/P-"+str(0)+"-responseEncoded-"+nowf2.strftime("%Y-%m-%d")+".txt"
			logFile = open(filenm, "ab")
			toBeWrittenData = ""
			logFile.write(zCompressed)
			logFile.write(b'0x0A')
			logFile.close()
		else:
			print(content_raw)
			print(response.status)
		#print(len(content) , 'KBs')
		ietc +=1
		filetest = open(dpath+testFile,'r')
		line3 = filetest.read()
		filetest.close()
		if line3 == 'ready':
			filetest = open(dpath+testFile,'w')
			filetest.write('close')
			filetest.close()
			print('Closing file')
			time.sleep(1000)
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