# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 15:08:17 2021

@author: anacs

Explanatory Variable - Unemployment
"""

import pandas as pd
import numpy as np
import os, inspect
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

#Importing National Data
data = pd.read_csv(r'Data\unemployment.csv', delimiter=';')

#Eliminate Irrelevant Rows
data = data.iloc[10:]
data.drop(data.tail(23).index,inplace=True)
data.reset_index(drop=True, inplace=True)

#Removing Null Columns
data.dropna(axis=1, how='all', inplace=True)

#Creating Titles for Columns
data.columns = ['Âmbito Geográfico', 'Municipality'] + [str(i) for i in range(2009,2020)] + [f'{i}M' for i in range(2009, 2020)] + [f'{i}F' for i in range(2009, 2020)]
data = data.iloc[1:]

#Keeping Only Municipality Data
data = data[data['Âmbito Geográfico'] == 'Município']
data.drop(data.columns[0], axis=1, inplace=True)

#Correcting Null Values
data.replace('x', np.NaN, inplace=True)

#Remove Unknown Characters
for i in data.columns[1:]:
    data[i] = data[i].str.replace(",", ".")
    data[i] = data[i].str.replace(" ", "")
    data[i] = data[i].str.replace("[^A-Za-z1234567890'-. ]", "")
del i

#Convert Data to Numeric
data[data.columns[1:].tolist()] = data[data.columns[1:].tolist()].apply(pd.to_numeric)

#Separating Datasets for Total, Male and Female Unemployment
male = data[['Municipality'] + [f'{i}M' for i in range(2009, 2020)]].copy()
male.columns = ['Municipality'] + [str(i) for i in range(2009, 2020)]
male['2008'] = np.nan
cols = male.columns.tolist()
cols = cols[0:1] + cols[-1:] + cols[1:]
male = male[cols]
female = data[['Municipality'] + [f'{i}F' for i in range(2009, 2020)]].copy()
female.columns = ['Municipality'] + [str(i) for i in range(2009, 2020)]
female['2008'] = np.nan
female = female[cols]
total = data[['Municipality'] + [str(i) for i in range(2009, 2020)]]
total['2008'] = np.nan
total = total[cols]
del cols

#Turn Years into One Column
male = male.melt(id_vars=["Municipality"], var_name="Year", value_name="Value")
male['Year'] = male['Year'].apply(pd.to_numeric)
female = female.melt(id_vars=["Municipality"], var_name="Year", value_name="Value")
female['Year'] = female['Year'].apply(pd.to_numeric)
total = total.melt(id_vars=["Municipality"], var_name="Year", value_name="Value")
total['Year'] = total['Year'].apply(pd.to_numeric)

#Export as CSV
male.to_csv(r'Data\unemployment_male_final.csv', index=False)
female.to_csv(r'Data\unemployment_female_final.csv', index=False)
total.to_csv(r'Data\unemployment_total_final.csv', index=False)
