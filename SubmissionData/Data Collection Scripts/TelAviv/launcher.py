import os
import time

# toronto scripts 

full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'


#1 uber near by
os.system("xterm -e \"python3 "+dpath+"Wind/WindLauncherTA.py\" &")

os.system("xterm -e \"python3 "+dpath+"Bird/BirdTA.py\" &")


# os.system("xterm -e \"python3 "+dpath+"Wind/WindParis.py\" &")

# os.system("xterm -e \"python3 "+dpath+"Tier/TierParis.py\" &")

# os.system("xterm -e \"python3 "+dpath+"Jump/JumpParis.py\" &")

os.system("xterm -e \"python3 "+dpath+"Lime/LimeLauncher.py\" &")