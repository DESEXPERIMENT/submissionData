from calendar import c, week
from operator import le
import os
import time

import json

import warnings
from scipy import stats
warnings.filterwarnings("ignore")
from datetime import datetime, timedelta
import pytz
import datetime

import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from scipy.stats import kendalltau
from scipy.stats import pearsonr
import numpy as np
from scipy.spatial.distance import cdist
from math import sin, cos, sqrt, atan2, radians

phases = ['P1']

cityAndServiceDict = {'P1': {'SanFrancisco': ['Scoot', 'Jump'], 'Brussels': ['Lime', 'Circ', 'Jump'], 'Detroit': ['Spin', 'Bird', 'Lime'], 'Chicago': ['LyftScooter', 'Jump'], 'Madrid': ['Voi', 'Bird', 'Wind', 'Lime', 'Circ', 'Jump', 'Tier'], 'Paris': ['Bird', 'Voi', 'Wind', 'Lime', 'Jump', 'Tier'], 'TelAviv': ['Bird', 'Wind', 'Lime'], 'MexicoCity': ['Movo', 'Lime'], 'Zurich': ['Bird', 'Tier'], 'DC': ['Spin', 'LyftScooter', 'Skip', 'Bird', 'Lime', 'Jump'], 'Lisbon': ['Voi', 'Bird', 'Circ', 'Wind', 'Jump', 'Tier']}, 'P2': {'SanFrancisco': ['Bird', 'Lime'], 'Brussels': ['Circ', 'Lime'], 'Detroit': ['Bird'], 'Chicago': ['LyftScooter'], 'Madrid': ['Bird', 'Lime'], 'Paris': ['Tier', 'Bird', 'Lime', 'Voi'], 'TelAviv': ['Bird', 'Lime', 'Wind'], 'MexicoCity': ['Movo', 'Lime'], 'Zurich': ['Tier', 'Bird'], 'DC': ['LyftScooter', 'Bird', 'Lime', 'Spin'], 'Lisbon': ['Bird', 'Lime']}}

cityTimeDelta = {}
cityTimeDelta['Brussels'] = 'Europe/Brussels'
cityTimeDelta['Chicago'] =  'America/Chicago'
cityTimeDelta['DC'] = 'America/New_York'
cityTimeDelta['Detroit'] = 'America/Detroit'
cityTimeDelta['Lisbon'] = 'Europe/Lisbon'
cityTimeDelta['Madrid'] = 'Europe/Madrid'
cityTimeDelta['MexicoCity'] = 'America/Mexico_City'
cityTimeDelta['Paris'] = 'Europe/Paris'
cityTimeDelta['SanFrancisco'] = 'America/Los_Angeles'
cityTimeDelta['TelAviv'] = 'Asia/Jerusalem'
cityTimeDelta['Zurich'] = 'Europe/Zurich'

datesTimeWindow = {}


otherWindowDelta = 1
windowDelta = 60
totalLocations = {}
totalCorrelation = []

totalServicesColors = {}
totalServicesColors['Circ'] ='#800000'
totalServicesColors['Lime'] ='#FF0000'
totalServicesColors['Jump'] ='#FFA500'
totalServicesColors['LyftScooter'] ='#FFFF00'
totalServicesColors['Bird'] ='#808000'
totalServicesColors['Skip'] ='#800080'
totalServicesColors['Spin'] ='#FF00FF'
totalServicesColors['Voi'] ='#00FF00'
totalServicesColors['Tier'] ='#008000'
totalServicesColors['Wind'] ='#000080'
totalServicesColors['Movo'] ='#00FFFF'
totalServicesColors['Scoot'] ='#C0C0C0'


cities = list(cityAndServiceDict['P1'])
cities.sort()



hourlyUtilDict = {}


cityDone = 0



tempCats = ['Educational\nFacilities', 'Business\n&\nServices', 'Residential\nArea', 'Govt./\nFacility', 'Clothing\n&\nAccessories', 'Libraries', 'Parking\nFacility', 'Public\nTransport', 'Taxi\nStand', 'Food\n&\nDrink']
n=len(tempCats)
r = np.arange(n)
width = 0.8

colorsList = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
labelsList = []

p1 = [17.78181818181818, 15.490909090909089, 11.236363636363636, 7.963636363636364, 6.327272727272727, 5.672727272727273, 5.236363636363635, 4.6909090909090905, 4.581818181818182, 3.4909090909090907]


plt.rcParams["figure.figsize"] = (8,5.9)


plt.bar(r, p1, color = 'gray',
        width = width, edgecolor = 'black')

plt.xlabel("Location categories", fontsize=20)
plt.ylabel("Two-way Trips Percentage", fontsize=20)
# plt.title("Categorical two-way trips% out of total two-way trips")


legenLines = []
legenLinesLabels = []

print(tempCats)

for i in range(0, len(tempCats)):
    r[i] = r[i]+0.5

plt.yticks(fontsize=17, rotation=0)

xoffset = 0
for i in range(0,len(tempCats)):
    textcat = tempCats[i]
    textcat = textcat.replace('\n', ' ')
    text_kwargs = dict(ha='center', va='center', rotation=90, fontsize=20, color='Black')
    # if i < 4:
        # plt.text(xoffset, 7, textcat, **text_kwargs)
    # else:
    yval  = p1[i]/2
    if i >3:
        yval = p1[i]*2
    if  i == 5:
        yval = p1[i]*1.5
    if i == 8:
        yval = p1[i]*1.7
    
    plt.text(xoffset, yval, textcat, **text_kwargs)
    xoffset += 1

plt.xticks([],[])

plt.subplots_adjust(left=0.12,
                bottom=0.05, 
                right=0.99, 
                top=0.939, 
                wspace=0.05, 
                hspace=0.01)


plt.savefig('Results2l/2l12-twowayCitiesCatsPercentage.png')
plt.savefig('Results2l/2l12-twowayCitiesCatsPercentage.eps')

plt.clf()

