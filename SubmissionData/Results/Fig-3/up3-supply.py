from cProfile import label
import matplotlib.pyplot as plt
import random
import numpy as np
import json
import pandas as pd
import time

citiesAndSerivces = {'P1': {'SanFrancisco': ['Jump', 'Scoot'], 'Brussels': ['Jump', 'Lime', 'Circ'], 'Detroit': ['Spin', 'Lime', 'Bird'], 'Chicago': ['Jump', 'LyftScooter'], 'Madrid': ['Wind', 'Jump', 'Lime', 'Bird', 'Circ', 'Voi', 'Tier'], 'Paris': ['Wind', 'Jump', 'Lime', 'Bird', 'Voi', 'Tier'], 'TelAviv': ['Wind', 'Lime', 'Bird'], 'MexicoCity': ['Movo', 'Lime'], 'Zurich': ['Tier', 'Bird'], 'DC': ['Spin', 'Jump', 'LyftScooter', 'Lime', 'Bird', 'Skip'], 'Lisbon': ['Wind', 'Jump', 'Bird', 'Circ', 'Voi', 'Tier']}, 'P2': {'SanFrancisco': ['Lime', 'Bird'], 'Brussels': ['Lime', 'Circ'], 'Detroit': ['Bird'], 'Chicago': ['LyftScooter'], 'Madrid': ['Wind', 'Lime', 'Bird', 'Circ', 'Voi', 'Tier'], 'Paris': ['Wind', 'Lime', 'Bird', 'Voi', 'Tier'], 'TelAviv': ['Wind', 'Lime', 'Bird'], 'MexicoCity': ['Movo', 'Lime'], 'Zurich': ['Tier', 'Bird'], 'DC': ['Spin', 'LyftScooter', 'Lime', 'Bird', 'Skip'], 'Lisbon': ['Wind', 'Lime', 'Bird', 'Circ', 'Voi', 'Tier']}}



cities = ['DC', 'Paris', 'Brussels', 'Lisbon', 'Madrid', 'MexicoCity', 'SanFrancisco', 'TelAviv', 'Zurich', 'Detroit', 'Chicago']

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

cities = cities[::-1]

phases = ['P1', 'P2']
x = []
totalServices = [ 'Bird', 'Circ', 'Jump', 'Lime', 'LyftScooter', 'Movo', 'Scoot', 'Skip', 'Spin', 'Tier', 'Voi', 'Wind']

colors = [(0.9554474166212361, 0.7459731394920444, 0.0026170137322456544), (0.4142129200649052, 0.42555039949753826, 0.25225294260246656), (0.3296664605096191, 0.47834124362580377, 0.5605835286795703), (0.8556147726350499, 0.2727362473963153, 0.13140635340726659), (0.8210114253872471, 0.5345817538295028, 0.2944545678038304), (0.6354468639306041, 0.7675394278173934, 0.6239493801884614), (0.010005718214378678, 0.7244359665901243, 0.24160721313845768), (0.0024234876338239397, 0.2455766145923386, 0.016886799525566265), (0.9151364173731882, 0.7312665294075509, 0.9811423414138214), (0.5, 0, 0), (0.11317432893945689, 0.5631925853747284, 0.7442930586201215), (0.7827819162943063, 0.7563760713398012, 0.1032224970669354)]


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


width = 0.93 
df1 = pd.read_pickle('supplyP1Data')

tind = 0
titles = ['P1']
labels2 = ['CHI', 'DTW', 'ZRX', 'TLV', 'SFX', 'MXC', 'MAD', 'LXN', 'BXL', 'PAR', 'WDC']
for df in [df1]:
    fig, axes = plt.subplots(nrows=1, ncols=1)

    print(df)
    title = titles[tind]
    tind += 1
        
    df.plot.barh(ax=axes,stacked=True,width = width, color = colors)
    fig = plt.gcf()
    fig.set_size_inches(1.8*3, 1.25*3)

    props = dict( facecolor='white', alpha=0.5)

    axes.legend(loc='upper center', bbox_to_anchor=(0.65, 0.56),
            ncol=2, fancybox=True, shadow=True, fontsize=13)


    xticks = []
    xlabels = []
    for i in range(0,9,2):
        xticks.append(i*1000)
        if i != 0:
            xlabels.append(i*1000)
        else:
            xlabels.append('0')
    axes.set_xticks(xticks)
    axes.set_xticklabels(xlabels, fontsize=14)
    
    axes.set_yticklabels(labels2, fontsize=14, rotation=0)

    axes.set_xlim(0, 7100)


    axes.set_ylabel('Cities', fontsize=14)
    axes.set_xlabel('Average number of DESs per hour', fontsize=14)
    plt.subplots_adjust(left=0.16, bottom=0.14, right=0.99, top=0.99, wspace=0.01, hspace=-0)



    plt.savefig('Results2m2/'+title+'-1-Supply2Phases-2m2.eps')
    plt.savefig('Results2m2/'+title+'-1-Supply2Phases-2m2.png')

