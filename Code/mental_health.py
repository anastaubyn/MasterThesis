# -*- coding: utf-8 -*-
"""
Created on Mon May 10 18:58:06 2021

@author: anacs

Explanatory Variable - Psychiatrists and Total Doctors
"""

import pandas as pd
import numpy as np
import os, inspect
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

#Importing National Data
data = pd.read_csv(r'Data\mental_health.csv', delimiter=';')

#Eliminate Irrelevant Rows
data = data.iloc[10:]
data.drop(data.tail(23).index,inplace=True)
data.reset_index(drop=True, inplace=True)

#Removing Null Columns
data.dropna(axis=1, how='all', inplace=True)

#Creating Titles for Columns
data.columns = ['Âmbito Geográfico', 'Municipality'] + [str(i) for i in range(2009,2020)] + [f'{i}P' for i in range(2009, 2020)]
data = data.iloc[1:]

#Keeping Only Municipality Data
data = data[data['Âmbito Geográfico'] == 'Município']
data.drop(data.columns[0], axis=1, inplace=True)

#Remove Unknown Characters
for i in data.columns[1:]:
    data[i] = data[i].str.replace(" ", "")
    data[i] = data[i].str.replace("[^A-Za-z1234567890'-. ]", "")
del i

#Convert Data to Numeric
data[data.columns[1:].tolist()] = data[data.columns[1:].tolist()].apply(pd.to_numeric)

#Get Total doctors
total = data[['Municipality'] + [str(i) for i in range(2009,2020)]]
total = total.melt(id_vars=["Municipality"], var_name="Year", value_name="Value")
total['Year'] = total['Year'].apply(pd.to_numeric)
total.to_csv(r'Data\total_doctors_final.csv', index=False)

#Calculating Percentage of Mental Health Doctors
for i in range(2009,2020):
    data[str(i)] = data[str(i)+'P'] * 100 / data[str(i)]

#Removing Unnecessary Columns
data = data[['Municipality'] + [str(i) for i in range(2009,2020)]]

#Turn Years into One Column
data = data.melt(id_vars=["Municipality"], var_name="Year", value_name="Value")
data['Year'] = data['Year'].apply(pd.to_numeric)

#Export as CSV
data.to_csv(r'Data\mental_health_final.csv', index=False)
