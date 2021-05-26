# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 14:51:56 2021

@author: anacs

Explanatory Variable - Monthly Gain
"""
import pandas as pd
import numpy as np
import os, inspect
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

#Importing Data
data = pd.read_csv(r'Data\monthly_gain.csv', delimiter=';')

#Eliminate Irrelevant Rows
data = data.iloc[10:]
data.drop(data.tail(23).index,inplace=True)
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

#Remove Unknown Characters
for i in range(2009, 2019):
    data[str(i)] = data[str(i)].str.replace(",", ".")
    data[str(i)] = data[str(i)].str.replace(" ", "")
    data[str(i)] = data[str(i)].str.replace("[^A-Za-z1234567890'-. ]", "")
del i

#Correcting Null Values
data.replace('x', np.NaN, inplace=True)

#Convert Data to Numeric
data[data.columns[1:].tolist()] = data[data.columns[1:].tolist()].apply(pd.to_numeric)

#Including 2008 and 2019
data['2008'] = np.nan
data['2019'] = np.nan
cols = data.columns.tolist()
cols = cols[0:1] + cols[-2:-1] + cols[1:-2] + cols[-1:]
data = data[cols]
del cols

#Copying 2018 to 2019
data['2019'] = data['2018']

#Turn Years into One Column
data = data.melt(id_vars=["Municipality"], var_name="Year", value_name="Value")
data['Year'] = data['Year'].apply(pd.to_numeric)

#Export as CSV
data.to_csv(r'Data\monthly_gain_final.csv', index=False)
