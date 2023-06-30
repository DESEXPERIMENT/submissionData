from nis import cat
import os
import sys
sys.path = [os.path.abspath("..")] + sys.path

import matplotlib.pyplot as plt
import numpy as np

from mpl_chord_diagram import chord_diagram


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



phases = ['P1', 'P2']



cityAndServiceDict = {'P1': {'SanFrancisco': ['Scoot', 'Jump'], 'Brussels': ['Lime', 'Circ', 'Jump'], 'Detroit': ['Spin', 'Bird', 'Lime'], 'Chicago': ['LyftScooter', 'Jump'], 'Madrid': ['Voi', 'Bird', 'Wind', 'Lime', 'Circ', 'Jump', 'Tier'], 'Paris': ['Bird', 'Voi', 'Wind', 'Lime', 'Jump', 'Tier'], 'TelAviv': ['Bird', 'Wind', 'Lime'], 'MexicoCity': ['Movo', 'Lime'], 'Zurich': ['Bird', 'Tier'], 'DC': ['Spin', 'LyftScooter', 'Skip', 'Bird', 'Lime', 'Jump'], 'Lisbon': ['Voi', 'Bird', 'Circ', 'Wind', 'Jump', 'Tier']}, 'P2': {'SanFrancisco': ['Bird', 'Lime'], 'Brussels': ['Circ', 'Lime'], 'Detroit': ['Bird'], 'Chicago': ['LyftScooter'], 'Madrid': ['Bird', 'Lime'], 'Paris': ['Tier', 'Bird', 'Lime', 'Voi'], 'TelAviv': ['Bird', 'Lime', 'Wind'], 'MexicoCity': ['Movo', 'Lime'], 'Zurich': ['Tier', 'Bird'], 'DC': ['LyftScooter', 'Bird', 'Lime', 'Spin'], 'Lisbon': ['Bird', 'Lime']}}

baseAddress = '/home/hakhan/Google Drive/Scooter_Sheets/Dictionaries/'

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


totalCats = []


from matplotlib.lines import Line2D




from mpl_toolkits.axes_grid.anchored_artists import AnchoredText

cities = ['Brussels', 'Lisbon']


catCodeMap = {}
catCodeMap['Food & Drink'] = 'C1'
catCodeMap['Restaurant'] = 'C1'
catCodeMap['Business & Services'] = 'C2'
catCodeMap['Educational Facilities'] = 'C3'
catCodeMap['Public Transport'] = 'C4'
catCodeMap['Tourist Attractions'] = 'C5'
catCodeMap['Clothing & Accessories'] = 'C6'
catCodeMap['Bar/Pub'] = 'C7'
catCodeMap['Recreational Place'] = 'C8'
catCodeMap['Cinema'] = 'C9'
catCodeMap['Sport Facility'] = 'C10'
catCodeMap['ATM/Bank/Exchange'] = 'C11'
catCodeMap['Parking Facility'] = 'C12'
catCodeMap['Dance or Nightclub'] = 'C13'
catCodeMap['Hospital or Healthcare '] = 'C14'
catCodeMap['Residential Area'] = 'C16'
catCodeMap['Unknown'] = 'C16'






newCatCodes = {}
for city in cities:
    namesCodeDict = {}
    namesCodeDict['code'] = 1
    categoryTripsDict = {}

    # cityDone += 1
    categoryTripsDict[city] = {}
    hourlyUtilDict[city] = {}
    totalDates = {}
    supplyPhase = {}

    for phase in ['P1']:

        flux = []
        names = []

        newList = []

   
        newListNames = []

        
        if 'Bru' in city:
            flux = [[1771.2, 2340.0, 1404.0, 1105.5, 1369.5, 3660.0, 1471.5], [2389.5, 1931.28, 3052.5, 2239.5, 3610.5, 7332.0, 2833.5], [1432.5, 3126.0, 2545.6000000000004, 1374.0, 1737.0, 4342.5, 1888.5], [1021.5, 2253.0, 1368.0, 1772.0, 1305.0, 3366.0, 1519.5], [1218.0, 3696.0, 1687.5, 1252.5, 7016.0, 3855.0, 1582.5], [3459.0, 7417.5, 4479.0, 3262.5, 3777.0, 3006.48, 4266.0], [1386.0, 2821.5, 1908.0, 1401.0, 1699.5, 4135.5, 2964.8]]
        else:
            flux = [[359.03999999999996, 796.5, 621.0, 853.5, 808.5, 2772.0, 1993.5], [675.0, 813.6, 448.5, 654.0, 640.5, 2070.0, 1680.0], [580.5, 489.0, 675.2, 588.0, 432.0, 1486.5, 1279.5], [916.5, 646.5, 528.0, 1512.8000000000002, 759.0, 3169.5, 1786.5], [762.0, 597.0, 517.5, 757.5, 384.8, 2127.0, 1506.0], [2640.0, 2100.0, 1464.0, 3025.5, 2112.0, 2251.92, 5703.0], [1846.5, 1714.5, 1215.0, 1786.5, 1522.5, 5908.5, 3507.2000000000003]]
        # print(flux)
        # time.sleep(1000)
        # plot different examples

        grads = True               # gradient
        gaps  = 0.05                       # gap value
        sorts = "size"    # sort type
        cclrs = None        # chord colors
        nrota = True               # name rotation
        cmaps = None             # colormap
        fclrs = "grey"                                    # fontcolors
        drctd = True               # directed
        names = []
        for i in range(0,len(flux)):
            # print(flux[i])
            names.append('')

        ax = chord_diagram(flux, names, gap=gaps, use_gradient=grads, sort=sorts, directed=drctd,
                  cmap=cmaps, chord_colors=cclrs, rotate_names=nrota, fontcolor=fclrs)
        plt.tight_layout()

        text_kwargs = dict(ha='center', va='center', rotation=90, fontsize=35, color='Black')
        plt.text(-1.4, 0.1, city, **text_kwargs)
        
        if 'Brus' in city:
            text_kwargs = dict(ha='center', va='center', rotation=70, fontsize=20, color='Black')
            plt.text(-1.05, 0.4, 'C4', **text_kwargs)

            text_kwargs = dict(ha='center', va='center', rotation=40, fontsize=20, color='Black')
            plt.text(-1, -0.5, 'C3', **text_kwargs)

            text_kwargs = dict(ha='center', va='center', rotation=0, fontsize=20, color='Black')
            plt.text(0.1, -1.1, 'C1', **text_kwargs)

            text_kwargs = dict(ha='center', va='center', rotation=-30, fontsize=20, color='Black')
            plt.text(0.45, 1., 'C2', **text_kwargs)

            text_kwargs = dict(ha='center', va='center', rotation=-40, fontsize=20, color='Black')
            plt.text(-0.6, 0.95, 'C5', **text_kwargs)

            text_kwargs = dict(ha='center', va='center', rotation=30, fontsize=20, color='Black')
            plt.text(1.05, 0.35, 'C7', **text_kwargs)

            text_kwargs = dict(ha='center', va='center', rotation=-40, fontsize=20, color='Black')
            plt.text(1, -0.47, 'C6', **text_kwargs)

        if 'Lis' in city:
            text_kwargs = dict(ha='center', va='center', rotation=70, fontsize=15, color='Black')
            plt.text(-1.05, 0.4, 'Residential\nArea', **text_kwargs)

            text_kwargs = dict(ha='center', va='center', rotation=40, fontsize=20, color='Black')
            plt.text(-0.75, -0.85, 'C1', **text_kwargs)


            text_kwargs = dict(ha='center', va='center', rotation=-30, fontsize=20, color='Black')
            plt.text(0.63, 0.91, 'C5', **text_kwargs)

            ext_kwargs = dict(ha='center', va='center', rotation=-30, fontsize=20, color='Black')
            plt.text(0.05, 1.1, 'C3', **text_kwargs)

            text_kwargs = dict(ha='center', va='center', rotation=-40, fontsize=20, color='Black')
            plt.text(-0.6, 0.92, 'C4', **text_kwargs)

            text_kwargs = dict(ha='center', va='center', rotation=30, fontsize=20, color='Black')
            plt.text(1.05, 0.35, 'C2', **text_kwargs)

            text_kwargs = dict(ha='center', va='center', rotation=-40, fontsize=20, color='Black')
            plt.text(0.81, -0.76, 'C6', **text_kwargs)


        plt.savefig('Results2l/2l10a'+city+'~'+phase+'~cord.png')
        plt.savefig('Results2l/2l10a'+city+'~'+phase+'~cord.eps')
        plt.clf()

        cmap = plt.cm.coolwarm

        
        plt.clf()
