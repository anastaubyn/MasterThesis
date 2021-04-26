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
Old_Men = pd.read_csv(r'Data\old_men_final.csv')
Monthly_Gain = pd.read_csv(r'Data\monthly_gain_final.csv')

#Importing Helper Variables
Population = pd.read_csv(r'Data\resident_population_final.csv')

#Checking if Municipality Names are the Same (Fertility and Dvasa)
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

#Changing Name of Columns (Dvasa and Fertility)
Dvasa.rename(columns={"Value": "DVASA"}, inplace=True)
Fertility.rename(columns={"Value": "Fertility"}, inplace=True)

#Merging Dvasa and Fertility (Fertility has no Data for 2008)
dfinal = Dvasa.merge(Fertility, on=["Municipality", "Year"], how = 'inner')

del Dvasa, Fertility

#Checking if Municipality Names are the Same (dfinal and Population)
mun_dvasa = dfinal.Municipality.unique().tolist()
mun_pop = Population.Municipality.unique().tolist()
mun_dvasa = sorted(mun_dvasa)
mun_pop = sorted(mun_pop)
dif = list(set(mun_dvasa).symmetric_difference(mun_pop))
del mun_dvasa, mun_pop, dif

#Changing Name of Columns (Population)
Population.rename(columns={"Value": "Population"}, inplace=True)

#Merging dfinal and Population
dfinal = dfinal.merge(Population, on=["Municipality", "Year"], how = 'inner')

del Population

#Standardizing DVASA
dfinal['Population1000'] = dfinal['Population']/1000
dfinal['DVASA'] = dfinal['DVASA']/dfinal['Population1000']

#Changing Name of Columns (Old_Men)
Old_Men.rename(columns={"Value": "Old_Men"}, inplace=True)

#Merging dfinal and Old_Men
dfinal = dfinal.merge(Old_Men, on=["Municipality", "Year"], how = 'inner')
del Old_Men

#Standardizing Old_Men
dfinal['Old_Men'] = (dfinal['Old_Men']*100)/dfinal['Population']
dfinal.rename(columns={"Old_Men": "Men65"}, inplace=True)

#Changing Name of Columns (Monthly_Gain)
Monthly_Gain.rename(columns={"Value": "Monthly_Gain"}, inplace=True)

#Merging dfinal and Montlhy_Gain
dfinal = dfinal.merge(Monthly_Gain, on=["Municipality", "Year"], how = 'inner')
del Monthly_Gain