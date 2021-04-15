# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:21:08 2021

@author: Ana Clara St. Aubyn

Data Treatment Domestic Violence National Portugal

"""

import pandas as pd
import numpy as np
import os, inspect
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

#Importing National Data
data = pd.read_csv(r'Data\National.csv', delimiter=';')

#Eliminate Irrelevant Rows
data = data.iloc[5:]
data.reset_index(drop=True, inplace=True)

#Creating Titles for Columns
data.columns = data.iloc[0]
data = data.iloc[1:]

#Removing Null and Unnecessary Columns
data.dropna(axis=1, how='all', inplace=True)
data.drop([data.columns[0], data.columns[1]], axis=1, inplace=True)
data.rename(columns={data.columns[0]: "Crime"}, inplace=True)

#Eliminate Rows Referring to Other Type 2 Crimes
data = data[data[data.columns[0]].notna()]

#Removing Unknown Characters from Crime
data['Crime'] = data['Crime'].str.replace("[^A-Za-z1234567890'-. ]", "")

#Keeping Only Domestic Violence
data = data[data['Crime'].str.contains('violncia domstica') | data['Crime'].str.contains('Violncia domstica')]

#Remove Years With No Data
data = data.replace('..', np.nan)
data.dropna(axis=1, how='all', inplace=True)

#Sort Years in Ascending Order
data = data[data.columns[::-1]]
cols = data.columns.tolist()
cols = cols[-1:] + cols[:-1]
data = data[cols]
del cols

#Create a Total Row
data[data.columns[1:].tolist()] = data[data.columns[1:].tolist()].apply(lambda x: x.str.replace(' ',''))
data[data.columns[1:].tolist()] = data[data.columns[1:].tolist()].apply(pd.to_numeric)
data.loc['Total']= data.sum(numeric_only=True, axis=0)
data.reset_index(drop=True, inplace=True)

#Correct Crime Column
data['Crime'] = ['Violencia Domestica Conjuge ou Analogo', 'Violencia Domestica Menores', 'Outros Violencia Domestica', 'Total']

#Export as CSV
data.to_csv(r'Data\national_treated.csv', index=False)

