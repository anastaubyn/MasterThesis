# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 16:11:48 2021

@author: anacs

Appending Explanatory Variables
"""

import pandas as pd
import os, inspect
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

#Importing DVASA Dataset
Dvasa = pd.read_csv(r'Data\DVASA.csv')

#Importing Explanatory Variables
Fertility = pd.read_csv(r'Data\synthetic_fertility_index_final.csv')

#Checking if Municipality Names are the Same
mun_dvasa = Dvasa.Municipality.unique().tolist()
mun_fertility = Fertility.Municipality.unique().tolist()
mun_dvasa = sorted(mun_dvasa)
mun_fertility = sorted(mun_fertility)
dif = list(set(mun_dvasa).symmetric_difference(mun_fertility))

#Replacing Municipalities so That There is a Match
Dvasa['Municipality'] = Dvasa['Municipality'].str.replace("Vila Praia da Vitória", "Vila da Praia da Vitória")
Dvasa['Municipality'] = Dvasa['Municipality'].str.replace("Meda", "Mêda")
Dvasa['Municipality'] = Dvasa['Municipality'].str.replace("Velas \\(R.A.A.\\)", "Velas")
Dvasa['Municipality'] = Dvasa['Municipality'].str.replace("Lagoa \\(Açores\\)", "Lagoa [R.A.A.]")
Dvasa['Municipality'] = Dvasa['Municipality'].str.replace("Calheta \\(Açores\\)", "Calheta [R.A.A.]")
Dvasa['Municipality'] = Dvasa['Municipality'].str.replace("Almodóvar", "Almodôvar")
Dvasa['Municipality'] = Dvasa['Municipality'].str.replace("Lousãada", "Lousada")
Dvasa['Municipality'] = Dvasa['Municipality'].str.replace("Santa Cruz  Graciosa \\(R.A.A\\)", "Santa Cruz da Graciosa")
Dvasa['Municipality'] = Dvasa['Municipality'].str.replace("Calheta \\(Madeira\\)", "Calheta [R.A.M.]")
del mun_dvasa, mun_fertility, dif

#Changing Name of Columns
Dvasa.rename(columns={"Value": "DVASA"}, inplace=True)
Fertility.rename(columns={"Value": "Fertility"}, inplace=True)

#Merging Dvasa and Fertility (Fertility has no Data for 2008)
dfinal = Dvasa.merge(Fertility, on=["Municipality", "Year"], how = 'inner')
