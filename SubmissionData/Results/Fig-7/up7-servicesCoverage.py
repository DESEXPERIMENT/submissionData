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


totalData = {'SanFrancisco': {'nhCount': 28, 'services': {'Bird': -5, 'Circ': -5, 'Jump': 0.72, 'Lime': -5, 'LyftScooter': -5, 'Movo': -5, 'Scoot': 0.75, 'Skip': -5, 'Spin': -5, 'Tier': -5, 'Voi': -5, 'Wind': -5}}, 'Brussels': {'nhCount': 50, 'services': {'Bird': -5, 'Circ': 0.31, 'Jump': 0.51, 'Lime': 0.11, 'LyftScooter': -5, 'Movo': -5, 'Scoot': -5, 'Skip': -5, 'Spin': -5, 'Tier': -5, 'Voi': -5, 'Wind': -5}}, 'Detroit': {'nhCount': 26, 'services': {'Bird': 0.26, 'Circ': -5, 'Jump': -5, 'Lime': 0.06, 'LyftScooter': -5, 'Movo': -5, 'Scoot': -5, 'Skip': -5, 'Spin': 0.11, 'Tier': -5, 'Voi': -5, 'Wind': -5}}, 'Chicago': {'nhCount': 57, 'services': {'Bird': -5, 'Circ': -5, 'Jump': 0.16, 'Lime': -5, 'LyftScooter': 0.15, 'Movo': -5, 'Scoot': -5, 'Skip': -5, 'Spin': -5, 'Tier': -5, 'Voi': -5, 'Wind': -5}}, 'Madrid': {'nhCount': 131, 'services': {'Bird': 0.42, 'Circ': 0.24, 'Jump': 0.56, 'Lime': 0.36, 'LyftScooter': -5, 'Movo': -5, 'Scoot': -5, 'Skip': -5, 'Spin': -5, 'Tier': 0.32, 'Voi': 0.41, 'Wind': 0.09}}, 'Paris': {'nhCount': 20, 'services': {'Bird': 0.5, 'Circ': -5, 'Jump': 0.95, 'Lime': 0.48, 'LyftScooter': -5, 'Movo': -5, 'Scoot': -5, 'Skip': -5, 'Spin': -5, 'Tier': 0.37, 'Voi': 0.73, 'Wind': 0.33}}, 'TelAviv': {'nhCount': 178, 'services': {'Bird': 0.4, 'Circ': -5, 'Jump': -5, 'Lime': 0.12, 'LyftScooter': -5, 'Movo': -5, 'Scoot': -5, 'Skip': -5, 'Spin': -5, 'Tier': -5, 'Voi': -5, 'Wind': 0.22}}, 'MexicoCity': {'nhCount': 62, 'services': {'Bird': -5, 'Circ': -5, 'Jump': -5, 'Lime': 0.07, 'LyftScooter': -5, 'Movo': 0.03, 'Scoot': -5, 'Skip': -5, 'Spin': -5, 'Tier': -5, 'Voi': -5, 'Wind': -5}}, 'Zurich': {'nhCount': 22, 'services': {'Bird': 0.56, 'Circ': -5, 'Jump': -5, 'Lime': -5, 'LyftScooter': -5, 'Movo': -5, 'Scoot': -5, 'Skip': -5, 'Spin': -5, 'Tier': 0.47, 'Voi': -5, 'Wind': -5}}, 'DC': {'nhCount': 46, 'services': {'Bird': 0.47, 'Circ': -5, 'Jump': 0.93, 'Lime': 0.47, 'LyftScooter': 0.66, 'Movo': -5, 'Scoot': -5, 'Skip': 0.0, 'Spin': 0.45, 'Tier': -5, 'Voi': -5, 'Wind': -5}}, 'Lisbon': {'nhCount': 20, 'services': {'Bird': 0.38, 'Circ': 0.59, 'Jump': 0.96, 'Lime': -5, 'LyftScooter': -5, 'Movo': -5, 'Scoot': -5, 'Skip': -5, 'Spin': -5, 'Tier': 0.34, 'Voi': 0.42, 'Wind': 0.33}}}


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(0)
sns.set()
uniform_data = np.random.rand(11, 12)

# cmap = plt.get_cmap(GnRd,30)
# cmap.set_under('dimgrey')#Colour values less than vmin in white
# cmap.set_over('dimgrey')# colour valued larger than vmax in red

services = list(totalServicesColors.keys())
services.sort()
citiesLong = list(cityTimeDelta.keys())


fx = open('up7-newTotalData.txt', 'r')
newTotalData = json.loads(fx.read())
fx.close()

fx = open('up7-maxVals.txt', 'r')
maxVals = json.loads(fx.read())
fx.close()


# print(np.average(maxVals))
# print(newTotalData)

plt_1 = plt.figure(figsize=(1.8*3, 1.3*3.4))


ax = sns.heatmap(newTotalData, cbar=False, vmin=0, vmax=100, annot=True,linewidths=0.4,  cbar_kws={"shrink": .7}, annot_kws={"size":15})


linecolor="grey"

for t in ax.texts:
    if float(t.get_text())<=100 and float(t.get_text())>0:
        t.set_text(t.get_text()) #if the value is greater than 0.4 then I set the text 
    else:
        t.set_text('') # if not it sets an empty text


cities = ['BXL', 'CHI', 'WDC', 'DTW', 'LXN', 'MAD', 'MXC', 'PAR', 'SFX', 'TLV', 'ZRX']

# plt.xlabel('Services',fontsize=14)#fontweight='bold')
# plt.ylabel('Cities', fontsize=14)#fontweight='bold')

# plt.title('Percentage of Census Tracts Covered by available DES providers in each city.')
yt = [0,1,2,3,4,5,6,7,8,9,10]
xt = [0,1,2,3,4,5,6,7,8,9,10,11]

for i in range(0, len(yt)):
    yt[i]+=0.5
for i in range(0, len(xt)):
    xt[i]+=0.5
plt.yticks(yt, cities, rotation=0)
services[4]= 'Lyft'
plt.xticks(xt, services, rotation=90)

# plt.yticks([0,10,20,30,40,50,60,70,80,90,100])
ax.tick_params(axis='both', which='major', labelsize=15)

plt.subplots_adjust(left=0.13,
                    bottom=0.18, 
                    right=0.99, 
                    top=0.99, 
                    wspace=0.1, 
                    hspace=0.4)


plt.savefig('Results2l/2l3-servicesCoverage.png')
plt.savefig('Results2l/2l3-servicesCoverage.eps')