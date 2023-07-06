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



full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'


ietc = 0
if __name__ == "__main__":
	nowf3 = datetime.datetime.now()
	listHeaders = ''

	headersDynamic = {}
	file = open(dpath+"TierHeaders.txt", "r") 
	i =0
	for line in file: 
		line = line.replace('\n','')
		tempVals = line.split(': ')
		headersDynamic[tempVals[0]] = tempVals[1]
		listHeaders = listHeaders + line;
		i = 1+i
	ietc = 0
	while  1:

		conn = http.client.HTTPSConnection('platform.tier-services.io', 443)
		#print(conn)

		#conn.putrequest('GET', '/')
		#conn.endheaders() # <---


		# Fill in the entries one by one
		current_milli_time = int(round(time.time() * 1000))
		conn.request('GET', '/vehicle?lat=40.416618&lng=-3.703787&radius=400000','',headersDynamic)

		#print('came here at least')

		response = conn.getresponse()
		current_milli_time = int(round(time.time() * 1000)) - current_milli_time
		#print('came here at least')
		
		#print(current_milli_time, response.status)

		content_raw = ''
		content_raw = response.read()
		response_headers = response.info()
		if 'Content-Encoding' in response_headers.keys():
			content = gzip.GzipFile(fileobj=BytesIO(content_raw)).read().decode('utf-8')
			print(len(content))
			#print('- Response Time: ',response_headers)

			nowf2 = datetime.datetime.now()
			filenm = dpath +"Madrid/Data-responseEncoded-"+nowf2.strftime("%Y-%m-%d")+".txt"


			#print('- Response Length (gzip compressed): ',len(content_raw))
			#content = gzip.GzipFile(fileobj=BytesIO(content_raw)).read().decode('utf-8')
			#print(len(content_raw)/1000 , 'KBs')
			milis = int(round(time.time() * 1000))
			content = str(milis)+'--'+str(content)
			zCompressed = zlib.compress(content.encode())
			logFile = open(filenm, "ab")
			toBeWrittenData = ""
			logFile.write(zCompressed)
			logFile.write(b'0x0A')
			logFile.close()

			print('Done writing - compressed', len(zCompressed)/1000, 'KBs')

			print(ietc,'Starters at:',nowf3.strftime('%I:%M %p'),': Tier Madrid')
			ietc +=1
			if(ietc > 100):
				ietc = 0
				print('longer sleep')
				time.sleep(100)
		else:
			print('No bikes found')
		time.sleep(29)