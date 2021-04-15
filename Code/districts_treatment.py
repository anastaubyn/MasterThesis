# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:21:08 2021

@author: Ana Clara St. Aubyn

Data Treatment - Domestic Violence Districts Portugal

"""

import pandas as pd
import numpy as np
import os, inspect
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

#Importing Data
data = pd.read_csv(r'Data\Districts.csv', delimiter=';')

#Eliminate Irrelevant Rows
data = data.iloc[5:]
data.reset_index(drop=True, inplace=True)

#Removing Null and Unnecessary Columns
data.dropna(axis=1, how='all', inplace=True)
data.drop([data.columns[0]], axis=1, inplace=True)

#Creating Titles for Columns
data.columns = data.iloc[0]
data = data.iloc[1:]
data.rename(columns={data.columns[0]: "Crime", "District": "District"}, inplace=True)

#Replacing Nulls in Crime Column
data['Crime'] = data['Crime'].fillna(method='ffill')

#Removing Unknown Characters from District and Crime
data['Crime'] = data['Crime'].str.replace("[^A-Za-z1234567890'-. ]", "")
data['District'] = data['District'].str.replace("[^A-Za-z1234567890'-. ]", "")
data['District'] = data['District'].str.replace("vora", "Evora")
data['District'] = data['District'].str.replace("Bragana", "Braganca")
data['District'] = data['District'].str.replace("Santarm", "Santarem")
data['District'] = data['District'].str.replace("Setbal", "Setubal")
data['District'] = data['District'].str.replace("So Miguel", "Sao Miguel")
data['District'] = data['District'].str.replace("So Jorge", "Sao Jorge")

#Keeping Only Domestic Violence
data = data[data['Crime'].str.contains('violncia domstica') | data['Crime'].str.contains('Violncia domstica')]

#Correct Nulls
data = data.replace('..', np.nan)
data.dropna(axis=1, how='all', inplace=True)
data ['District'] = data['District'].replace(np.nan, 'Nacional')

#Correct Crime Column
data['Crime'] = data['Crime'].replace('Violncia domstica cnjugeanlogo', 'Violencia Domestica Conjuge ou Analogo')
data['Crime'] = data['Crime'].replace('Violncia domstica contra menores', 'Violencia Domestica Menores')
data['Crime'] = data['Crime'].replace('Outros violncia domstica', 'Outros Violencia Domestica')

#Sort Years in Ascending Order
data = data[data.columns[::-1]]
cols = data.columns.tolist()
cols = cols[-2:] + cols[:-2]
data = data[cols]
del cols

#Removing Total Rows
data = data[~(data['Crime'].str.contains('Total'))]

#Exportar as CSV
data.to_csv(r'Data\districts_treated.csv', index=False)

