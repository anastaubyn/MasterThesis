# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 11:05:28 2021

@author: anacs

Explanatory Variable - Education
"""

import pandas as pd
import numpy as np
import os, inspect
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

#Importing National Data
data = pd.read_csv(r'Data\education.csv', delimiter=';')

#Eliminate Irrelevant Rows
data = data.iloc[5:]

#Creating Titles for Columns
data.columns = data.iloc[0]
data = data.iloc[1:]
data.rename(columns={"ANO LETIVO": "Year"}, inplace=True)
data.rename(columns={"MUNICÍPIO": "Municipality"}, inplace=True)

#Removing Irrelevant Columns
data.drop(['NUT I - Continente', 'NUTS II de 2013', 'NUTS III de 2013', 'CÓDIGO DE MUNICÍPIO'], axis = 1, inplace=True)

#Dividing Datasets by Gender and Keeping only High School Data
data_women = data.iloc[:, 0:2].join(data.iloc[:,-1])
data_men = data.iloc[:, 0:2].join(data.iloc[:,13])
data = data.iloc[:, 0:2].join(data.iloc[:,7])

#Delete Rows With No Municipality
data = data.dropna(axis=0, subset=['Municipality'])
data_women = data_women.dropna(axis=0, subset=['Municipality'])
data_men = data_men.dropna(axis=0, subset=['Municipality'])

#Correcting Column Names
data.rename(columns={data.columns[2]: "GER"}, inplace=True)
data_women.rename(columns={data_women.columns[2]: "GER"}, inplace=True)
data_men.rename(columns={data_men.columns[2]: "GER"}, inplace=True)

#Correcting Null Values
data['GER'] = data['GER'].replace('-', np.nan)
data_women['GER'] = data_women['GER'].replace('-', np.nan)
data_men['GER'] = data_men['GER'].replace('-', np.nan)

#Keeping Only Relevant Years
years_to_keep = ['2008/09','2009/10', '2010/11', '2011/12', '2012/13', '2013/14', '2014/15',
                 '2015/16', '2016/17', '2017/18', '2018/19']
data = data[data.Year.isin(years_to_keep)]
data_women = data_women[data_women.Year.isin(years_to_keep)]
data_men = data_men[data_men.Year.isin(years_to_keep)]
del years_to_keep

#Correcting Years
dict_years = {'2008/09': 2009, '2009/10': 2010, '2010/11': 2011, '2011/12': 2012, 
              '2012/13': 2013, '2013/14': 2014, '2014/15': 2015, '2015/16': 2016,
              '2016/17': 2017, '2017/18': 2018, '2018/19': 2019}
data = data.replace({"Year": dict_years})
data_women = data_women.replace({"Year": dict_years})
data_men = data_men.replace({"Year": dict_years})
del dict_years

#Convert Data to Numeric
data['GER'] = data['GER'].str.replace(",", ".")
data['GER'] = data['GER'].apply(pd.to_numeric)
data_women['GER'] = data_women['GER'].str.replace(",", ".")
data_women['GER'] = data_women['GER'].apply(pd.to_numeric)
data_men['GER'] = data_men['GER'].str.replace(",", ".")
data_men['GER'] = data_men['GER'].apply(pd.to_numeric)

#Export as CSV
data.to_csv(r'Data\education_total_final.csv', index=False)
data_women.to_csv(r'Data\education_women_final.csv', index=False)
data_men.to_csv(r'Data\education_men_final.csv', index=False)
