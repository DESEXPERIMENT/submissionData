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


utilDailyHourlyDict = {}

import seaborn as sns; sns.set_theme()
weekdays = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdaysShort = ['Mon','Tue','Wed','Thu', 'Fri', 'Sat', 'Su']


fx = open('up11-data2.txt','r')
utilDailyHourlyDict = json.loads(fx.read())
fx.close()

totalMax = 0
maxVal = 336
for city in utilDailyHourlyDict:
    print(city)
    for phase in ['P1']:#utilDailyHourlyDict[city]:
        if 'Mexico' in city and 'P2' in phase:
            pass
        else:
            utilData = []
            if 'San' in city:
                sns.set(rc = {'figure.figsize':(5*0.85,3.1*1.2)})
            else:
                sns.set(rc = {'figure.figsize':(6*0.85,3.1*1.2)})


            for day in weekdays:
                utilData.append(utilDailyHourlyDict[city][phase][day])

            grid_kws = {"height_ratios": (.9, .05), "hspace": .3}
            

            if 'Tel' not in city:
                ax = sns.heatmap(utilData, cbar=False, linewidths=0, xticklabels=2, vmax=maxVal, vmin=0)
            else:
                ax = sns.heatmap(utilData, cbar=True, linewidths=0, xticklabels=2, vmax=maxVal, vmin=0)
            totalMax = max(maxVal, totalMax)
            if 'Bru' in city:
                ax.set_yticklabels(weekdaysShort ,rotation = 0, fontsize=15)
            else:
                ax.set_yticklabels([])
            if 'SanF' in city:
                ax.set_title('San Francisco'+'-'+phase, fontsize=20)
            else:
                ax.set_title(city+'-'+phase, fontsize=18)

            ax.xaxis.set_tick_params(labelsize=17)


            # set the spacing between subplots
            if 'San' in city :
                plt.subplots_adjust(left=0.0,
                    bottom=0.17, 
                    right=0.99, 
                    top=0.92, 
                    wspace=0.05, 
                    hspace=0.01)
            elif 'Tel' in city:
                plt.subplots_adjust(left=0,
                    bottom=0.17, 
                    right=1.04, 
                    top=0.92, 
                    wspace=0.05, 
                    hspace=0.01)
            else:
                plt.subplots_adjust(left=0.15,
                        bottom=0.17, 
                        right=0.99, 
                        top=0.92, 
                        wspace=0.05, 
                        hspace=0.01)

            if 'Bru' in city:
                plt.ylabel("Day of the Week", fontsize=16, labelpad=-1)
            plt.xlabel("Hour of the Day", fontsize=16)

            plt.savefig('Results2l/2l8-'+city+'-hourly.eps')
            plt.savefig('Results2l/2l8-'+city+'-hourly.png')



            plt.clf()
            # print('Sleeping')
            # time.sleep(1000)



print(totalMax)