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


lyftToken = ''
authBody = '{"authenticationToken":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjgzMDc3MzgsImp0aSI6IjAiLCJpYXQiOjE1NjA1MzE3MzgsImlzcyI6ImF1dGguYXBpLnZvaWFwcC5pbyIsIm5iZiI6MTU2MDUzMTczNywidXNlcklkIjoiNjAyNDAwYjktYmUyYy00MGM2LTkzMDgtM2ZmODU1MjI2OGRkIiwiVXNlcklEIjoiNjAyNDAwYjktYmUyYy00MGM2LTkzMDgtM2ZmODU1MjI2OGRkIiwiVmVyaWZpZWQiOmZhbHNlLCJ2ZXJpZmllZCI6ZmFsc2V9.X4RZ32vC5htYtmv_qY1lqw0njbzxr8WQKupEVQ3ap4DZjaXiU9scQj2duFW3wKl-BhXCJeYDKDIIBef7Io0gSg"}'

full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'



def mainProc():
	global lyftToken
	global authBody
	global dpath
	global testFile



	ietc = 0
	nowf3 = datetime.datetime.now()
	while 1:
			
		if ietc%10 == 0 or ietc == 0:
			
			print('Getting token\n\n')
			conn = http.client.HTTPSConnection('api.lyft.com', 443)
			listHeaders = ''
			headersDynamic = {}
			listHeaders = ''
			file = open(dpath+'AuthHeaders.txt', "r") 
			i =0
			for line in file: 
				line = line.replace('\n','')
				tempVals = line.split(': ')
				headersDynamic[tempVals[0]] = tempVals[1]
				listHeaders = listHeaders + line;
				i = 1+i
			# Fill in the entries one by one
			current_milli_time = int(round(time.time() * 1000))


			authBody = 'grant_type=refresh_token&refresh_token=BKi75KFVH7pUo1wQHKsxpqHiqy5Lb%2BmHRxEkq6k77AZ0PfyjXn6OcgRLYA8ClJQ1peZcfgKCCL%2Fufms3pY6FNiduJREqv7W6wgXgPt3R4d6j'


			#print(headersDynamic)
			conn.request('POST', '/oauth2/access_token',authBody,headersDynamic)

			#print('came here at least')

			response = conn.getresponse()

			content_raw = ''
			content_raw = response.read()
			if response.status == 200:
					#print(content_raw)
					content = gzip.GzipFile(fileobj=BytesIO(content_raw)).read().decode('utf-8')
					dict1 = parsed_json = json.loads(content)
					lyftToken = 'Bearer '+dict1["access_token"]
					#print(lyftToken)
			else:
				print(response.status)
			#jsonContent = json.loads(content)
			#print((jsonContent.keys()))




		headersDynamic = {}
			##################### Got Token - Washington ##################



		file = open(dpath+"reqHeader.txt", "r") 
		i =0
		for line in file: 
			line = line.replace('\n','')
			tempVals = line.split(': ')
			headersDynamic[tempVals[0]] = tempVals[1]
			listHeaders = listHeaders + line;
			i = 1+i


		file.close()
		# Fill in the entries one by one
		current_milli_time = int(round(time.time() * 1000))
		headersDynamic['authorization'] = lyftToken


		conn = http.client.HTTPSConnection('api.lyft.com', 443)

		milis = int(round(time.time() * 1000))
		conn.request('GET', '/v1/last-mile/nearby-rideables?origin_lat=41.877726&origin_lng=-87.63009304&radius_km=220.260264520463144&result_types=rideables&result_types=stations','',headersDynamic)

		#print('came here at least')

		response = conn.getresponse()
		current_milli_time = int(round(time.time() * 1000)) - current_milli_time
		#print('came here at least')
		#print(current_milli_time, response.status)

		content_raw = ''
		content_raw = response.read()
		response_headers = response.info()
		#print(content_raw)
		#print('- Response Time: ',response_headers)
		if response.status == 200:
			content = gzip.GzipFile(fileobj=BytesIO(content_raw)).read().decode('utf-8')
			content = str(milis)+'--'+content

			print(ietc,'(started at '+nowf3.strftime('%I:%M %p')+'): Lyft- Chicago - Response Length (gzip compressed): ',len(content))
			#write the response 
			zCompressed = zlib.compress(content.encode());
			nowf2 = datetime.datetime.now()
			filenm = dpath +'Chicago'+"/P-"+str(0)+"-responseEncoded-"+nowf2.strftime("%Y-%m-%d")+".txt"
			logFile = open(filenm, "ab")
			toBeWrittenData = ""
			logFile.write(zCompressed)
			logFile.write(b'0x0A')
			logFile.close()
		else:
			print(0, content_raw)
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