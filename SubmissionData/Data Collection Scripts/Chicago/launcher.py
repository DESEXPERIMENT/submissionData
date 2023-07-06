import os
import time

# toronto scripts 

full_path = os.path.realpath(__file__)
dpath, realfilename = os.path.split(full_path)

dpath +='/'


os.system("xterm -e \"python3 "+dpath+"Jump/JumpChicago.py\" &")

os.system("xterm -e \"python3 "+dpath+"LyftScooter/LyftChicago.py\" &")