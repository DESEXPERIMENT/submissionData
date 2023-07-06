import subprocess
import os
import time

full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'


while 1:
	os.system("python3 "+dpath+"LimeParis.py")
	print('Sleeping for 30 sec')
	time.sleep(40)
