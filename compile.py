# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:14:39 2018

@author: nicky
"""
import glob
import pandas as pd

indicators = {}
tables = []

for filename in glob.glob('*datapoints*.csv'):
    key = filename.partition('datapoints--')[2].partition('--')[0]
    data = pd.read_csv(filename)
    data = data[data.time > 1950]
    data = data[data.time <= 2018]
    data = data.pivot(index='geo', columns='time')
    data = data.stack(level=0)
    indicators[key] = data
    tables.append(data)

master = pd.concat(tables)
master = master.sort_index()
