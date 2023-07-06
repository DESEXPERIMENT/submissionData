import os
import time

# toronto scripts 

full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'


#1 uber near by
os.system("xterm -e \"python3 "+dpath+"Circ/CircMadrid.py\" &")

os.system("xterm -e \"python3 "+dpath+"Bird/BirdMadrid.py\" &")

os.system("xterm -e \"python3 "+dpath+"Lime/LimeLauncher.py\" &")

os.system("xterm -e \"python3 "+dpath+"Tier/TierMadrid.py\" &")

os.system("xterm -e \"python3 "+dpath+"Wind/WindLauncherMadrid.py\" &")

os.system("xterm -e \"python3 "+dpath+"Jump/JumpMadrid.py\" &")