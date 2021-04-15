# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:21:08 2021

@author: Ana Clara St. Aubyn

Data Treatment Domestic Violence Municipalities Portugal

"""

import pandas as pd
import numpy as np
import os, inspect
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

#Importing Municipality Data
data = pd.read_csv(r'Data\Municipalities.csv', delimiter=';') 

#Eliminate Irrelevant Rows
data = data.iloc[5:]
data.reset_index(drop=True, inplace=True)

#Removing Null and Unnecessary Columns
data.dropna(axis=1, how='all', inplace=True)
data.drop([data.columns[0]], axis=1, inplace=True)

#Creating Titles for Columns
data.columns = data.iloc[0]
data = data.iloc[1:]
data.rename(columns={data.columns[0]: "Municipality", data.columns[1]: "Crime"}, inplace=True)

#Replacing Nulls in Municipality Columns
data['Municipality'] = data['Municipality'].fillna(method='ffill')

#Removing Unknown Characters from Municipality and Crime
data['Crime'] = data['Crime'].str.replace("[^A-Za-z1234567890'-. ]", "")
data['Municipality'] = data['Municipality'].str.replace("[^A-Za-z1234567890'-. ]", "")
data['Municipality'] = data['Municipality'].str.replace("gueda", "Águeda")
data['Municipality'] = data['Municipality'].str.replace("Azemis", "Azeméis")
data['Municipality'] = data['Municipality'].str.replace("So Joo", "São João")
data['Municipality'] = data['Municipality'].str.replace("Almodvar", "Almodóvar")
data['Municipality'] = data['Municipality'].str.replace("Mrtola", "Mértola")
data['Municipality'] = data['Municipality'].str.replace("lhavo", "Ílhavo")
data['Municipality'] = data['Municipality'].str.replace("Guimares", "Guimarães")
data['Municipality'] = data['Municipality'].str.replace("Pvoa", "Póvoa")
data['Municipality'] = data['Municipality'].str.replace("Famalico", "Famalicão")
data['Municipality'] = data['Municipality'].str.replace("Alfndega da F", "Alfândega da Fé")
data['Municipality'] = data['Municipality'].str.replace("Bragana", "Bragança")
data['Municipality'] = data['Municipality'].str.replace("Freixo de Espada  Cinta", "Freixo de Espada à Cinta")
data['Municipality'] = data['Municipality'].str.replace("Ansies", "Ansiães")
data['Municipality'] = data['Municipality'].str.replace("Covilh", "Covilhã")
data['Municipality'] = data['Municipality'].str.replace("Fundo", "Fundão")
data['Municipality'] = data['Municipality'].str.replace("Proena", "Proença")
data['Municipality'] = data['Municipality'].str.replace("Sert", "Sertã")
data['Municipality'] = data['Municipality'].str.replace("Velha de Rdo", "Velha de Ródão")
data['Municipality'] = data['Municipality'].str.replace("Gis", "Góis")
data['Municipality'] = data['Municipality'].str.replace("Lous", "Lousã")
data['Municipality'] = data['Municipality'].str.replace("Tbua", "Tábua")
data['Municipality'] = data['Municipality'].str.replace("vora", "Évora")
data['Municipality'] = data['Municipality'].str.replace("Mouro", "Mourão")
data['Municipality'] = data['Municipality'].str.replace("Vila Viosa", "Vila Viçosa")
data['Municipality'] = data['Municipality'].str.replace("Loul", "Loulé")
data['Municipality'] = data['Municipality'].str.replace("Olho", "Olhão")
data['Municipality'] = data['Municipality'].str.replace("Portimo", "Portimão")
data['Municipality'] = data['Municipality'].str.replace("So Brs", "São Brás")
data['Municipality'] = data['Municipality'].str.replace("Antnio", "António")
data['Municipality'] = data['Municipality'].str.replace("Foz Ca", "Foz Côa")
data['Municipality'] = data['Municipality'].str.replace("Alcobaa", "Alcobaça")
data['Municipality'] = data['Municipality'].str.replace("Alvaizere", "Alvaiázere")
data['Municipality'] = data['Municipality'].str.replace("Ansio", "Ansião")
data['Municipality'] = data['Municipality'].str.replace("Castanheira de Pra", "Castanheira de Pêra")
data['Municipality'] = data['Municipality'].str.replace("Figueir dos", "Figueiró dos")
data['Municipality'] = data['Municipality'].str.replace("Nazar", "Nazaré")
data['Municipality'] = data['Municipality'].str.replace("bidos", "Óbidos")
data['Municipality'] = data['Municipality'].str.replace("Pedrgo", "Pedrógão")
data['Municipality'] = data['Municipality'].str.replace("Porto de Ms", "Porto de Mós")
data['Municipality'] = data['Municipality'].str.replace("Lourinh", "Lourinhã")
data['Municipality'] = data['Municipality'].str.replace("Monte Agrao", "Monte Agraço")
data['Municipality'] = data['Municipality'].str.replace("Alter do Cho", "Alter do Chão")
data['Municipality'] = data['Municipality'].str.replace("Gavio", "Gavião")
data['Municipality'] = data['Municipality'].str.replace("Marvo", "Marvão")
data['Municipality'] = data['Municipality'].str.replace("Baio", "Baião")
data['Municipality'] = data['Municipality'].str.replace("Paos de", "Paços de")
data['Municipality'] = data['Municipality'].str.replace("Alpiara", "Alpiarça")
data['Municipality'] = data['Municipality'].str.replace("Zzere", "Zêzere")
data['Municipality'] = data['Municipality'].str.replace("Constncia", "Constância")
data['Municipality'] = data['Municipality'].str.replace("Goleg", "Golegã")
data['Municipality'] = data['Municipality'].str.replace("Mao", "Mação")
data['Municipality'] = data['Municipality'].str.replace("Santarm", "Santarém")
data['Municipality'] = data['Municipality'].str.replace("Ourm", "Ourém")
data['Municipality'] = data['Municipality'].str.replace("Alccer", "Alcácer")
data['Municipality'] = data['Municipality'].str.replace("Grndola", "Grândola")
data['Municipality'] = data['Municipality'].str.replace("Santiago do Cacm", "Santiago do Cacém")
data['Municipality'] = data['Municipality'].str.replace("Setbal", "Setúbal")
data['Municipality'] = data['Municipality'].str.replace("Melgao", "Melgaço")
data['Municipality'] = data['Municipality'].str.replace("Mono", "Monção")
data['Municipality'] = data['Municipality'].str.replace("Valena", "Valença")
data['Municipality'] = data['Municipality'].str.replace("Alij", "Alijó")
data['Municipality'] = data['Municipality'].str.replace("Meso Frio", "Mesão Frio")
data['Municipality'] = data['Municipality'].str.replace("Mura", "Murça")
data['Municipality'] = data['Municipality'].str.replace("Peso da Rgua", "Peso da Régua")
data['Municipality'] = data['Municipality'].str.replace("Penaguio", "Penaguião")
data['Municipality'] = data['Municipality'].str.replace("Valpaos", "Valpaços")
data['Municipality'] = data['Municipality'].str.replace("Cinfes", "Cinfães")
data['Municipality'] = data['Municipality'].str.replace("Mortgua", "Mortágua")
data['Municipality'] = data['Municipality'].str.replace("Santa Comba Do", "Santa Comba Dão")
data['Municipality'] = data['Municipality'].str.replace("So Pedro", "São Pedro")
data['Municipality'] = data['Municipality'].str.replace("Sto", "Sátão")
data['Municipality'] = data['Municipality'].str.replace("Tabuao", "Tabuaço")
data['Municipality'] = data['Municipality'].str.replace("Cmara", "Câmara")
data['Municipality'] = data['Municipality'].str.replace("So Vicente", "São Vicente")
data['Municipality'] = data['Municipality'].str.replace("Herosmo", "Heroísmo")
data['Municipality'] = data['Municipality'].str.replace("Aores", "Açores")
data['Municipality'] = data['Municipality'].str.replace("Povoao", "Povoação")
data['Municipality'] = data['Municipality'].str.replace("So Roque", "São Roque")
data['Municipality'] = data['Municipality'].str.replace("Vitria", "Vitória")

#Keeping Only Domestic Violence
data = data[data['Crime'].str.contains('violncia domstica') | data['Crime'].str.contains('Violncia domstica')]

#Correct Nulls
data = data.replace('..', np.nan)
data.dropna(axis=1, how='all', inplace=True)

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

#Convert Data to Numeric
data[data.columns[2:].tolist()] = data[data.columns[2:].tolist()].apply(lambda x: x.str.replace(' ',''))
data[data.columns[2:].tolist()] = data[data.columns[2:].tolist()].apply(pd.to_numeric)

#Exportar as CSV
data.to_csv(r'Data\municipalities_treated.csv', index=False)

