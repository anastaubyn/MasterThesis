# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:21:08 2021

@author: Ana Clara St. Aubyn

Tratamento de Dados Violência Doméstica Nacional

"""

import pandas as pd
import numpy as np

# importar dados
data = pd.read_csv(r'C:\Users\anacs\Documents\NOVA IMS\Mestrado\Tese\Dados\Nacional.csv', delimiter=';')

#eliminar linhas irrelevantes
data = data.iloc[5:]
data.reset_index(drop=True, inplace=True)

#colocar título certos nas colunas
data.columns = data.iloc[0]
data = data.iloc[1:]

#remover colunas só com null e colunas desnecessárias
data.dropna(axis=1, how='all', inplace=True)
data.drop([data.columns[0], data.columns[1]], axis=1, inplace=True)
data.rename(columns={data.columns[0]: "Tipo_Crime"}, inplace=True)

#eliminar linhas para outros tipos de crime nivel 2
data = data[data[data.columns[0]].notna()]

#remover caracteres desconhecidos da coluna Tipo_Crime
data['Tipo_Crime'] = data['Tipo_Crime'].str.replace("[^A-Za-z1234567890'-. ]", "")

#manter apenas violencia domestica
data = data[data['Tipo_Crime'].str.contains('violncia domstica') | data['Tipo_Crime'].str.contains('Violncia domstica')]

#apagar anos sem dados
data = data.replace('..', np.nan)
data.dropna(axis=1, how='all', inplace=True)

#meter os anos por ordem crescente
data = data[data.columns[::-1]]
cols = data.columns.tolist()
cols = cols[-1:] + cols[:-1]
data = data[cols]
del cols

#linha de soma
data[data.columns[1:].tolist()] = data[data.columns[1:].tolist()].apply(lambda x: x.str.replace(' ',''))
data[data.columns[1:].tolist()] = data[data.columns[1:].tolist()].apply(pd.to_numeric)
data.loc['Total']= data.sum(numeric_only=True, axis=0)
data.reset_index(drop=True, inplace=True)

#corrigir coluna Tipo_Crime
data['Tipo_Crime'] = ['Violencia Domestica Conjuge ou Analogo', 'Violencia Domestica Menores', 'Outros Violencia Domestica', 'Total']

#Exportar para CSV :)
data.to_csv(r'C:\Users\anacs\Documents\NOVA IMS\Mestrado\Tese\Dados\nacional_tratados.csv', index=False)

#TESTAR CSV
pd.read_csv(r'C:\Users\anacs\Documents\NOVA IMS\Mestrado\Tese\Dados\nacional_tratados.csv')

# GOOD TO GO!#