import os
import time

import psutil
import datetime

def killXtermProcs():
	PROCNAME1 = "xterm"
	count = 0
	for proc in psutil.process_iter():
		try:
			if PROCNAME1 in proc.name():
				count +=1
				proc.kill()
		except Exception as e:
			time.sleep(2)
			print(e)


full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'

hcount = 0
killWait = 1800
while 1:
	try:
		datetime.datetime.now()
		hcount = hcount+1
		print(hcount, 'Starting Procs: ',datetime.datetime.now().time())

		os.system("python "+dpath+"Paris/launcher.py")
		os.system("python "+dpath+"TelAviv/launcher.py")
		os.system("python "+dpath+"Madrid/launcher.py")
		os.system("python "+dpath+"Lisbon/launcher.py")
		os.system("python "+dpath+"Brussels/launcher.py")
		os.system("python "+dpath+"MexicoCity/launcher.py")
		os.system("python "+dpath+"Zurich/launcher.py")
		os.system("python "+dpath+"SanFrancisco/launcher.py")
		os.system("python "+dpath+"Chicago/launcher.py")
		os.system("python "+dpath+"Detroit/launcher.py")
		os.system("python "+dpath+"DC/launcher.py")

		
		
		#sleep
		time.sleep(killWait)

		killXtermProcs()
		datetime.datetime.now()
		print('Stopping Procs: ',datetime.datetime.now().time())
		time.sleep(60)
	except Exception as e:
		time.sleep(60)
		print(e)



