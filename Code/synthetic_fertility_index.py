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

#Convert Data to Numeric
data[data.columns[1:].tolist()] = data[data.columns[1:].tolist()].apply(pd.to_numeric)

#Turn Years into One Column
data = data.melt(id_vars=["Municipality"], var_name="Year", value_name="Value")
data['Year'] = data['Year'].apply(pd.to_numeric)

#Export as CSV
data.to_csv(r'Data\synthetic_fertility_index_final.csv', index=False)
