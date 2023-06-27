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

geojsonLocation = '/home/hakhan/Google Drive/Scooter_Sheets/Dictionaries/Scripts/Neighborhood polygons/US_Cities_Zip_Codes_Data/'


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



otherWindowDelta = 5
windowDelta = 10
totalLocations = {}
totalCitiesNH = []

def kNN2DDens(xv, yv, resolution, neighbours, dim=2):
    """
    """
    # Create the tree
    tree = cKDTree(np.array([xv, yv]).T)
    # Find the closest nnmax-1 neighbors (first entry is the point itself)
    grid = np.mgrid[0:resolution, 0:resolution].T.reshape(resolution**2, dim)
    dists = tree.query(grid, neighbours)
    # Inverse of the sum of distances to each grid point.
    inv_sum_dists = 1. / dists[0].sum(1)

    # Reshape
    im = inv_sum_dists.reshape(resolution, resolution)
    return im



sizeServiceScatter = {}
sizeServiceScatter['Bird'] = 1
sizeServiceScatter['Circ'] = 1.1
sizeServiceScatter['Jump'] = 1.2
sizeServiceScatter['Lime'] = 1.3
sizeServiceScatter['LyftScooter'] = 1.4
sizeServiceScatter['Movo'] =  1.5
sizeServiceScatter['Scoot'] = 1.6
sizeServiceScatter['Skip'] = 1.7
sizeServiceScatter['Spin'] = 1.8
sizeServiceScatter['Tier'] = 1.9
sizeServiceScatter['Voi'] = 2
sizeServiceScatter['Wind'] = 2.1

import random
cities = ['TelAviv', 'Paris']
for city in cities:
    for phase in phases:
        censusTracts = {}
        fx = open('up4-'+city+'-geojson.txt', 'r')
        censusTracts = json.loads(fx.read())
        fx.close()

        censusTractsPolygonObj = []
        censusTractsList = []
        for i in range(0,len(censusTracts)):
            if 1: #len(censusTracts[i]) > 3:
                censusTractsPolygonObj.append(Polygon(censusTracts[i]))
                censusTractsList.append(censusTracts[i])
        services = list(cityAndServiceDict[phase][city])
        services.sort()
        nhDictionary = {}
        myWindow = 60
        dayDict = {}

        print(city)
        for i in range(0,int(1440/myWindow)):
            dayDict[str(i)] = {}
        fx = open('up4-'+city+'-dayDict.txt', 'r')
        dayDict = json.loads(fx.read())
        fx.close()
        coveredPercentage = []
        
        # time.sleep(100000)

        # plt.figure(figsize=(10,3))

        months1 = ['-06-']
        months2 = ['-03-', '-04-', '-05-']
        months = months2
        if phase == 'P1':
            months = months1
        for month in months:
            targetHour = -1
            targetDate = ''
            targetLocs = 0
            for i in range(0,int(1440/myWindow)):
                hour = str(i)
                for date in dayDict[hour].keys():
                    if month in date:
                        if len(dayDict[hour][date]['x']) > targetLocs:
                            targetLocs = len(dayDict[hour][date]['x'])
                            targetDate = date
                            targetHour = hour

            if targetDate != '':
                print(targetDate, targetLocs, targetHour)
                # time.sleep(1000)
                find = 0
                data = json.load(open('up4-'+city+'-citygeojson.txt','r'))

                # fig = plt.figure(figsize=(10,3))# create a figure to contain the plot elements
                fig = plt.gcf()
                fig.set_size_inches(1.8*3, 1.25*3)
                ax = fig.gca(xlabel="Longitude", ylabel="Latitude")
                # plt.clf()

                
                for feat in data["features"]:
                    geom = asShape(feat["geometry"])
                    x, y = geom.centroid.x, geom.centroid.y

                    ax.plot(x, y)
                    ax.add_patch(PolygonPatch(feat["geometry"], fc='whitesmoke', ec='black',
                            alpha=1, lw=0.15, ls='--', zorder=2))
                    find += 1

                

                xs = x = dayDict[targetHour][targetDate]['x']
                ys = y = dayDict[targetHour][targetDate]['y']

                nx = []
                ny = []
                colors = []

                prevTuples = {}
                csize = 1.5
                sizes = []
                sizeDict = {}
                for i in range(0, len(y)):
                    try:
                        v10 = prevTuples[str(x[i])+str(y[i])]
                        # sizes[i] +=0.01
                        x[i] *= random.uniform(0.99,1.01)
                        y[i] *= random.uniform(0.99,1.01)
                        i -=1
                    except:
                        nx.append(x[i])
                        ny.append(y[i])
                        prevTuples[str(x[i])+str(y[i])] = len(nx)-1
                        colors.append(totalServicesColors[dayDict[targetHour][targetDate]['service'][i]])
                        v10 = csize
                        try:
                            v10 =sizeDict[str(dayDict[targetHour][targetDate]['service'][i])]
                        except:
                            sizeDict[str(dayDict[targetHour][targetDate]['service'][i])] = csize
                            v10 = csize
                            csize += 0.1
                        sizes.append(v10)

                plt.scatter(ny,nx,color=colors, alpha=0.3, s=sizes, zorder=10)

                legend_elements = []
                for service in services:
                    legend_elements.append(Line2D([0], [0], marker='.', color=totalServicesColors[service], label=service,
                        markerfacecolor=totalServicesColors[service], markersize=13))

                lgfs = 22
                if 'Par' in city:
                    lgfs = 17
                plt.legend(handles=legend_elements, loc='upper right', fontsize=lgfs)
                city2 = city[:]
                if 'Tel' in city:
                	city2 = 'Tel Aviv'
                plt.title(city2, fontsize = 24)

                plt.ylabel("Latitude", fontsize=15)
                plt.xlabel("Longitude", fontsize=15)
                ax.tick_params(axis='both', which='major', labelsize=13)

                scriptName = '2la'

                plt.subplots_adjust(left=0.18,
                    bottom=0.15, 
                    right=0.97, 
                    top=0.9, 
                    wspace=0.05, 
                    hspace=0.01)
                
                plt.savefig('Results2l/'+scriptName+'~'+city+phase+month+'.pdf')
                plt.savefig('Results2l/'+scriptName+'~'+city+phase+month+'.png')
                # ax.clear
                plt.clf()
          
                # time.sleep(10000)
        break
    print('DONE WITH ', city)
    # time.sleep(10000)
