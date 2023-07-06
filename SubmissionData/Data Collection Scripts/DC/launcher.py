import os
import time

# toronto scripts 

full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'


#1 uber near by
os.system("xterm -e \"python3 "+dpath+"Skip/SkipDC.py\" &")

os.system("xterm -e \"python3 "+dpath+"Bird/BirdDC.py\" &")

os.system("xterm -e \"python3 "+dpath+"Lime/LimeLauncher.py\" &")

os.system("xterm -e \"python3 "+dpath+"Spin/SpinDC.py\" &")

os.system("xterm -e \"python3 "+dpath+"Jump/JumpDC.py\" &")

os.system("xterm -e \"python3 "+dpath+"LyftScooter/LyftDC.py\" &")
