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
	while  1:
		conn = http.client.HTTPSConnection('app.scoot.co', 443)


		# Fill in the entries one by one
		current_milli_time = int(round(time.time() * 1000))
		milis = int(round(time.time() * 1000))
		try:
			conn.request('GET', '/api/v1/scooters.json?','',{})

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

			nowf2 = datetime.datetime.now()

			#print('- Response Length (gzip compressed): ',len(content_raw))


			#print(len(content_raw)/1000 , 'KBs')
			#content =  gzip.GzipFile(fileobj=BytesIO(content_raw)).read().decode('utf-8')
			content = str(milis)+'--'+content_raw.decode()
			zCompressed = zlib.compress(str(content).encode())

			print('Done writing - compressed', len(zCompressed)/1000, 'KBs')

			#zCompressed = zlib.compress(content)
			nowf2 = datetime.datetime.now()
			filenm = dpath+"SF/P-"+str(0)+"-responseEncoded-"+nowf2.strftime("%Y-%m-%d")+".txt"
			logFile = open(filenm, "ab")
			toBeWrittenData = ""
			logFile.write(zCompressed)
			logFile.write(b'0x0A')
			logFile.close()
			i = 1
			print(ietc,'Starters at:',nowf3.strftime('%I:%M %p'),': Scoot SF')
			ietc +=1
			if(ietc > 100):
				ietc = 0
				print('longer sleep')
				time.sleep(100)
			time.sleep(35)
		except Exception as e:
			print(e)
			time.sleep(30)