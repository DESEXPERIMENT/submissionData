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
	file = open(dpath+"MovoHeaders.txt", "r") 
	i =0
	for line in file: 
		line = line.replace('\n','')
		tempVals = line.split(': ')
		headersDynamic[tempVals[0]] = tempVals[1]
		listHeaders = listHeaders + line;
		i = 1+i


	while  1:
		conn = http.client.HTTPSConnection('s0.movo.me', 443)
		file.close()

		current_milli_time = int(round(time.time() * 1000))
		
		#print(payload)
		milis = int(round(time.time() * 1000))
		r = requests.post('https://s0.movo.me/Movo/scripts/fetch-all-available-vehicles.php', data='user_id=234301&user_token=c4ee8a01a7c03725515a70a816fef6e3ceb9817ac4fdecaacce9af9e31948128&site_id=22&filters_json=%7B%22_self%22%3A%7B%22latitude%22%3A%5B19.2377%2C19.6027%5D%2C%22longitude%22%3A%5B-99.3256%2C-98.8727%5D%2C%22type%22%3A%5B%22scooter%22%2C%22kick%22%5D%7D%7D', headers=headersDynamic)

		nowf2 = datetime.datetime.now()

		content = str(milis)+'--'+r.text
		zCompressed = zlib.compress(str(content).encode())

		print('Done writing - compressed', len(zCompressed)/1000, 'KBs')
		print(len(r.text))
		#zCompressed = zlib.compress(r.text)
		nowf2 = datetime.datetime.now()
		filenm = dpath+"MX/P-"+str(0)+"-responseEncoded-"+nowf2.strftime("%Y-%m-%d")+".txt"
		logFile = open(filenm, "ab")
		toBeWrittenData = ""
		logFile.write(zCompressed)
		logFile.write(b'0x0A')
		logFile.close()
		i = 1
		print(ietc,'Starters at:',nowf3.strftime('%I:%M %p'),': Movo Mexico City')
		ietc +=1
		if(ietc > 100):
			ietc = 0
			print('longer sleep')
			time.sleep(100)
		time.sleep(35)