# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 15:04:08 2021

@author: Ana Clara St. Aubyn

Creating DVASA Dataset

"""

import pandas as pd
import os, inspect
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

#Importing Domestic Violence Data
data = pd.read_csv(r'Data\municipios_tratados.csv')

#Eliminate Rows Where the Municipality is not Defined (N.E.)
ne = data.loc[data.Municipio == "N.E."]
ne = ne.loc[ne.Tipo_Crime =='Violencia Domestica Conjuge ou Analogo'].values.flatten().tolist()[2:]
data = data[data['Municipio']!='N.E.']

#Look for Municipalities that do not Have all Categories
municipios = data.Municipio.value_counts()

#Counting Null Values by Category
for cat in list(data.Tipo_Crime.unique()):
    nan = data[data['Tipo_Crime']==cat].isna().sum().sum()
    print(str(cat) + ': ' + str(nan))
del cat

#Removing all Categories Except for DVASA
data = data[data['Tipo_Crime']=='Violencia Domestica Conjuge ou Analogo']
data.drop(columns=['Tipo_Crime'], inplace=True)

#See Difference Between National Total and Municipalities Total for DVASA Category
data_total = pd.read_csv(r'C:\Users\anacs\Documents\NOVA IMS\Mestrado\Tese\Dados\nacional_tratados.csv')

total = data_total.loc[data_total.Tipo_Crime == "Violencia Domestica Conjuge ou Analogo"].values.flatten().tolist()[1:]
total_mun = data.sum(numeric_only=True, axis=0).tolist()
diference = [a-b for a,b in zip(total, total_mun)]
diference = [a-b for a,b in zip(diference, ne)]
del total, total_mun

#Replace Missing Values by 1
data.fillna(1, inplace=True)

#Turn Years into One Column
data = data.melt(id_vars=["Municipio"], var_name="Ano", value_name="Value")
data['Ano'] = data['Ano'].apply(pd.to_numeric)

del data_total, diference, municipios, ne

#Export Final DVASA Dataset
data.to_csv(r'Data\DVASA.csv', index=False)


 