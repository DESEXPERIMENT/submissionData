from calendar import c
from operator import le
import os
import time

import json

import warnings
from scipy import stats
warnings.filterwarnings("ignore")
from datetime import datetime, timedelta
import pytz
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from descartes import PolygonPatch
from shapely.geometry import box, Polygon, MultiPolygon, GeometryCollection

from scipy.stats import kendalltau
from scipy.stats import pearsonr
import numpy as np
from scipy.spatial.distance import cdist


import numpy as np
import numpy.random
import matplotlib.pyplot as plt
from shapely.geometry import asShape # manipulating geometry
import seaborn as sns
from scipy.spatial import cKDTree
import matplotlib.cm as cm
from matplotlib.patches import Patch
from matplotlib.lines import Line2D


def data_coord2view_coord(p, resolution, pmin, pmax):
    dp = pmax - pmin
    dv = (p - pmin) / dp * resolution
    return dv



phases = ['P1', 'P2']




cityAndServiceDict = {'P1': {'SanFrancisco': ['Scoot', 'Jump'], 'Brussels': ['Lime', 'Circ', 'Jump'], 'Detroit': ['Spin', 'Bird', 'Lime'], 'Chicago': ['LyftScooter', 'Jump'], 'Madrid': ['Voi', 'Bird', 'Wind', 'Lime', 'Circ', 'Jump', 'Tier'], 'Paris': ['Bird', 'Voi', 'Wind', 'Lime', 'Jump', 'Tier'], 'TelAviv': ['Bird', 'Wind', 'Lime'], 'MexicoCity': ['Movo', 'Lime'], 'Zurich': ['Bird', 'Tier'], 'DC': ['Spin', 'LyftScooter', 'Skip', 'Bird', 'Lime', 'Jump'], 'Lisbon': ['Voi', 'Bird', 'Circ', 'Wind', 'Jump', 'Tier']}, 'P2': {'SanFrancisco': ['Bird', 'Lime'], 'Brussels': ['Circ', 'Lime'], 'Detroit': ['Bird'], 'Chicago': ['LyftScooter'], 'Madrid': ['Bird', 'Lime'], 'Paris': ['Tier', 'Bird', 'Lime', 'Voi'], 'TelAviv': ['Bird', 'Lime', 'Wind'], 'MexicoCity': ['Movo', 'Lime'], 'Zurich': ['Tier', 'Bird'], 'DC': ['LyftScooter', 'Bird', 'Lime', 'Spin'], 'Lisbon': ['Bird', 'Lime']}}


totalServicesColors = {}
totalServicesColors['Bird'] = (0.9554474166212361, 0.7459731394920444, 0.0026170137322456544)
totalServicesColors['Circ'] = (0.4142129200649052, 0.42555039949753826, 0.25225294260246656)
totalServicesColors['Jump'] = (0.3296664605096191, 0.47834124362580377, 0.5605835286795703)
totalServicesColors['Lime'] = (0.8556147726350499, 0.2727362473963153, 0.13140635340726659)
totalServicesColors['LyftScooter'] = (0.8210114253872471, 0.5345817538295028, 0.2944545678038304)
totalServicesColors['Movo'] =  (0.6354468639306041, 0.7675394278173934, 0.6239493801884614)
totalServicesColors['Scoot'] = (0.010005718214378678, 0.7244359665901243, 0.24160721313845768)
totalServicesColors['Skip'] = (0.0024234876338239397, 0.2455766145923386, 0.016886799525566265)
totalServicesColors['Spin'] = (0.9151364173731882, 0.7312665294075509, 0.9811423414138214)
totalServicesColors['Tier'] = (0.5, 0, 0)
totalServicesColors['Voi'] = (0.11317432893945689, 0.5631925853747284, 0.7442930586201215)
totalServicesColors['Wind'] = (0.7827819162943063, 0.7563760713398012, 0.1032224970669354)


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


otherWindowDelta = 5
windowDelta = 10
totalLocations = {}
totalCitiesNH = []



import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(0)
sns.set()


totalCats = ['ATM/Bank/Exchange', 'Accommodation', 'Bar/Pub', 'Book Shop', 'Business & Services', 'Business/Industry', 'Car Dealer/Repair', 'Car Hire', "Chemist's", 'Cinema', 'Clothing & Accessories', 'Coffee/Tea', 'Communications/Media', 'DIY/garden centre', 'Dance or Nightclub', 'EV Charging Station', 'Eat & Drink', 'Educational Facility', 'Electronics', 'Facility', 'Food & Drink', 'Forest, Heath or Other Vegetation', 'Going Out', 'Government or Community Facility', 'Hospital or Healthcare Facility', 'Hostel', 'Hotel', 'Kiosk/24-7/Convenience Store', 'Landmark/Attraction', 'Library', 'Museum', 'Outdoor Sports', 'Parking Facility', 'Petrol Station', 'Police Station', 'Post Office', 'Public Transport', 'Railway Station', 'Recreation', 'Religious Place', 'Restaurant', 'Service', 'Shop', 'Shopping Centre', 'Sights & Museums', 'Snacks/Fast food', 'Sport Facility/Venue', 'Taxi Stand', 'Theatre, Music & Culture', 'Theme Park', 'Tourist Information', 'Transport', 'Travel Agency', 'Wine & Spirits', 'Body of Water', 'Building', 'Department Store', 'Fire Brigade', 'Natural or Geographical', 'Outdoor Area/Complex', 'Ambulance Services', 'Fair & Convention Facility', 'Police/Emergency', 'Public Toilet/Rest Area', 'Ferry Terminal', 'Hospital', 'Zoo', 'Casino', 'Motel']


catValPair  = [['Bar/Pub', 0.38], ['Car Hire', 0.38], ['Business & Services', 0.4], ['Clothing & Accessories', 0.4], ['Electronics', 0.4], ['Snacks/Fast food', 0.4], ['Hotel', 0.41], ['Parking Facility', 0.41], ['Public Transport', 0.41], ['Service', 0.41], ['Educational Facility', 0.42], ['Recreation', 0.43], ['Hospital or Healthcare Facility', 0.44], ['Shop', 0.44], ['Sport Facility/Venue', 0.44], ['ATM/Bank/Exchange', 0.45], ['DIY/garden centre', 0.45], ['Food & Drink', 0.45], ['Restaurant', 0.45], ['Coffee/Tea', 0.46], ['Petrol Station', 0.47], ['Religious Place', 0.49], ['Car Dealer/Repair', 0.5], ['Dance or Nightclub', 0.51]]


citiesLong = list(cityTimeDelta.keys())
citiesLong.sort()



newTotalData = [[0.13, 0.34, 0.06, 0.35, 0.08, 0.32, 0.8610887854316747, 0.19, 0.1, 0.07, 0.35], [0.32, 0.11, 0.11, 0.24, 0.31, 0.33, 0.81, 0.08, 0.09, 0.27, 0.38], [0.32, 0.2, 0.39, 0.37, 0.38, 0.13, 0.908627520802376, 0.36, 0.2, 0.07, 0.31], [0.29, 0.25, 0.35, 0.1, 0.27, 0.36, 0.6248088710099771, 0.2, 0.36, 0.36, 0.18], [0.31, 0.28, 0.29, 0.05, 0.2, 0.38, 0.8264633458685795, 0.05, 0.29, 0.12, 0.35], [0.46, 0.54, 0.51, 0.62, 0.56, 0.44, 0.8362598010953293, 0.65, 0.68, 0.64, 0.41], [0.47, 0.56, 0.43, 0.62, 0.43, 0.42, 0.7407968749022227, 0.44, 0.41, 0.45, 0.49], [0.5, 0.57, 0.62, 0.48, 0.61, 0.6, 0.6139981355380547, 0.67, 0.47, 0.59, 0.45], [0.66, 0.55, 0.5, 0.44, 0.68, 0.59, 0.7327744407920407, 0.55, 0.42, 0.67, 0.64], [0.51, 0.56, 0.48, 0.41, 0.49, 0.46, 0.84, 0.54, 0.59, 0.41, 0.44]]

ylticls = ['Bar/Pub', 'Car Hire', 'Business & Services', 'Clothing & Accessories', 'Electronics', 'Coffee/Tea', 'Petrol Station', 'Religious Place', 'Car Dealer/Repair', 'Dance or Nightclub']

yticksNew = []
plt_1 = plt.figure(figsize=(6.5, 5))


print(newTotalData)
for i in range(0,len(newTotalData)):
    print(i, np.average(newTotalData[i]))
ax = sns.heatmap(newTotalData, cbar=False, vmin=0, vmax=1,annot=True, annot_kws={"size":13}, cbar_kws={"shrink": .7})


linecolor="grey"


cities = ['BXL', 'CHI', 'WDC', 'DTW', 'LXN', 'MAD', 'MXC', 'PAR', 'SFX', 'TLV', 'ZRX']

# plt.ylabel('Hotspots Categories', fontsize=19)
# plt.xlabel('Cities', fontsize=17,labelpad=19)

xt = []
yt = []

ylticls = yticksNew= ['Business &\n Services', 'Educational \nFacilities', 'Food &\n Drink', 'Clothing/\nAccessories', 'Public\nTransport', 'Tourist\nAttractions', 'Healthcare\nFacility', 'Religious\nPlace', 'Car Dealer\n/Repair', 'Convenience\nStores']

for i in range (len(ylticls)):
    yt.append(i)
for i in range (len(cities)):
    xt.append(i)
for i in range(0, len(ylticls)):
    yt[i]+=0.5
for i in range(0, len(xt)):
    xt[i]+=0.5

plt.yticks(yt, yticksNew, rotation=0, fontsize=14)

plt.xticks(xt, cities, rotation=90, fontsize=14)

plt.subplots_adjust(left=0.0,
                    bottom=0.0, 
                    right=0.79, 
                    top=.87, 
                    wspace=0.1, 
                    hspace=0.4)

ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
ax.yaxis.tick_right()


plt.savefig('Results2l/2l6b-giCities.png')
plt.savefig('Results2l/2l6b-giCities.eps')