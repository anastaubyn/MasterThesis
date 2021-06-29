# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 16:11:48 2021

@author: anacs

Appending Explanatory Variables
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.neighbors import KNeighborsRegressor
import os, inspect
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

#Importing DVASA Dataset
Dvasa = pd.read_csv(r'Data\DVASA.csv')

#Importing Explanatory Variables
Fertility = pd.read_csv(r'Data\synthetic_fertility_index_final.csv')
Old_Men = pd.read_csv(r'Data\old_men_final.csv')
Monthly_Gain = pd.read_csv(r'Data\monthly_gain_final.csv')
Wage_Gap = pd.read_csv(r'Data\wage_gap_final.csv')
Middle_Women = pd.read_csv(r'Data\middle_aged_women_final.csv')
Unemployment_Women = pd.read_csv(r'Data\unemployment_female_final.csv')
Unemployment_Men = pd.read_csv(r'Data\unemployment_male_final.csv')
Unemployment = pd.read_csv(r'Data\unemployment_total_final.csv')
Marriages = pd.read_csv(r'Data\marriages_final.csv')
Elderly_Dependency = pd.read_csv(r'Data\elderly_dependency_final.csv')
Youth_Dependency = pd.read_csv(r'Data\youth_dependency_final.csv')
Divorces = pd.read_csv(r'Data\divorces_final.csv')
Female_Doctors = pd.read_csv(r'Data\female_doctors_final.csv')
Total_Doctors = pd.read_csv(r'Data\total_doctors_final.csv')
Mental_Health = pd.read_csv(r'Data\mental_health_final.csv')
SS_Pensions = pd.read_csv(r'Data\ss_pensions_final.csv')
Education = pd.read_csv(r'Data\education_total_final.csv')
Education_Men = pd.read_csv(r'Data\education_men_final.csv')
Education_Women = pd.read_csv(r'Data\education_women_final.csv')

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
dfinal['Population100'] = dfinal['Population']/100
dfinal['DVASA'] = dfinal['DVASA']/dfinal['Population100']

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

#Changing Name of Columns (Wage_Gap)
Wage_Gap.rename(columns={"Value": "Wage_Gap"}, inplace=True)

#Merging dfinal and Montlhy_Gain
dfinal = dfinal.merge(Wage_Gap, on=["Municipality", "Year"], how = 'inner')
del Wage_Gap

#Changing Name of Columns (Middle_Women)
Middle_Women.rename(columns={"Value": "Middle_Aged_Women"}, inplace=True)

#Merging dfinal and Middle_Women
dfinal = dfinal.merge(Middle_Women, on=["Municipality", "Year"], how = 'inner')
del Middle_Women

#Standardizing Middle_Aged_Women
dfinal['Middle_Aged_Women'] = (dfinal['Middle_Aged_Women']*100)/dfinal['Population']

#Changing Name of Columns (Unemployment) and Removing Duplicates
Unemployment.rename(columns={"Value": "Unemployment_Total"}, inplace=True)
Unemployment_Men.rename(columns={"Value": "Unemployment_Male"}, inplace=True)
Unemployment_Women.rename(columns={"Value": "Unemployment_Female"}, inplace=True)
Unemployment = Unemployment.drop_duplicates()
Unemployment_Men = Unemployment_Men.drop_duplicates()
Unemployment_Women = Unemployment_Women.drop_duplicates()

#Merging dfinal and Unemployment
dfinal = dfinal.merge(Unemployment, on=["Municipality", "Year"], how = 'inner')
del Unemployment
dfinal = dfinal.merge(Unemployment_Men, on=["Municipality", "Year"], how = 'inner')
del Unemployment_Men
dfinal = dfinal.merge(Unemployment_Women, on=["Municipality", "Year"], how = 'inner')
del Unemployment_Women

#Standardizing Unemployment
dfinal['Unemployment_Total'] = dfinal['Unemployment_Total']/dfinal['Population100']
dfinal['Unemployment_Male'] = dfinal['Unemployment_Male']/dfinal['Population100']
dfinal['Unemployment_Female'] = dfinal['Unemployment_Female']/dfinal['Population100']

#Changing Name of Columns (Marriages) and Removing Duplicates
Marriages.rename(columns={"Value": "Marriages"}, inplace=True)
Marriages = Marriages.drop_duplicates()

#Merging dfinal and Marriages
dfinal = dfinal.merge(Marriages, on=["Municipality", "Year"], how = 'inner')
del Marriages

#Standardizing Marriages
dfinal['Marriages'] = dfinal['Marriages'] / dfinal['Population100']

#Changing Name of Columns (Elderly_Dependency)
Elderly_Dependency.rename(columns={"Value": "Elderly_Dependency"}, inplace=True)

#Merging dfinal and Elderly_Dependency
dfinal = dfinal.merge(Elderly_Dependency, on=["Municipality", "Year"], how = 'inner')
del Elderly_Dependency

#Changing Name of Columns (Youth_Dependency)
Youth_Dependency.rename(columns={"Value": "Youth_Dependency"}, inplace=True)

#Merging dfinal and Elderly_Dependency
dfinal = dfinal.merge(Youth_Dependency, on=["Municipality", "Year"], how = 'inner')
del Youth_Dependency

#Changing Name of Columns (Divorces)
Divorces.rename(columns={"Value": "Divorces"}, inplace=True)

#Merging dfinal and Divorces
dfinal = dfinal.merge(Divorces, on=["Municipality", "Year"], how = 'inner')
del Divorces

#Removing 2008
dfinal = dfinal[dfinal.Year != 2008]

#Changing Name of Columns (Female_Doctors)
Female_Doctors.rename(columns={"Value": "Female_Doctors"}, inplace=True)

#Merging dfinal and Female_Doctors
dfinal = dfinal.merge(Female_Doctors, on=["Municipality", "Year"], how = 'inner')
del Female_Doctors

#Changing Name of Columns (Total_Doctors and Mental_Health)
Total_Doctors.rename(columns={"Value": "Total_Doctors"}, inplace=True)
Mental_Health.rename(columns={"Value": "Mental_Health"}, inplace=True)

#Merging dfinal and (Total_Doctors and Mental_Health)
dfinal = dfinal.merge(Total_Doctors, on=["Municipality", "Year"], how = 'inner')
dfinal = dfinal.merge(Mental_Health, on=["Municipality", "Year"], how = 'inner')
del Total_Doctors, Mental_Health

#Standardizing Total_Doctors
dfinal['Total_Doctors'] = dfinal['Total_Doctors']/dfinal['Population100']

#Changing Name of Columns (SS_Pensions)
SS_Pensions.rename(columns={"Value": "SS_Pensions"}, inplace=True)

#Merging dfinal and SS_Pensions
dfinal = dfinal.merge(SS_Pensions, on=["Municipality", "Year"], how = 'inner')
del SS_Pensions

#Correcting Nulls for Female_Doctors and Mental_Health
dfinal['Female_Doctors'] = dfinal['Female_Doctors'].fillna(0)
dfinal['Mental_Health'] = dfinal['Mental_Health'].fillna(0)

#Removing Azores and Madeira
autonomous = ['Angra do Heroísmo', 'Calheta [R.A.A.]', 'Corvo', 'Horta', 'Lagoa [R.A.A.]',
              'Lajes das Flores', 'Lajes do Pico', 'Madalena', 'Nordeste', 'Ponta Delgada',
              'Povoação', 'Ribeira Grande', 'São Roque do Pico', 'Vila da Praia da Vitória',
              'Santa Cruz da Graciosa', 'Santa Cruz das Flores', 'Velas', 'Vila do Porto',
              'Vila Franca do Campo', 'Calheta [R.A.M.]', 'Câmara de Lobos', 'Funchal',
              'Machico', 'Ponta do Sol', 'Porto Moniz', 'Porto Santo', 'Ribeira Brava',
              'São Vicente', 'Santa Cruz', 'Santana']
dfinal = dfinal[~dfinal.Municipality.isin(autonomous)]
del autonomous

#Checking if Municipality Names are the Same (Education and dfinal)
mun_dvasa = dfinal.Municipality.unique().tolist()
mun_education = Education.Municipality.unique().tolist()
mun_dvasa = sorted(mun_dvasa)
mun_education = sorted(mun_education)
dif = list(set(mun_dvasa).symmetric_difference(mun_education))
Education['Municipality'] = Education['Municipality'].str.replace("Meda", "Mêda")
Education_Men['Municipality'] = Education_Men['Municipality'].str.replace("Meda", "Mêda")
Education_Women['Municipality'] = Education_Women['Municipality'].str.replace("Meda", "Mêda")
del mun_dvasa, mun_education, dif

#Merging dfinal and Education
dfinal = dfinal.merge(Education, on=["Municipality", "Year"], how = 'inner')
Education_Men.rename(columns={"GER": "GER_Men"}, inplace=True)
dfinal = dfinal.merge(Education_Men, on=["Municipality", "Year"], how = 'inner')
Education_Women.rename(columns={"GER": "GER_Women"}, inplace=True)
dfinal = dfinal.merge(Education_Women, on=["Municipality", "Year"], how = 'inner')
del Education, Education_Men, Education_Women

#Calculating Correlations
for year in range(2009, 2020):
    data = dfinal.loc[dfinal['Year'] == year].drop(columns=['Year','Population', 'Population100'])
    corr = data.corr(method = 'pearson')
    corr = round(corr,1)
    f, ax = plt.subplots(figsize=(9, 9))
    ax.set_title('Contemporaneous Pearson Correlation for {}'.format(year), fontsize=16)
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    mask_annot = np.absolute(corr.values)>=0.4
    annot1 = np.where(mask_annot, corr.values, np.full((20,20),""))
    cmap = sb.diverging_palette(120, 40, as_cmap=True)
    sb.heatmap(corr, mask=mask, cmap=cmap, center=0, square=True, ax=ax, linewidths=.5, annot=annot1, fmt="s", vmin=-1, vmax=1, cbar_kws=dict(ticks=[-1,0,1]))
    sb.set(font_scale=0.7)
    sb.set_style('white')
    bottom, top = ax.get_ylim()
    ax.set_ylim(bottom + 0.5, top - 0.5)
    plt.gcf().subplots_adjust(left=0.25)
    plt.savefig(r'Images\correlations{}'.format(year))
    
del f, ax, bottom, corr, annot1, mask, mask_annot, top, year

    #get matrix with average correlations
data = dfinal.loc[dfinal['Year'] == 2009].drop(columns=['Year','Population', 'Population100'])
corr = data.corr(method = 'pearson')
for year in range(2010, 2020):
    data = dfinal.loc[dfinal['Year'] == year].drop(columns=['Year','Population', 'Population100'])
    corr2 = data.corr(method = 'pearson')
    corr = pd.concat((corr, corr2))
by_row_index = corr.groupby(corr.index)
corr = by_row_index.mean()
corr = round(corr,1)
corr = corr.reindex(list(corr.columns))
del corr2, data, year, by_row_index

f, ax = plt.subplots(figsize=(9, 9))
ax.set_title('Average Contemporaneous Pearson Correlation', fontsize=16)
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
mask_annot = np.absolute(corr.values)>=0.4
annot1 = np.where(mask_annot, corr.values, np.full((20,20),""))
cmap = sb.diverging_palette(120, 40, as_cmap=True)
sb.heatmap(corr, mask=mask, cmap=cmap, center=0, square=True, ax=ax, linewidths=.5, annot=annot1, fmt="s", vmin=-1, vmax=1, cbar_kws=dict(ticks=[-1,0,1]))
sb.set(font_scale=0.7)
sb.set_style('white')
bottom, top = ax.get_ylim()
ax.set_ylim(bottom + 0.5, top - 0.5)
plt.gcf().subplots_adjust(left=0.25)
plt.savefig(r'Images\correlations')
del f, ax, bottom, corr, annot1, mask, mask_annot, top

#Correcting Missing Values for SS_Pensions
dfinal2009 = dfinal[dfinal['Year']==2009]
corr = dfinal2009.corr()
del corr
dfinal_to_reg = dfinal2009[['SS_Pensions','Elderly_Dependency','Youth_Dependency', 'Middle_Aged_Women','Men65']]
reg_incomplete = dfinal_to_reg[dfinal_to_reg.SS_Pensions.isna()]
reg_complete = dfinal_to_reg[~dfinal_to_reg.index.isin(reg_incomplete.index)]
regressor = KNeighborsRegressor(7, weights ='distance', metric='euclidean')
neigh = regressor.fit(reg_complete.loc[:,['Elderly_Dependency','Youth_Dependency', 'Middle_Aged_Women','Men65']],
                      reg_complete.loc[:,['SS_Pensions']])
imputed = neigh.predict(reg_incomplete.drop(columns = ['SS_Pensions']))
imputed = imputed[0][0]
dfinal['SS_Pensions'] = dfinal['SS_Pensions'].fillna(imputed)
del dfinal_to_reg, neigh, imputed, reg_complete, reg_incomplete, dfinal2009, regressor

#Correcting Missing Values for Marriages
def impute_marriages(dfinal, year):
    dfinal2009 = dfinal[dfinal['Year']==year]
    dfinal_to_reg = dfinal2009[['Marriages','Elderly_Dependency','SS_Pensions', 'Middle_Aged_Women','Men65']]
    reg_incomplete = dfinal_to_reg[dfinal_to_reg.Marriages.isna()]
    reg_complete = dfinal_to_reg[~dfinal_to_reg.index.isin(reg_incomplete.index)]
    regressor = KNeighborsRegressor(7, weights ='distance', metric='euclidean')
    neigh = regressor.fit(reg_complete.loc[:,['Elderly_Dependency','SS_Pensions', 'Middle_Aged_Women','Men65']],
                          reg_complete.loc[:,['Marriages']])
    imputed = neigh.predict(reg_incomplete.drop(columns = ['Marriages']))
    imputed = imputed[0][0]
    dfinal2009['Marriages'] = dfinal2009['Marriages'].fillna(imputed)
    dfinal_not2009 = dfinal[dfinal['Year']!=year]
    dfinal = pd.concat([dfinal2009, dfinal_not2009])
    return dfinal

for year in range(2009, 2019):
    dfinal = impute_marriages(dfinal, year)
del year
    
#Correcting Missing Values for Divorces
def impute_divorces(dfinal, year):
    dfinal2009 = dfinal[dfinal['Year']==year]
    dfinal_to_reg = dfinal2009[['Divorces','Monthly_Gain','Fertility', 'Wage_Gap','SS_Pensions']]
    reg_incomplete = dfinal_to_reg[dfinal_to_reg.Divorces.isna()]
    reg_complete = dfinal_to_reg[~dfinal_to_reg.index.isin(reg_incomplete.index)]
    regressor = KNeighborsRegressor(7, weights ='distance', metric='euclidean')
    neigh = regressor.fit(reg_complete.loc[:,['Monthly_Gain','Fertility', 'Wage_Gap','SS_Pensions']],
                          reg_complete.loc[:,['Divorces']])
    imputed = neigh.predict(reg_incomplete.drop(columns = ['Divorces']))
    imputed = imputed[0][0]
    dfinal2009['Divorces'] = dfinal2009['Divorces'].fillna(imputed)
    dfinal_not2009 = dfinal[dfinal['Year']!=year]
    dfinal = pd.concat([dfinal2009, dfinal_not2009])
    return dfinal

for year in range(2009, 2013):
    dfinal = impute_divorces(dfinal, year)
del year
for year in range(2014, 2019):
    dfinal = impute_divorces(dfinal, year)
del year

def impute_divorces2(dfinal, year):
    dfinal2013 = dfinal[dfinal['Year']==year]
    reg_incomplete = dfinal2013[dfinal2013.Divorces.isna()]
    reg_complete = dfinal2013[~dfinal2013.index.isin(reg_incomplete.index)]
    regressor = KNeighborsRegressor(7, weights ='distance', metric='euclidean')
    neigh = regressor.fit(reg_complete.loc[:,['Monthly_Gain','Fertility', 'Wage_Gap','SS_Pensions']],
                          reg_complete.loc[:,['Divorces']])
    imputed = neigh.predict(reg_incomplete[['Monthly_Gain','Fertility', 'Wage_Gap','SS_Pensions']])
    temp_df = pd.DataFrame(imputed.reshape(-1,1), columns = ['Divorces'])
    reg_incomplete = reg_incomplete.drop(columns=['Divorces'])
    reg_incomplete = reg_incomplete.reset_index(drop=True)
    cols = reg_incomplete.columns.tolist()
    reg_incomplete = pd.concat([reg_incomplete, temp_df], axis=1, ignore_index=True, verify_integrity=False)
    reg_incomplete.columns = cols + ['Divorces']
    dfinal2013 = pd.concat([reg_incomplete, reg_complete])
    dfinal_not2013 = dfinal[dfinal['Year']!=year]
    dfinal = pd.concat([dfinal2013, dfinal_not2013])
    return dfinal

dfinal = impute_divorces2(dfinal, 2013)
dfinal = impute_divorces2(dfinal, 2019)

#Imputing Missing Values for Education
null_data = dfinal[dfinal.isnull().any(axis=1)]
