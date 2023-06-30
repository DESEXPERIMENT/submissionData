from calendar import c
from operator import le
import os
import time

import geopy.distance

from matplotlib.lines import Line2D

import json
import copy
import warnings
from mercantile import neighbors
from scipy import stats
warnings.filterwarnings("ignore")
from datetime import datetime, timedelta
import pytz
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from scipy.stats import kendalltau
from scipy.stats import pearsonr
import numpy as np
from scipy.spatial.distance import cdist
from operator import itemgetter

import colorsys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from shapely.geometry import asShape # manipulating geometry
from descartes import PolygonPatch
from shapely.geometry import box, Polygon, MultiPolygon, GeometryCollection


thresholdGlobal = 0.007

def katana(geometry, threshold, count=0):
    """Split a Polygon into two parts across it's shortest dimension"""
    bounds = geometry.bounds
    width = bounds[2] - bounds[0]
    height = bounds[3] - bounds[1]
    # print(width, height)
    # time.sleep(1000)
    if max(width, height) <= threshold or count == 250:
        # either the polygon is smaller than the threshold, or the maximum
        # number of recursions has been reached
        return [geometry]
    if height >= width:
        # split left to right
        a = box(bounds[0], bounds[1], bounds[2], bounds[1]+height/2)
        b = box(bounds[0], bounds[1]+height/2, bounds[2], bounds[3])
    else:
        # split top to bottom
        a = box(bounds[0], bounds[1], bounds[0]+width/2, bounds[3])
        b = box(bounds[0]+width/2, bounds[1], bounds[2], bounds[3])
    result = []
    for d in (a, b,):
        c = geometry.intersection(d)
        if not isinstance(c, GeometryCollection):
            c = [c]
        for e in c:
            if isinstance(e, (Polygon, MultiPolygon)):
                result.extend(katana(e, threshold, count+1))
    if count > 0:
        return result
    # convert multipart into singlepart
    final_result = []
    for g in result:
        if isinstance(g, MultiPolygon):
            final_result.extend(g)
        else:
            final_result.append(g)
    return final_result




geojsonLocation = '/home/hakhan/Google Drive/Scooter_Sheets/Dictionaries/Scripts/Neighborhood polygons/US_Cities_Zip_Codes_Data/'


def find_top_n_indices(data, top):
    temp = data[:]
    return sorted(range(len(temp)), key=lambda i: temp[i], reverse=False)[-top:]

rgb = []
for i in range(101):
    rgb.append(colorsys.hsv_to_rgb(i / 300., 1.0, 1.0))
    # print(i, [round(255*x) for x in rgb])

phases = ['P1', 'P2']

datesOfExperiment = { 'P1': [ '2019-07-02', '2019-10-22', '2019-07-10', '2019-07-12', '2019-08-11', '2019-08-14', '2019-08-26', '2019-07-25', '2019-08-02', '2019-10-28', '2019-09-11', '2019-10-09', '2019-10-29', '2019-08-09', '2019-07-23', '2019-06-18', '2019-10-17', '2019-09-18', '2019-10-12', '2019-09-02', '2019-06-27', '2019-07-21', '2019-09-30', '2019-08-10', '2019-07-22', '2019-08-08', '2019-08-19', '2019-10-21', '2019-06-23', '2019-10-02', '2019-07-05', '2019-08-16', '2019-07-04', '2019-10-07', '2019-08-15', '2019-07-24', '2019-07-06', '2019-09-03', '2019-07-17', '2019-08-17', '2019-09-08', '2019-10-19', '2019-06-28', '2019-07-14', '2019-07-01', '2019-07-13', '2019-08-03', '2019-06-25', '2019-08-04', '2019-07-27', '2019-10-08', '2019-06-22', '2019-06-26', '2019-09-29', '2019-08-07', '2019-08-30', '2019-07-16', '2019-06-30', '2019-07-08', '2019-10-01', '2019-10-14', '2019-10-18', '2019-08-05', '2019-08-25', '2019-09-25', '2019-06-20', '2019-07-15', '2019-07-18', '2019-06-29', '2019-07-07', '2019-10-25', '2019-07-20', '2019-08-29', '2019-09-16', '2019-07-28', '2019-08-20', '2019-10-04', '2019-09-12', '2019-09-15', '2019-07-19', '2019-08-12', '2019-10-05', '2019-07-29', '2019-10-13', '2019-07-11', '2019-09-17', '2019-10-10', '2019-06-19', '2019-08-21', '2019-09-09', '2019-09-27', '2019-06-24', '2019-09-28', '2019-10-20', '2019-09-14', '2019-10-16', '2019-09-01', '2019-09-13', '2019-07-30', '2019-10-15', '2019-09-10', '2019-09-04', '2019-07-09', '2019-09-07', '2019-09-05', '2019-06-21', '2019-09-06', '2019-10-03', '2019-09-26', '2019-10-24', '2019-10-23', '2019-08-23', '2019-07-26', '2019-10-11', '2019-10-06', '2019-10-30', '2019-08-31', '2019-08-27', '2019-08-13',  '2019-09-19', '2019-08-22' ], 'P2': [ '2021-05-03', '2021-05-15', '2021-05-06', '2021-04-27', '2021-04-08', '2021-03-27', '2021-03-24', '2021-03-23', '2021-05-10', '2021-04-04', '2021-05-08', '2021-04-18', '2021-05-13', '2021-04-20', '2021-04-16', '2021-04-24', '2021-04-23', '2021-04-06', '2021-05-04', '2021-05-09', '2021-04-11', '2021-03-12', '2021-05-07', '2021-04-10', '2021-04-14', '2021-04-28', '2021-03-22', '2021-04-12', '2021-04-02', '2021-05-16', '2021-04-09', '2021-05-14', '2021-04-17', '2021-04-22', '2021-03-13', '2021-04-19', '2021-04-25', '2021-03-25', '2021-04-30', '2021-05-05', '2021-04-07', '2021-04-29', '2021-05-02', '2021-04-13', '2021-04-01', '2021-05-11', '2021-03-26', '2021-04-21', '2021-03-31', '2021-04-15', '2021-03-29', '2021-04-03', '2021-04-26', '2021-05-01', '2021-03-30', '2021-04-05', '2021-03-28', '2021-05-12' ] }


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


def get_color(red_to_green):
    assert 0 <= red_to_green <= 1
    # in HSV, red is 0 deg and green is 120 deg (out of 360);
    # divide red_to_green with 3 to map [0, 1] to [0, 1./3.]
    hue = red_to_green / 3.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return map(lambda x: int(255 * x), (r, g, b))


otherWindowDelta = 5
windowDelta = 60
totalLocations = {}
totalCitiesNH = []
scooterDistWeight = 0.2
# skipList = {'P1':['Lisbon', 'Detroit', 'DC', 'Chicago', 'Brussels'], 'P2':[]} #{'P1':['Brussels']}
skipList = {'P1':[], 'P2':[]} #{'P1':['Brussels']}





totalCityColors = {}
totalCityColors['Brussels'] = (0.9554474166212361, 0.7459731394920444, 0.0026170137322456544)
totalCityColors['Chicago'] = (0.4142129200649052, 0.42555039949753826, 0.25225294260246656)
totalCityColors['DC'] = (0.3296664605096191, 0.47834124362580377, 0.5605835286795703)
totalCityColors['Detroit'] = (0.8556147726350499, 0.2727362473963153, 0.13140635340726659)
totalCityColors['Lisbon'] = (0.8210114253872471, 0.5345817538295028, 0.2944545678038304)
totalCityColors['Madrid'] =  (0.6354468639306041, 0.7675394278173934, 0.6239493801884614)
totalCityColors['MexicoCity'] = (0.010005718214378678, 0.7244359665901243, 0.24160721313845768)
totalCityColors['Paris'] = (0.0024234876338239397, 0.2455766145923386, 0.016886799525566265)
totalCityColors['SanFrancisco'] = (0.9151364173731882, 0.7312665294075509, 0.9811423414138214)
totalCityColors['TelAviv'] = (0.5, 0, 0)
totalCityColors['Zurich'] = (0.11317432893945689, 0.5631925853747284, 0.7442930586201215)


mapCities = {}
mapCities['DC'] = 'WDC'
mapCities['Paris'] = 'PAR'
mapCities['Brussels'] = 'BXL'
mapCities['Lisbon'] = 'LXN'
mapCities['Madrid'] = 'MAD'
mapCities['MexicoCity'] = 'MXC'
mapCities['SanFrancisco'] = 'SFX'
mapCities['TelAviv'] = 'TLV'
mapCities['Zurich'] = 'ZRX'
mapCities['Detroit'] = 'DTW'
mapCities['Chicago'] = 'CHI'
fig, ax1 = plt.subplots(1, 1, figsize=(7.5,5.4))

legenLines = []
legenLinesLabels = []
for phase in ['P1']:
    ax = ax1

    cities = list(cityAndServiceDict[phase])
    cities.sort()
    
    print('PHASE          :         ', phase)
    for city in cities:
        fx = open('up9-scriptData-'+city+phase+'.txt','r')
        dataContent = json.loads(fx.read())
        fx.close()

    
        dataContent = json.loads(dataContent)
        line, = ax.plot(dataContent['uni'],  color=totalCityColors[city], label='Line y', lw=2)
        line2,= ax.plot(dataContent['transits'], color=totalCityColors[city],linestyle= 'dashed', label='Line y', lw=2)

        if phase == 'P1':
            legenLines.append(line)
            legenLinesLabels.append(mapCities[city])

x = [0,5,10,15,20,25]
labels = [0, 0.05,0.1,0.15,0.2,0.25]
ax1.set_xticks(x, labels, fontsize=11)
ax1.set_ylabel("Number of DESs", fontsize=20, labelpad=-1)
ax1.set_xlabel("Distance (miles)", fontsize=19)

ax1.xaxis.set_label_coords(0.5, -0.075)


custom_lines = [Line2D([0], [0], color='black', lw=0.5),
                line2]

custom_lines[0].set_color(custom_lines[1].get_color())
print(legenLinesLabels)
l1 = ax1.legend(legenLines, legenLinesLabels, loc='center left', bbox_to_anchor=(0, 0.77), ncol=3, fontsize=20)
ax1.legend(custom_lines, ['Edu. Facitilies', 'Public Transport'], fontsize=20, bbox_to_anchor=(0.5,-0.3), loc='lower center', ncol=2)
plt.gca().add_artist(l1)

plt.subplots_adjust(left=0.1,
                    bottom=0.2, 
                    right=0.98, 
                    top=0.98, 
                    wspace=0.1, 
                    hspace=0.4)
ax.tick_params(axis='both', which='major', labelsize=20)


scriptName = '2l11'
plt.savefig('Results2l/'+scriptName+'-CDFuniTransit.eps')
plt.savefig('Results2l/'+scriptName+'-CDFuniTransit.png')


