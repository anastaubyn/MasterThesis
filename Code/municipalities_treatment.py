# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:21:08 2021

@author: Ana Clara St. Aubyn

Tratamento de Dados Violência Doméstica Municípios

"""

import pandas as pd
import numpy as np

#importar dados
data = pd.read_csv(r'C:\Users\anacs\Documents\NOVA IMS\Mestrado\Tese\Dados\Municipio.csv', delimiter=';') 

#eliminar linhas irrelevantes
data = data.iloc[5:]
data.reset_index(drop=True, inplace=True)

#remover colunas só com null e colunas desnecessárias
data.dropna(axis=1, how='all', inplace=True)
data.drop([data.columns[0]], axis=1, inplace=True)

#colocar titulos nas colunas
data.columns = data.iloc[0]
data = data.iloc[1:]
data.rename(columns={data.columns[0]: "Municipio", data.columns[1]: "Tipo_Crime"}, inplace=True)

#substituir nulls da coluna Municipio
data['Municipio'] = data['Municipio'].fillna(method='ffill')

#remover caracteres desconhecidos da coluna Tipo_Crime e da coluna Municipio
data['Tipo_Crime'] = data['Tipo_Crime'].str.replace("[^A-Za-z1234567890'-. ]", "")
data['Municipio'] = data['Municipio'].str.replace("[^A-Za-z1234567890'-. ]", "")
data['Municipio'] = data['Municipio'].str.replace("gueda", "Águeda")
data['Municipio'] = data['Municipio'].str.replace("Azemis", "Azeméis")
data['Municipio'] = data['Municipio'].str.replace("So Joo", "São João")
data['Municipio'] = data['Municipio'].str.replace("Almodvar", "Almodóvar")
data['Municipio'] = data['Municipio'].str.replace("Mrtola", "Mértola")
data['Municipio'] = data['Municipio'].str.replace("lhavo", "Ílhavo")
data['Municipio'] = data['Municipio'].str.replace("Guimares", "Guimarães")
data['Municipio'] = data['Municipio'].str.replace("Pvoa", "Póvoa")
data['Municipio'] = data['Municipio'].str.replace("Famalico", "Famalicão")
data['Municipio'] = data['Municipio'].str.replace("Alfndega da F", "Alfândega da Fé")
data['Municipio'] = data['Municipio'].str.replace("Bragana", "Bragança")
data['Municipio'] = data['Municipio'].str.replace("Freixo de Espada  Cinta", "Freixo de Espada à Cinta")
data['Municipio'] = data['Municipio'].str.replace("Ansies", "Ansiães")
data['Municipio'] = data['Municipio'].str.replace("Covilh", "Covilhã")
data['Municipio'] = data['Municipio'].str.replace("Fundo", "Fundão")
data['Municipio'] = data['Municipio'].str.replace("Proena", "Proença")
data['Municipio'] = data['Municipio'].str.replace("Sert", "Sertã")
data['Municipio'] = data['Municipio'].str.replace("Velha de Rdo", "Velha de Ródão")
data['Municipio'] = data['Municipio'].str.replace("Gis", "Góis")
data['Municipio'] = data['Municipio'].str.replace("Lous", "Lousã")
data['Municipio'] = data['Municipio'].str.replace("Tbua", "Tábua")
data['Municipio'] = data['Municipio'].str.replace("vora", "Évora")
data['Municipio'] = data['Municipio'].str.replace("Mouro", "Mourão")
data['Municipio'] = data['Municipio'].str.replace("Vila Viosa", "Vila Viçosa")
data['Municipio'] = data['Municipio'].str.replace("Loul", "Loulé")
data['Municipio'] = data['Municipio'].str.replace("Olho", "Olhão")
data['Municipio'] = data['Municipio'].str.replace("Portimo", "Portimão")
data['Municipio'] = data['Municipio'].str.replace("So Brs", "São Brás")
data['Municipio'] = data['Municipio'].str.replace("Antnio", "António")
data['Municipio'] = data['Municipio'].str.replace("Foz Ca", "Foz Côa")
data['Municipio'] = data['Municipio'].str.replace("Alcobaa", "Alcobaça")
data['Municipio'] = data['Municipio'].str.replace("Alvaizere", "Alvaiázere")
data['Municipio'] = data['Municipio'].str.replace("Ansio", "Ansião")
data['Municipio'] = data['Municipio'].str.replace("Castanheira de Pra", "Castanheira de Pêra")
data['Municipio'] = data['Municipio'].str.replace("Figueir dos", "Figueiró dos")
data['Municipio'] = data['Municipio'].str.replace("Nazar", "Nazaré")
data['Municipio'] = data['Municipio'].str.replace("bidos", "Óbidos")
data['Municipio'] = data['Municipio'].str.replace("Pedrgo", "Pedrógão")
data['Municipio'] = data['Municipio'].str.replace("Porto de Ms", "Porto de Mós")
data['Municipio'] = data['Municipio'].str.replace("Lourinh", "Lourinhã")
data['Municipio'] = data['Municipio'].str.replace("Monte Agrao", "Monte Agraço")
data['Municipio'] = data['Municipio'].str.replace("Alter do Cho", "Alter do Chão")
data['Municipio'] = data['Municipio'].str.replace("Gavio", "Gavião")
data['Municipio'] = data['Municipio'].str.replace("Marvo", "Marvão")
data['Municipio'] = data['Municipio'].str.replace("Baio", "Baião")
data['Municipio'] = data['Municipio'].str.replace("Paos de", "Paços de")
data['Municipio'] = data['Municipio'].str.replace("Alpiara", "Alpiarça")
data['Municipio'] = data['Municipio'].str.replace("Zzere", "Zêzere")
data['Municipio'] = data['Municipio'].str.replace("Constncia", "Constância")
data['Municipio'] = data['Municipio'].str.replace("Goleg", "Golegã")
data['Municipio'] = data['Municipio'].str.replace("Mao", "Mação")
data['Municipio'] = data['Municipio'].str.replace("Santarm", "Santarém")
data['Municipio'] = data['Municipio'].str.replace("Ourm", "Ourém")
data['Municipio'] = data['Municipio'].str.replace("Alccer", "Alcácer")
data['Municipio'] = data['Municipio'].str.replace("Grndola", "Grândola")
data['Municipio'] = data['Municipio'].str.replace("Santiago do Cacm", "Santiago do Cacém")
data['Municipio'] = data['Municipio'].str.replace("Setbal", "Setúbal")
data['Municipio'] = data['Municipio'].str.replace("Melgao", "Melgaço")
data['Municipio'] = data['Municipio'].str.replace("Mono", "Monção")
data['Municipio'] = data['Municipio'].str.replace("Valena", "Valença")
data['Municipio'] = data['Municipio'].str.replace("Alij", "Alijó")
data['Municipio'] = data['Municipio'].str.replace("Meso Frio", "Mesão Frio")
data['Municipio'] = data['Municipio'].str.replace("Mura", "Murça")
data['Municipio'] = data['Municipio'].str.replace("Peso da Rgua", "Peso da Régua")
data['Municipio'] = data['Municipio'].str.replace("Penaguio", "Penaguião")
data['Municipio'] = data['Municipio'].str.replace("Valpaos", "Valpaços")
data['Municipio'] = data['Municipio'].str.replace("Cinfes", "Cinfães")
data['Municipio'] = data['Municipio'].str.replace("Mortgua", "Mortágua")
data['Municipio'] = data['Municipio'].str.replace("Santa Comba Do", "Santa Comba Dão")
data['Municipio'] = data['Municipio'].str.replace("So Pedro", "São Pedro")
data['Municipio'] = data['Municipio'].str.replace("Sto", "Sátão")
data['Municipio'] = data['Municipio'].str.replace("Tabuao", "Tabuaço")
data['Municipio'] = data['Municipio'].str.replace("Cmara", "Câmara")
data['Municipio'] = data['Municipio'].str.replace("So Vicente", "São Vicente")
data['Municipio'] = data['Municipio'].str.replace("Herosmo", "Heroísmo")
data['Municipio'] = data['Municipio'].str.replace("Aores", "Açores")
data['Municipio'] = data['Municipio'].str.replace("Povoao", "Povoação")
data['Municipio'] = data['Municipio'].str.replace("So Roque", "São Roque")
data['Municipio'] = data['Municipio'].str.replace("Vitria", "Vitória")

#manter apenas violencia domestica
data = data[data['Tipo_Crime'].str.contains('violncia domstica') | data['Tipo_Crime'].str.contains('Violncia domstica')]

#corrigir nulls
data = data.replace('..', np.nan)
data.dropna(axis=1, how='all', inplace=True)

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

#meter dados numericos
data[data.columns[2:].tolist()] = data[data.columns[2:].tolist()].apply(lambda x: x.str.replace(' ',''))
data[data.columns[2:].tolist()] = data[data.columns[2:].tolist()].apply(pd.to_numeric)

#Exportar para CSV :)
data.to_csv(r'C:\Users\anacs\Documents\NOVA IMS\Mestrado\Tese\Dados\municipios_tratados.csv', index=False)

#TESTAR CSV
data = pd.read_csv(r'C:\Users\anacs\Documents\NOVA IMS\Mestrado\Tese\Dados\municipios_tratados.csv')

# GOOD TO GO!#
#SUBSTITUIR POR 0 OS VALORES NULL?