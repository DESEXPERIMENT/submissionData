import os
import time

# toronto scripts 

full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'


#1 uber near by
# os.system("xterm -e \"python3 "+dpath+"Circ/CircBrussels.py\" &")

# os.system("xterm -e \"python3 "+dpath+"Bird/BirdLisbon.py\" &")

os.system("xterm -e \"python3 "+dpath+"Lime/LimeLauncher.py\" &")
os.system("xterm -e \"python3 "+dpath+"Movo/MovoMX.py\" &")
# os.system("xterm -e \"python3 "+dpath+"Tier/TierBrussels.py\" &")

# # os.system("xterm -e \"python3 "+dpath+"Wind/WindLisbon.py\" &")

# os.system("xterm -e \"python3 "+dpath+"Jump/JumpBrussels.py\" &")

# os.system("xterm -e \"python3 "+dpath+"Voi/VoiLisbon.py\" &")