# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:21:30 2021

@author: Ana Clara St. Aubyn

Portuguese National Domestic Violence Statistics

"""

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import os, inspect
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

#Import data
data = pd.read_csv(r'Data\national_treated.csv')

#Descriptive Statistics
data = data.transpose()

data.columns = data.iloc[0]
data = data.iloc[1:]
data = data.apply(pd.to_numeric)

descriptive = data.describe()

#Differences Between Years
data = data.reindex([str(i) for i in range(2019,2007,-1)])
data["dDVASA"] = data[data.columns[0]].diff(-1)
data["dTotal"] = data[data.columns[3]].diff(-1)

#Percentage of Total Change Caused by DVASA
data['%DVASA'] = data['dDVASA']*100/data['dTotal']

#Plot With Yearly Changes
data.index = data.index.astype(int)
data = data.reindex(list(range(2008,2020)))

plt.figure(figsize=(14,6))
ax = plt.subplot(111)
ax.bar(data.index - 0.4/2, data["dTotal"], width=0.4, label='Absolute Change in Total Occurrences',color='darkseagreen')
ax.bar(data.index + 0.4/2, data["dDVASA"], width=0.4, label='Absolute Change in DVASA Occurrences', color='dimgrey')
plt.axhline(y=0, color='lightgray', linewidth=1, linestyle='--')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.text(0.7, -0.15, 'Source: Direção-Geral da Política de Justiça (DGPJ)', transform=ax.transAxes)
ax.set_title('Absolute Change in Total and DVASA Occurrences', fontsize=16)
ax.set_xlabel('Year')
ax.set_ylabel('Number of Occurrences')
#ax.set_xticklabels(data.index)
plt.xticks(np.arange(2009, 2020, 1))
ax.legend(ncol=1)
plt.savefig(r'Images\absolute_changes.png')
