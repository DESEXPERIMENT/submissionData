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


authBody = '{"authenticationToken":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjgzMDc3MzgsImp0aSI6IjAiLCJpYXQiOjE1NjA1MzE3MzgsImlzcyI6ImF1dGguYXBpLnZvaWFwcC5pbyIsIm5iZiI6MTU2MDUzMTczNywidXNlcklkIjoiNjAyNDAwYjktYmUyYy00MGM2LTkzMDgtM2ZmODU1MjI2OGRkIiwiVXNlcklEIjoiNjAyNDAwYjktYmUyYy00MGM2LTkzMDgtM2ZmODU1MjI2OGRkIiwiVmVyaWZpZWQiOmZhbHNlLCJ2ZXJpZmllZCI6ZmFsc2V9.X4RZ32vC5htYtmv_qY1lqw0njbzxr8WQKupEVQ3ap4DZjaXiU9scQj2duFW3wKl-BhXCJeYDKDIIBef7Io0gSg"}'

full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'




ietc = 0
if __name__ == "__main__":

	conn = http.client.HTTPSConnection('api.voiapp.io', 443)
	#print(conn)

	#conn.putrequest('GET', '/')
	#conn.endheaders() # <---
	listHeaders = ''



	headersDynamic = {}


	######################### Get Token ##############

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
	conn.request('POST', '/v1/auth/session/',authBody,headersDynamic)

	#print('came here at least')

	response = conn.getresponse()

	content_raw = ''
	content_raw = response.read()
	content = gzip.GzipFile(fileobj=BytesIO(content_raw)).read().decode('utf-8')
	#content = str(milis)+'--'+content
	jsonContent = json.loads(content)
	#print(jsonContent['authenticationToken'])





	##################### Got Token ##################
	file = open(dpath+"VoiHeaders.txt", "r") 
	i =0
	for line in file: 
		line = line.replace('\n','')
		tempVals = line.split(': ')
		headersDynamic[tempVals[0]] = tempVals[1]
		listHeaders = listHeaders + line;
		i = 1+i



	nowf3 = datetime.datetime.now()
	while  1:

		milis = int(round(time.time() * 1000))
		#######################   LISBON Zone 6 #########################

		# Fill in the entries one by one
		current_milli_time = int(round(time.time() * 1000))
		headersDynamic['x-access-token'] = jsonContent['authenticationToken']
		conn.request('GET', '/v1/vehicles/zone/6/ready','',headersDynamic)

		#print('came here at least')

		response = conn.getresponse()
		current_milli_time = int(round(time.time() * 1000)) - current_milli_time
		#print('came here at least')
		print(current_milli_time, response.status)

		content_raw = ''
		content_raw = response.read()
		response_headers = response.info()
		#print(content_raw)
		#print('- Response Time: ',response_headers)

		nowf2 = datetime.datetime.now()
		
		content = gzip.GzipFile(fileobj=BytesIO(content_raw)).read().decode('utf-8')
		content = str(milis)+'--'+content
		zCompressed = zlib.compress(str(content).encode())

		print('Done writing LISBON - compressed', len(zCompressed)/1024, 'KBs')

		zCompressed = zlib.compress(content_raw)
		nowf2 = datetime.datetime.now()
		filenm = dpath+"Lisbon/P-"+str(0)+"-Lisbon-responseEncoded-"+nowf2.strftime("%Y-%m-%d")+".txt"
		logFile = open(filenm, "ab")
		toBeWrittenData = ""
		logFile.write(zCompressed)
		logFile.write(b'0x0A')
		logFile.close()
		i = 1
		




		time.sleep(10)
		milis = int(round(time.time() * 1000))
		############################## MADRID Zone 2#####################################

		current_milli_time = int(round(time.time() * 1000))
		headersDynamic['x-access-token'] = jsonContent['authenticationToken']
		conn.request('GET', '/v1/vehicles/zone/2/ready','',headersDynamic)

		#print('came here at least')

		response = conn.getresponse()
		current_milli_time = int(round(time.time() * 1000)) - current_milli_time
		#print('came here at least')
		print(current_milli_time, response.status)

		content_raw = ''
		content_raw = response.read()
		response_headers = response.info()
		#print(content_raw)
		#print('- Response Time: ',response_headers)

		nowf2 = datetime.datetime.now()
		
		content = gzip.GzipFile(fileobj=BytesIO(content_raw)).read().decode('utf-8')
		content = str(milis)+'--'+content
		zCompressed = zlib.compress(str(content).encode())

		print('Done writing MADRID - compressed', len(zCompressed)/1024, 'KBs')

		zCompressed = zlib.compress(content_raw)
		nowf2 = datetime.datetime.now()
		filenm = dpath+"Lisbon/P-"+str(0)+"-Madrid-responseEncoded-"+nowf2.strftime("%Y-%m-%d")+".txt"
		logFile = open(filenm, "ab")
		toBeWrittenData = ""
		logFile.write(zCompressed)
		logFile.write(b'0x0A')
		logFile.close()
		i = 1
		time.sleep(10)
		milis = int(round(time.time() * 1000))
		########################## Paris Zone 9 #############################################

		current_milli_time = int(round(time.time() * 1000))
		headersDynamic['x-access-token'] = jsonContent['authenticationToken']
		conn.request('GET', '/v1/vehicles/zone/9/ready','',headersDynamic)

		#print('came here at least')

		response = conn.getresponse()
		current_milli_time = int(round(time.time() * 1000)) - current_milli_time
		#print('came here at least')
		print(current_milli_time, response.status)

		content_raw = ''
		content_raw = response.read()
		response_headers = response.info()
		#print(content_raw)
		#print('- Response Time: ',response_headers)

		nowf2 = datetime.datetime.now()
		
		content = gzip.GzipFile(fileobj=BytesIO(content_raw)).read().decode('utf-8')
		content = str(milis)+'--'+content
		zCompressed = zlib.compress(str(content).encode())

		print('Done writing PARIS- compressed', len(zCompressed)/1024, 'KBs')

		zCompressed = zlib.compress(content_raw)
		nowf2 = datetime.datetime.now()
		filenm = dpath+"Lisbon/P-"+str(0)+"-Paris-responseEncoded-"+nowf2.strftime("%Y-%m-%d")+".txt"
		logFile = open(filenm, "ab")
		toBeWrittenData = ""
		logFile.write(zCompressed)
		logFile.write(b'0x0A')
		logFile.close()
		i = 1


		print(ietc,'Starters at:',nowf3.strftime('%I:%M %p'),': Voi Lisbon, Madrid, Paris')
		ietc +=1
		if(ietc > 100):
			ietc = 0
			print('longer sleep')
			time.sleep(100)
		time.sleep(10)