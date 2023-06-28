from calendar import c, week
from cgi import print_form
from operator import le
import os
import time

import json

import warnings
from scipy import stats
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

fx = open('up5-totalCats.txt', 'r')
totalCats = json.loads(fx.read())
fx.close()

cityDone = 0

import seaborn as sns; sns.set_theme()
import random

for phase in ['P1']:

    fx = open('up5-totalLocsCats.txt', 'r')
    totalLocsCats = json.loads(fx.read())
    fx.close()


    cityListSptial = {}
  
    fx = open('up5-cityListSptial.txt', 'r')
    cityListSptial = json.loads(fx.read())
    fx.close()


    cities = list(cityListSptial.keys())
    cities.sort()
    correfArr = []
    for i in range (0, len(cities)):
        correfArr.append([])
        for j in range(0,len(cities)):
            correfArr[i].append(0)
    vals = []
    for geo in ['Destination']:
        fx = open('up5-correfArr.txt', 'r')
        correfArr = json.loads(fx.read())
        fx.close()

        matrix = np.triu(np.ones_like(correfArr)) 
      
        weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        totalVals = []
        tv2 = []
       
        for i in range(0,7):
            for j in range(i,7):

                if i == j:
                    tv2.append(correfArr[i][j])
                totalVals.append(correfArr[i][j])

        print(np.average(totalVals))
        print(np.average(tv2))
        ax = sns.heatmap(correfArr, annot=True,square=False, annot_kws={"size":15}, vmin=0.4, vmax=1,cbar=False, cbar_kws={"shrink": .7})
   
        ax.set_yticklabels(weekdays ,rotation = 0)
        ax.set_xticklabels(weekdays ,rotation = 90)

        # plt.title
        ax.tick_params(axis='both', which='major', labelsize=14)
        plt.xlabel('Days of the week',fontsize=16)
        plt.subplots_adjust(left=0.15,
                bottom=0.2, 
                right=.98, 
                top=0.97, 
                wspace=0.05, 
                hspace=0.01)
        fig = plt.gcf()
        fig.set_size_inches(1.9*3, 1.25*3.4)

        plt.savefig('Results2l/2l4-'+phase+'-csCorrelation.png')
        plt.savefig('Results2l/2l4-'+phase+'-csCorrelation.eps')
        plt.clf()

    print('Phase', phase, 'Done', np.average(vals))
