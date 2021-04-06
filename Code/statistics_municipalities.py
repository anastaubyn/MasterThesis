# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 15:04:08 2021

@author: Ana Clara St. Aubyn

Estatísticas Municípios

"""

import pandas as pd

#Importar dados
data = pd.read_csv(r'C:\Users\anacs\Documents\NOVA IMS\Mestrado\Tese\Dados\municipios_tratados.csv')

#Eliminar registos N.E.
ne = data.loc[data.Municipio == "N.E."]
ne = ne.loc[ne.Tipo_Crime =='Violencia Domestica Conjuge ou Analogo'].values.flatten().tolist()[2:]
data = data[data['Municipio']!='N.E.']

#Ver municipios que não têm todas as categorias
municipios = data.Municipio.value_counts()

#Contagem de valores null por categoria e no total
for cat in list(data.Tipo_Crime.unique()):
    nan = data[data['Tipo_Crime']==cat].isna().sum().sum()
    print(str(cat) + ': ' + str(nan))
del cat

#Remover tudo menos DVASA
data = data[data['Tipo_Crime']=='Violencia Domestica Conjuge ou Analogo']
data.drop(columns=['Tipo_Crime'], inplace=True)

#Ver diferença entre total nacional DVASA e total municipios DVASA
data_total = pd.read_csv(r'C:\Users\anacs\Documents\NOVA IMS\Mestrado\Tese\Dados\nacional_tratados.csv')

total = data_total.loc[data_total.Tipo_Crime == "Violencia Domestica Conjuge ou Analogo"].values.flatten().tolist()[1:]
total_mun = data.sum(numeric_only=True, axis=0).tolist()
diference = [a-b for a,b in zip(total, total_mun)]
diference = [a-b for a,b in zip(diference, ne)]
del total, total_mun

#Substituir missing values
data.fillna(1, inplace=True)

#Fazer uma coluna para os anos
data = data.melt(id_vars=["Tipo_Crime", "Municipio"], var_name="Ano", value_name="Value")
data['Ano'] = data['Ano'].apply(pd.to_numeric)

#Somar valores das três categorias para obter total por municipio
for mun in list(data.Municipio.unique()):
    for year in range(2008,2020):
        line=['Total']
        line.append(mun)
        line.append(year)
        line.append(data[(data['Municipio'] == mun) & (data['Ano']==year)]['Value'].sum())
        data.loc[len(data)] = line
    
del line, mun, year

