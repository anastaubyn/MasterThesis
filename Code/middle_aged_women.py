# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 14:12:15 2021

@author: anacs

Explanatory Variable - Middle-Aged Women
"""
import pandas as pd
import numpy as np
import os, inspect
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

#Importing Data
data1 = pd.read_csv(r'Data\middle_aged_women_1.csv', delimiter=';')
data2 = pd.read_csv(r'Data\middle_aged_women_2.csv', delimiter=';')

#Eliminate Irrelevant Rows
data1 = data1.iloc[10:]
data2 = data2.iloc[10:]
data1.drop(data1.tail(23).index,inplace=True)
data2.drop(data2.tail(23).index,inplace=True)
data1.reset_index(drop=True, inplace=True)
data2.reset_index(drop=True, inplace=True)

#Removing Null Columns
data1.dropna(axis=1, how='all', inplace=True)
data2.dropna(axis=1, how='all', inplace=True)

#Creating Titles for Columns
data1.columns = data1.iloc[0]
data1 = data1.iloc[1:]
data1.rename(columns={"Anos": "Municipality"}, inplace=True)
data2.columns = data2.iloc[0]
data2 = data2.iloc[1:]
data2.rename(columns={"Anos": "Municipality"}, inplace=True)

#Keeping Only Municipality Data
data1 = data1[data1['Âmbito Geográfico'] == 'Município']
data1.drop(data1.columns[0], axis=1, inplace=True)
data2 = data2[data2['Âmbito Geográfico'] == 'Município']
data2.drop(data2.columns[0], axis=1, inplace=True)

#Remove Unknown Characters
for i in range(1, len(list(data1.columns))):
    data1.iloc[:,i] = data1.iloc[:,i].str.replace(" ", "")
    data1.iloc[:,i] = data1.iloc[:,i].str.replace("[^A-Za-z1234567890'-. ]", "")
del i
for i in range(1, len(list(data2.columns))):
    data2.iloc[:,i] = data2.iloc[:,i].str.replace(" ", "")
    data2.iloc[:,i] = data2.iloc[:,i].str.replace("[^A-Za-z1234567890'-. ]", "")
del i

#Convert Data to Numeric
data1.iloc[:,1:] = data1.iloc[:,1:].apply(pd.to_numeric)
data2.iloc[:,1:] = data2.iloc[:,1:].apply(pd.to_numeric)

#Summing Values for Same Year
data1 = data1.groupby(data1.columns, axis=1).sum()
data2 = data2.groupby(data2.columns, axis=1).sum()

#Merging data1 and data2
data = data1.merge(data2, on=["Municipality"], how = 'inner')
del data1, data2

#Including 2008
data['2008'] = np.nan
cols = data.columns.tolist()
cols = cols[9:10] + cols[-1:] + cols[0:9] + cols[-3:-1]
data = data[cols]
del cols

#Turn Years into One Column
data = data.melt(id_vars=["Municipality"], var_name="Year", value_name="Value")
data['Year'] = data['Year'].apply(pd.to_numeric)

#Export as CSV
data.to_csv(r'Data\middle_aged_women_final.csv', index=False)
