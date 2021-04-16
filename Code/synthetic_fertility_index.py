# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 16:13:50 2021

@author: anacs

Explanatory Variable - Synthetic Fertility Index
"""

import pandas as pd
import numpy as np
import os, inspect
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

#Importing National Data
data = pd.read_csv(r'Data\synthetic_fertility_index.csv', delimiter=';')

#Eliminate Irrelevant Rows
data = data.iloc[10:]
data.drop(data.tail(24).index,inplace=True)
data.reset_index(drop=True, inplace=True)

#Creating Titles for Columns
data.columns = data.iloc[0]
data = data.iloc[1:]
data.rename(columns={"Anos": "Municipality"}, inplace=True)

#Keeping Only Municipality Data
data = data[data['Âmbito Geográfico'] == 'Município']

#Removing Null and Unnecessary Columns
data.dropna(axis=1, how='all', inplace=True)
data.drop(data.columns[0], axis=1, inplace=True)

#Including 2008
data['2008'] = np.nan
cols = data.columns.tolist()
cols = cols[0:1] + cols[-1:] + cols[1:-1]
data = data[cols]
del cols

#Remove Unknown Characters
for i in range(2009, 2020):
    data[str(i)] = data[str(i)].str.replace("[^A-Za-z1234567890'-. ]", "")
    data[str(i)] = data[str(i)].str.replace(",", ".")
    data[str(i)] = data[str(i)].str.replace("Rv ", "")
del i

#Convert Data to Numeric
data[data.columns[1:].tolist()] = data[data.columns[1:].tolist()].apply(pd.to_numeric)

#Check for Evolution on the National Level
total_mun = data.sum(numeric_only=True, axis=0).tolist()
total_mun = [round(x / 308, 2) for x in total_mun]

import matplotlib.pyplot as plt
plt.figure(figsize=(14,6))
ax = plt.subplot(111)
ax.plot(list(range(2009, 2020)), total_mun[1:], color='darkseagreen')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.text(0.31, -0.15, 'Source: Pordata at https://www.pordata.pt/Municipios/%c3%8dndice+sint%c3%a9tico+de+fecundidade-739', transform=ax.transAxes)
ax.set_title('Synthetic Fertility Index - National', fontsize=16)
ax.set_xlabel('Year')
ax.set_ylabel('Average Number of Children Born for Each Woman in Fertile Age')
plt.savefig(r'Images\synthetic_fertility.png')


#Turn Years into One Column
data = data.melt(id_vars=["Municipality"], var_name="Year", value_name="Value")
data['Year'] = data['Year'].apply(pd.to_numeric)

#Export as CSV
data.to_csv(r'Data\synthetic_fertility_index_final.csv', index=False)
