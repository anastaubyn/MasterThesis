# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:21:08 2021

@author: Ana Clara St. Aubyn

Data Treatment - Domestic Violence Districts Portugal

"""

import pandas as pd
import numpy as np

#importar dados
data = pd.read_csv(r'C:\Users\anacs\Documents\NOVA IMS\Mestrado\Tese\Dados\Distrito.csv', delimiter=';')

#eliminar linhas irrelevantes
data = data.iloc[5:]
data.reset_index(drop=True, inplace=True)

#remover colunas só com null e colunas desnecessárias
data.dropna(axis=1, how='all', inplace=True)
data.drop([data.columns[0]], axis=1, inplace=True)

#colocar titulos nas colunas
data.columns = data.iloc[0]
data = data.iloc[1:]
data.rename(columns={data.columns[0]: "Tipo_Crime"}, inplace=True)

#substituir nulls da coluna Tipo_Crime
data['Tipo_Crime'] = data['Tipo_Crime'].fillna(method='ffill')

#remover caracteres desconhecidos da coluna Tipo_Crime e da coluna Distrito
data['Tipo_Crime'] = data['Tipo_Crime'].str.replace("[^A-Za-z1234567890'-. ]", "")
data['Distrito'] = data['Distrito'].str.replace("[^A-Za-z1234567890'-. ]", "")
data['Distrito'] = data['Distrito'].str.replace("vora", "Evora")
data['Distrito'] = data['Distrito'].str.replace("Bragana", "Braganca")
data['Distrito'] = data['Distrito'].str.replace("Santarm", "Santarem")
data['Distrito'] = data['Distrito'].str.replace("Setbal", "Setubal")
data['Distrito'] = data['Distrito'].str.replace("So Miguel", "Sao Miguel")
data['Distrito'] = data['Distrito'].str.replace("So Jorge", "Sao Jorge")

#manter apenas violencia domestica
data = data[data['Tipo_Crime'].str.contains('violncia domstica') | data['Tipo_Crime'].str.contains('Violncia domstica')]

#corrigir nulls
data = data.replace('..', np.nan)
data.dropna(axis=1, how='all', inplace=True)
data ['Distrito'] = data['Distrito'].replace(np.nan, 'Nacional')

#corrigir coluna Tipo_Crime
data['Tipo_Crime'] = data['Tipo_Crime'].replace('Violncia domstica cnjugeanlogo', 'Violencia Domestica Conjuge ou Analogo')
data['Tipo_Crime'] = data['Tipo_Crime'].replace('Violncia domstica contra menores', 'Violencia Domestica Menores')
data['Tipo_Crime'] = data['Tipo_Crime'].replace('Outros violncia domstica', 'Outros Violencia Domestica')

#meter os anos por ordem crescente
data = data[data.columns[::-1]]
cols = data.columns.tolist()
cols = cols[-2:] + cols[:-2]
data = data[cols]
del cols

#remover linhas de total
data = data[~(data['Tipo_Crime'].str.contains('Total'))]

#Exportar para CSV :)
data.to_csv(r'C:\Users\anacs\Documents\NOVA IMS\Mestrado\Tese\Dados\distritos_tratados.csv', index=False)

#TESTAR CSV
data = pd.read_csv(r'C:\Users\anacs\Documents\NOVA IMS\Mestrado\Tese\Dados\distritos_tratados.csv')

# GOOD TO GO!#
#SUBSTITUIR POR 0 OS VALORES NULL?