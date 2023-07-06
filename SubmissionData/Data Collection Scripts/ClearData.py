from os import listdir
from os.path import isfile, join
import os
from distutils.dir_util import copy_tree
from shutil import copytree,copy2

cdate = '2019-10-30'
cfiles = 0 
def copy2_verbose(src, dst):
    global cfiles
    if 'responseEncoded' in src and cdate in src:
    	cfiles += 1
    	print(cfiles , 'Copying {0}'.format(src))
    	copy2(src,dst)
    elif 'responseEncoded' not in src :
    	cfiles += 1
    	print(cfiles, 'Copying {0}'.format(src))
    	copy2(src,dst)


dataPaths = [
#Paris
'/home/hakhan/Desktop/ScooterProject/Paris/Lime/Paris',
'/home/hakhan/Desktop/ScooterProject/Paris/Bird/Paris',
'/home/hakhan/Desktop/ScooterProject/Paris/Wind/Paris',
'/home/hakhan/Desktop/ScooterProject/Paris/Tier/Paris',
'/home/hakhan/Desktop/ScooterProject/Paris/Jump/Paris',
#Tel Aviv
'/home/hakhan/Desktop/ScooterProject/TelAviv/Lime/TA',
'/home/hakhan/Desktop/ScooterProject/TelAviv/Wind/TA',
'/home/hakhan/Desktop/ScooterProject/TelAviv/Bird/TA',

#Madrid
'/home/hakhan/Desktop/ScooterProject/Madrid/Lime/Madrid',
'/home/hakhan/Desktop/ScooterProject/Madrid/Circ/Madrid',
'/home/hakhan/Desktop/ScooterProject/Madrid/Bird/Madrid',
'/home/hakhan/Desktop/ScooterProject/Madrid/Tier/Madrid',
'/home/hakhan/Desktop/ScooterProject/Madrid/Wind/Madrid',
'/home/hakhan/Desktop/ScooterProject/Madrid/Jump/Madrid',

#Lisbon
'/home/hakhan/Desktop/ScooterProject/Lisbon/Jump/Lisbon',
'/home/hakhan/Desktop/ScooterProject/Lisbon/Wind/Lisbon',
'/home/hakhan/Desktop/ScooterProject/Lisbon/Voi/Lisbon',
'/home/hakhan/Desktop/ScooterProject/Lisbon/Tier/Lisbon',
'/home/hakhan/Desktop/ScooterProject/Lisbon/Circ/Lisbon',
'/home/hakhan/Desktop/ScooterProject/Lisbon/Bird/Lisbon',

#Brussels
'/home/hakhan/Desktop/ScooterProject/Brussels/Lime/Brussels',
'/home/hakhan/Desktop/ScooterProject/Brussels/Jump/Brussels',
'/home/hakhan/Desktop/ScooterProject/Brussels/Tier/Brussels',
'/home/hakhan/Desktop/ScooterProject/Brussels/Circ/Brussels',

#Mexico city 
'/home/hakhan/Desktop/ScooterProject/MexicoCity/Lime/MX',
'/home/hakhan/Desktop/ScooterProject/MexicoCity/Movo/MX',

#Zurich
'/home/hakhan/Desktop/ScooterProject/Zurich/Tier/Zurich',
'/home/hakhan/Desktop/ScooterProject/Zurich/Bird/Zurich',

#San Francisco
'/home/hakhan/Desktop/ScooterProject/SanFrancisco/Jump/SF',
'/home/hakhan/Desktop/ScooterProject/SanFrancisco/Scoot/SF',

#Chicago 
'/home/hakhan/Desktop/ScooterProject/Chicago/Jump/Chicago',
'/home/hakhan/Desktop/ScooterProject/Chicago/LyftScooter/Chicago',

#Detroit
'/home/hakhan/Desktop/ScooterProject/Detroit/Lime/Detroit',
'/home/hakhan/Desktop/ScooterProject/Detroit/Bird/Detroit',
'/home/hakhan/Desktop/ScooterProject/Detroit/Spin/Detroit',

# Washington DC
'/home/hakhan/Desktop/ScooterProject/DC/Lime/DC',
'/home/hakhan/Desktop/ScooterProject/DC/Skip/DC',
'/home/hakhan/Desktop/ScooterProject/DC/Bird/DC',
'/home/hakhan/Desktop/ScooterProject/DC/Jump/DC',
'/home/hakhan/Desktop/ScooterProject/DC/Spin/DC',
'/home/hakhan/Desktop/ScooterProject/DC/LyftScooter/DC'
]


# define the name of the directory to be created
path = '/media/hakhan/Seagate Expansion Drive/ScooterBackup/'+cdate


src = '/home/hakhan/Desktop/ScooterProject'

try:  
    os.mkdir(path)

except OSError:  
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s " % path)

    copytree(src, path+'/backup/', copy_function=copy2_verbose)


    #copy_tree('/home/hakhan/Desktop/ScooterProject', path)
    print('-------- Copied on the External Hard ------')
    for mypath in dataPaths:
    	print(mypath)
    	for f in listdir(mypath):
    		if isfile(join(mypath, f)):
    			if cdate in f:
    				print('\t',f)
    				os.remove(mypath+'/'+f)
					
