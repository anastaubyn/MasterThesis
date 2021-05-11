# -*- coding: utf-8 -*-
"""
Created on Tue May 11 12:17:23 2021

@author: anacs

Explanatory Variable - Social Security Pensioners
"""

import pandas as pd
import numpy as np
import os, inspect
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

#Importing National Data
data = pd.read_csv(r'Data\ss_pensions.csv', delimiter=';')

#Eliminate Irrelevant Rows
data = data.iloc[10:]
data.drop(data.tail(25).index,inplace=True)
data.reset_index(drop=True, inplace=True)

#Removing Null Columns
data.dropna(axis=1, how='all', inplace=True)

#Creating Titles for Columns
data.columns = data.iloc[0]
data = data.iloc[1:]
data.rename(columns={"Anos": "Municipality"}, inplace=True)

#Keeping Only Municipality Data
data = data[data['Âmbito Geográfico'] == 'Município']
data.drop(data.columns[0], axis=1, inplace=True)

#Correcting Null Values
data.replace('-', np.NaN, inplace=True)

#Remove Unknown Characters
for i in data.columns[1:]:
    data[i] = data[i].str.replace(",", ".")
    data[i] = data[i].str.replace('[^\d\.]', "")
del i

#Convert Data to Numeric
data[data.columns[1:].tolist()] = data[data.columns[1:].tolist()].apply(pd.to_numeric)

#Turn Years into One Column
data = data.melt(id_vars=["Municipality"], var_name="Year", value_name="Value")
data['Year'] = data['Year'].apply(pd.to_numeric)

#Export as CSV
data.to_csv(r'Data\ss_pensions_final.csv', index=False)