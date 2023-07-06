import os
import time

# toronto scripts 

full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'

os.system("xterm -e \"python3 "+dpath+"Bird/BirdDetroit.py\" &")

os.system("xterm -e \"python3 "+dpath+"Lime/LimeLauncher.py\" &")
time.sleep(1)
os.system("xterm -e \"python3 "+dpath+"Spin/SpinDetroit.py\" &")
