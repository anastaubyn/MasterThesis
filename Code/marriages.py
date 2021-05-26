# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 10:56:42 2021

@author: anacs

Explanatory Variable? - Marriages
"""

import pandas as pd
import numpy as np
import os, inspect
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

#Importing Data
data = pd.read_csv(r'Data\marriages.csv', delimiter=';')

#Eliminate Irrelevant Rows
data = data.iloc[10:]
data.drop(data.tail(23).index,inplace=True)
data.reset_index(drop=True, inplace=True)

#Creating Titles for Columns
data.columns = data.iloc[0]
data = data.iloc[1:]
data.rename(columns={"Anos": "Municipality"}, inplace=True)
data.columns.values[3] = '2010'

#Keeping Only Municipality and National Data
marriages_national = data[data['Âmbito Geográfico'] == 'NUTS 2013']
data = data[data['Âmbito Geográfico'] == 'Município']

#Removing Null and Unnecessary Columns
data.dropna(axis=1, how='all', inplace=True)
data.drop(data.columns[0], axis=1, inplace=True)
marriages_national.dropna(axis=1, how='all', inplace=True)
marriages_national.drop(marriages_national.columns[0], axis=1, inplace=True)

#Remove Unknown Characters
for i in range(2009, 2020):
    data[str(i)] = data[str(i)].str.replace(" ", "")
    data[str(i)] = data[str(i)].str.replace("[^A-Za-z1234567890'-. ]", "")

for i in range(2009, 2020):
    marriages_national[str(i)] = marriages_national[str(i)].str.replace(" ", "")
    marriages_national[str(i)] = marriages_national[str(i)].str.replace("[^A-Za-z1234567890'-. ]", "")
del i

#Convert Data to Numeric
marriages_national[marriages_national.columns[1:].tolist()] = marriages_national[marriages_national.columns[1:].tolist()].apply(pd.to_numeric)
data[data.columns[1:].tolist()] = data[data.columns[1:].tolist()].apply(pd.to_numeric)

#Including 2008
data['2008'] = np.nan
cols = data.columns.tolist()
cols = cols[0:1] + cols[-1:] + cols[1:]
data = data[cols]
del cols

#Undo effects of series break (2010) by removing values for 2009
data['2009'] = data['2010']

#Turn Years into One Column
data = data.melt(id_vars=["Municipality"], var_name="Year", value_name="Value")
data['Year'] = data['Year'].apply(pd.to_numeric)
marriages_national = marriages_national.melt(id_vars=["Municipality"], var_name="Year", value_name="Value")
marriages_national['Year'] = marriages_national['Year'].apply(pd.to_numeric)

#Export as CSV
data.to_csv(r'Data\marriages_final.csv', index=False)

#Import DVASA National Data
dvasa = pd.read_csv(r'Data\national_treated.csv')
dvasa = dvasa.head(1)
dvasa['Crime'] = 'Portugal'
dvasa = dvasa.melt(id_vars=['Crime'], var_name="Year", value_name="Value")
dvasa.columns.values[0] = 'Municipality'
dvasa['Year'] = dvasa['Year'].apply(pd.to_numeric)
dvasa = dvasa[dvasa['Year']!=2008]

#Changing Name of Columns
dvasa.rename(columns={"Value": "DVASA"}, inplace=True)
marriages_national.rename(columns={"Value": "Marriages"}, inplace=True)

#Merging marriages and dvasa
dvasa = dvasa.merge(marriages_national, on=["Municipality", "Year"], how = 'inner')

#Standardizing by Population
pop = pd.read_csv(r'Data\population_national_final.csv')
pop.rename(columns={"Value": "Population"}, inplace=True)
dvasa = dvasa.merge(pop, on=["Municipality", "Year"], how = 'inner')
dvasa['Population'] = dvasa['Population']/100
dvasa['DVASA'] = dvasa['DVASA'] / dvasa['Population']
dvasa['Marriages'] = dvasa['Marriages'] / dvasa['Population']

#Plotting DVASA and Marriages
import matplotlib.pyplot as plt
plt.figure(figsize=(14,6))
ax = plt.subplot(111)
ax.plot(dvasa['Year'], dvasa["DVASA"], linewidth=4, label='DVASA Occurrences',color='darkseagreen')
ax.plot(dvasa['Year'], dvasa["Marriages"], linewidth=4, label='Marriages', color='dimgrey')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.text(0.9, -0.15, 'Source: Pordata', transform=ax.transAxes)
ax.set_title('Are Marriages and Domestic Violence Occurrences Related?', fontsize=16)
ax.set_xlabel('Year')
ax.set_ylabel('Number by 100 Inhabitants')
ax.legend(ncol=1)
plt.savefig(r'Images\marriages_DVASA')


