import os
import time

# toronto scripts 

full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'


#1 uber near by
os.system("xterm -e \"python3 "+dpath+"Circ/CircLisbon.py\" &")

os.system("xterm -e \"python3 "+dpath+"Bird/BirdLisbon.py\" &")

# os.system("xterm -e \"python3 "+dpath+"Lime/LimeLauncher.py\" &")

os.system("xterm -e \"python3 "+dpath+"Tier/TierLisbon.py\" &")

os.system("xterm -e \"python3 "+dpath+"Wind/WindLauncherLisbon.py\" &")

os.system("xterm -e \"python3 "+dpath+"Jump/JumpLisbon.py\" &")

os.system("xterm -e \"python3 "+dpath+"Voi/VoiLisbon.py\" &")