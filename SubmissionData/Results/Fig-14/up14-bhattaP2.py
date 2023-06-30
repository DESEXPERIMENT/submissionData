from calendar import c
from operator import le
import os
import time

import json

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
import dictances
import math

cityAndServiceDict = {'P1': {'SanFrancisco': ['Scoot', 'Jump'], 'Brussels': ['Lime', 'Circ', 'Jump'], 'Detroit': ['Spin', 'Bird', 'Lime'], 'Chicago': ['LyftScooter', 'Jump'], 'Madrid': ['Voi', 'Bird', 'Wind', 'Lime', 'Circ', 'Jump', 'Tier'], 'Paris': ['Bird', 'Voi', 'Wind', 'Lime', 'Jump', 'Tier'], 'TelAviv': ['Bird', 'Wind', 'Lime'], 'MexicoCity': ['Movo', 'Lime'], 'Zurich': ['Bird', 'Tier'], 'DC': ['Spin', 'LyftScooter', 'Skip', 'Bird', 'Lime', 'Jump'], 'Lisbon': ['Voi', 'Bird', 'Circ', 'Wind', 'Jump', 'Tier']}, 'P2': {'SanFrancisco': ['Bird', 'Lime'], 'Brussels': ['Circ', 'Lime'], 'Detroit': ['Bird'], 'Chicago': ['LyftScooter'], 'Madrid': ['Bird', 'Lime'], 'Paris': ['Tier', 'Bird', 'Lime', 'Voi'], 'TelAviv': ['Bird', 'Lime', 'Wind'], 'MexicoCity': ['Movo', 'Lime'], 'Zurich': ['Tier', 'Bird'], 'DC': ['LyftScooter', 'Bird', 'Lime', 'Spin'], 'Lisbon': ['Bird', 'Lime']}}


phases = ['P1']

phase = 'P1'

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd



fx = open('up14-data1.txt','r')
box_plot_data = json.loads(fx.read())
fx.close()


fx = open('up14-data2.txt','r')
totalVals = json.loads(fx.read())
fx.close()



print(np.average(totalVals))
fig, ax = plt.subplots()

# print(box_plot_data)
xticks = []
citiesShort = ['BXL', 'CHI', 'WDC', 'DTW', 'LXN', 'MAD', 'MXC', 'PAR', 'SFX', 'TLV', 'ZRX']


plt.yticks([0,0.2,0.4,0.6,0.8,1], ['0','0.2','0.4','0.6','0.8','1'],  fontsize=14)

plt.ylabel('Value of Bhattacharya Coeff.', labelpad=5,  fontsize=20)
plt.ylim([0,1.01])

xlabels = []
cities = list(cityAndServiceDict[phase])

for i in range(0, len(cities)):
    xlabels.append(cities[i])

for i in range(0, len(xlabels)):
    xticks.append(i+1)


plt.boxplot(box_plot_data, showfliers=False, boxprops= dict(linewidth=2.0, color='black'),  whiskerprops=dict(linestyle='-',linewidth=2.0, color='black'))


plt.xticks(xticks, citiesShort, fontsize=12,  rotation=90)
plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)


ax.tick_params(axis='both', which='major', labelsize=19)
ax.tick_params(axis='x', which='major', labelsize=20)

# ax.tick_params(axis='y', which='major', rotate=40)

plt.subplots_adjust(left=0.15,
                    bottom=0.16, 
                    right=0.95, 
                    top=0.97, 
                    wspace=0.05, 
                    hspace=0.01)

plt.savefig('Results2l/2l5d-P2-bhatta.png')
plt.savefig('Results2l/2l5d-P2-bhatta.eps')