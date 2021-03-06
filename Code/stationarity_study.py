# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 11:52:43 2021

@author: anacs

Stationarity Studies
"""
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

#Importing Dataset
data = pd.read_csv(r'Data\dfinal.csv')

#Getting Average Values to Build One Time Series for Each Variable
avg = data.groupby(by=["Year"]).mean()

#Getting First Differences
differences = avg.diff()
differences.columns = [str(col) + '_diff' for col in differences.columns]

#Joining Averages and Differences
plot_df = avg.merge(differences, left_index=True, right_index=True)
plot_df.reset_index(inplace=True)

#Plotting Stationarity
fig, axs = plt.subplots(nrows=10, ncols=4, figsize=(20,25))
fig.tight_layout(pad=3.0)
def make_space_above(axes, topmargin=1):
    """ increase figure size to make topmargin (in inches) space for 
        titles, without changing the axes sizes"""
    fig = axes.flatten()[0].figure
    s = fig.subplotpars
    w, h = fig.get_size_inches()

    figh = h - (1-s.top)*h  + topmargin
    fig.subplots_adjust(bottom=s.bottom*h/figh, top=1-topmargin/figh)
    fig.set_figheight(figh)
make_space_above(axs, topmargin=2) 
fig.suptitle('Evolution and Changes of Variables', fontsize=20, y=0.97)
axs[0, 0].plot(plot_df['Year'], plot_df['DVASA'], color='darkseagreen')
axs[0, 0].set_title('DVASA Average Evolution')
axs[0, 0].set_xlabel('Year')
axs[0, 0].spines['right'].set_visible(False)
axs[0, 0].spines['top'].set_visible(False)
axs[0, 1].plot(plot_df['Year'], plot_df['DVASA_diff'], color='darkseagreen')
axs[0, 1].set_title('DVASA Average Changes')
axs[0, 1].set_xlabel('Year')
axs[0, 1].spines['right'].set_visible(False)
axs[0, 1].spines['top'].set_visible(False)
axs[0, 2].plot(plot_df['Year'], plot_df['Divorces'], color='darkseagreen')
axs[0, 2].set_title('Divorces Average Evolution')
axs[0, 2].set_xlabel('Year')
axs[0, 2].spines['right'].set_visible(False)
axs[0, 2].spines['top'].set_visible(False)
axs[0, 3].plot(plot_df['Year'], plot_df['Divorces_diff'], color='darkseagreen')
axs[0, 3].set_title('Divorces Average Changes')
axs[0, 3].set_xlabel('Year')
axs[0, 3].spines['right'].set_visible(False)
axs[0, 3].spines['top'].set_visible(False)
axs[1, 0].plot(plot_df['Year'], plot_df['Elderly_Dependency'], color='darkseagreen')
axs[1, 0].set_title('Elderly_Dependency Average Evolution')
axs[1, 0].set_xlabel('Year')
axs[1, 0].spines['right'].set_visible(False)
axs[1, 0].spines['top'].set_visible(False)
axs[1, 1].plot(plot_df['Year'], plot_df['Elderly_Dependency_diff'], color='darkseagreen')
axs[1, 1].set_title('Elderly_Dependency Average Changes')
axs[1, 1].set_xlabel('Year')
axs[1, 1].spines['right'].set_visible(False)
axs[1, 1].spines['top'].set_visible(False)
axs[1, 2].plot(plot_df['Year'], plot_df['Female_Doctors'], color='darkseagreen')
axs[1, 2].set_title('Female_Doctors Average Evolution')
axs[1, 2].set_xlabel('Year')
axs[1, 2].spines['right'].set_visible(False)
axs[1, 2].spines['top'].set_visible(False)
axs[1, 3].plot(plot_df['Year'], plot_df['Female_Doctors_diff'], color='darkseagreen')
axs[1, 3].set_title('Female_Doctors Average Changes')
axs[1, 3].set_xlabel('Year')
axs[1, 3].spines['right'].set_visible(False)
axs[1, 3].spines['top'].set_visible(False)
axs[2, 0].plot(plot_df['Year'], plot_df['Fertility'], color='darkseagreen')
axs[2, 0].set_title('Fertility Average Evolution')
axs[2, 0].set_xlabel('Year')
axs[2, 0].spines['right'].set_visible(False)
axs[2, 0].spines['top'].set_visible(False)
axs[2, 1].plot(plot_df['Year'], plot_df['Fertility_diff'], color='darkseagreen')
axs[2, 1].set_title('Fertility Average Changes')
axs[2, 1].set_xlabel('Year')
axs[2, 1].spines['right'].set_visible(False)
axs[2, 1].spines['top'].set_visible(False)
axs[2, 2].plot(plot_df['Year'], plot_df['GER'], color='darkseagreen')
axs[2, 2].set_title('GER Average Evolution')
axs[2, 2].set_xlabel('Year')
axs[2, 2].spines['right'].set_visible(False)
axs[2, 2].spines['top'].set_visible(False)
axs[2, 3].plot(plot_df['Year'], plot_df['GER_diff'], color='darkseagreen')
axs[2, 3].set_title('GER Average Changes')
axs[2, 3].set_xlabel('Year')
axs[2, 3].spines['right'].set_visible(False)
axs[2, 3].spines['top'].set_visible(False)
axs[3, 0].plot(plot_df['Year'], plot_df['GER_Men'], color='darkseagreen')
axs[3, 0].set_title('GER_Men Average Evolution')
axs[3, 0].set_xlabel('Year')
axs[3, 0].spines['right'].set_visible(False)
axs[3, 0].spines['top'].set_visible(False)
axs[3, 1].plot(plot_df['Year'], plot_df['GER_Men_diff'], color='darkseagreen')
axs[3, 1].set_title('GER_Men Average Changes')
axs[3, 1].set_xlabel('Year')
axs[3, 1].spines['right'].set_visible(False)
axs[3, 1].spines['top'].set_visible(False)
axs[3, 2].plot(plot_df['Year'], plot_df['GER_Women'], color='darkseagreen')
axs[3, 2].set_title('GER_Women Average Evolution')
axs[3, 2].set_xlabel('Year')
axs[3, 2].spines['right'].set_visible(False)
axs[3, 2].spines['top'].set_visible(False)
axs[3, 3].plot(plot_df['Year'], plot_df['GER_Women_diff'], color='darkseagreen')
axs[3, 3].set_title('GER_Women Average Changes')
axs[3, 3].set_xlabel('Year')
axs[3, 3].spines['right'].set_visible(False)
axs[3, 3].spines['top'].set_visible(False)
axs[4, 0].plot(plot_df['Year'], plot_df['Marriages'], color='darkseagreen')
axs[4, 0].set_title('Marriages Average Evolution')
axs[4, 0].set_xlabel('Year')
axs[4, 0].spines['right'].set_visible(False)
axs[4, 0].spines['top'].set_visible(False)
axs[4, 1].plot(plot_df['Year'], plot_df['Marriages_diff'], color='darkseagreen')
axs[4, 1].set_title('Marriages Average Changes')
axs[4, 1].set_xlabel('Year')
axs[4, 1].spines['right'].set_visible(False)
axs[4, 1].spines['top'].set_visible(False)
axs[4, 2].plot(plot_df['Year'], plot_df['Men65'], color='darkseagreen')
axs[4, 2].set_title('Men65 Average Evolution')
axs[4, 2].set_xlabel('Year')
axs[4, 2].spines['right'].set_visible(False)
axs[4, 2].spines['top'].set_visible(False)
axs[4, 3].plot(plot_df['Year'], plot_df['Men65_diff'], color='darkseagreen')
axs[4, 3].set_title('Men65 Average Changes')
axs[4, 3].set_xlabel('Year')
axs[4, 3].spines['right'].set_visible(False)
axs[4, 3].spines['top'].set_visible(False)
axs[5, 0].plot(plot_df['Year'], plot_df['Mental_Health'], color='darkseagreen')
axs[5, 0].set_title('Mental_Health Average Evolution')
axs[5, 0].set_xlabel('Year')
axs[5, 0].spines['right'].set_visible(False)
axs[5, 0].spines['top'].set_visible(False)
axs[5, 1].plot(plot_df['Year'], plot_df['Mental_Health_diff'], color='darkseagreen')
axs[5, 1].set_title('Mental_Health Average Changes')
axs[5, 1].set_xlabel('Year')
axs[5, 1].spines['right'].set_visible(False)
axs[5, 1].spines['top'].set_visible(False)
axs[5, 2].plot(plot_df['Year'], plot_df['Middle_Aged_Women'], color='darkseagreen')
axs[5, 2].set_title('Middle_Aged_Women Average Evolution')
axs[5, 2].set_xlabel('Year')
axs[5, 2].spines['right'].set_visible(False)
axs[5, 2].spines['top'].set_visible(False)
axs[5, 3].plot(plot_df['Year'], plot_df['Middle_Aged_Women_diff'], color='darkseagreen')
axs[5, 3].set_title('Middle_Aged_Women Average Changes')
axs[5, 3].set_xlabel('Year')
axs[5, 3].spines['right'].set_visible(False)
axs[5, 3].spines['top'].set_visible(False)
axs[6, 0].plot(plot_df['Year'], plot_df['Monthly_Gain'], color='darkseagreen')
axs[6, 0].set_title('Monthly_Gain Average Evolution')
axs[6, 0].set_xlabel('Year')
axs[6, 0].spines['right'].set_visible(False)
axs[6, 0].spines['top'].set_visible(False)
axs[6, 1].plot(plot_df['Year'], plot_df['Monthly_Gain_diff'], color='darkseagreen')
axs[6, 1].set_title('Monthly_Gain Average Changes')
axs[6, 1].set_xlabel('Year')
axs[6, 1].spines['right'].set_visible(False)
axs[6, 1].spines['top'].set_visible(False)
axs[6, 2].plot(plot_df['Year'], plot_df['SS_Pensions'], color='darkseagreen')
axs[6, 2].set_title('SS_Pensions Average Evolution')
axs[6, 2].set_xlabel('Year')
axs[6, 2].spines['right'].set_visible(False)
axs[6, 2].spines['top'].set_visible(False)
axs[6, 3].plot(plot_df['Year'], plot_df['SS_Pensions_diff'], color='darkseagreen')
axs[6, 3].set_title('SS_Pensions Average Changes')
axs[6, 3].set_xlabel('Year')
axs[6, 3].spines['right'].set_visible(False)
axs[6, 3].spines['top'].set_visible(False)
axs[7, 0].plot(plot_df['Year'], plot_df['Total_Doctors'], color='darkseagreen')
axs[7, 0].set_title('Total_Doctors Average Evolution')
axs[7, 0].set_xlabel('Year')
axs[7, 0].spines['right'].set_visible(False)
axs[7, 0].spines['top'].set_visible(False)
axs[7, 1].plot(plot_df['Year'], plot_df['Total_Doctors_diff'], color='darkseagreen')
axs[7, 1].set_title('Total_Doctors Average Changes')
axs[7, 1].set_xlabel('Year')
axs[7, 1].spines['right'].set_visible(False)
axs[7, 1].spines['top'].set_visible(False)
axs[7, 2].plot(plot_df['Year'], plot_df['Unemployment_Female'], color='darkseagreen')
axs[7, 2].set_title('Unemployment_Female Average Evolution')
axs[7, 2].set_xlabel('Year')
axs[7, 2].spines['right'].set_visible(False)
axs[7, 2].spines['top'].set_visible(False)
axs[7, 3].plot(plot_df['Year'], plot_df['Unemployment_Female_diff'], color='darkseagreen')
axs[7, 3].set_title('Unemployment_Female Average Changes')
axs[7, 3].set_xlabel('Year')
axs[7, 3].spines['right'].set_visible(False)
axs[7, 3].spines['top'].set_visible(False)
axs[8, 0].plot(plot_df['Year'], plot_df['Unemployment_Male'], color='darkseagreen')
axs[8, 0].set_title('Unemployment_Male Average Evolution')
axs[8, 0].set_xlabel('Year')
axs[8, 0].spines['right'].set_visible(False)
axs[8, 0].spines['top'].set_visible(False)
axs[8, 1].plot(plot_df['Year'], plot_df['Unemployment_Male_diff'], color='darkseagreen')
axs[8, 1].set_title('Unemployment_Male Average Changes')
axs[8, 1].set_xlabel('Year')
axs[8, 1].spines['right'].set_visible(False)
axs[8, 1].spines['top'].set_visible(False)
axs[8, 2].plot(plot_df['Year'], plot_df['Unemployment_Total'], color='darkseagreen')
axs[8, 2].set_title('Unemployment_Total Average Evolution')
axs[8, 2].set_xlabel('Year')
axs[8, 2].spines['right'].set_visible(False)
axs[8, 2].spines['top'].set_visible(False)
axs[8, 3].plot(plot_df['Year'], plot_df['Unemployment_Total'], color='darkseagreen')
axs[8, 3].set_title('Unemployment_Total Average Changes')
axs[8, 3].set_xlabel('Year')
axs[8, 3].spines['right'].set_visible(False)
axs[8, 3].spines['top'].set_visible(False)
axs[9, 0].plot(plot_df['Year'], plot_df['Youth_Dependency'], color='darkseagreen')
axs[9, 0].set_title('Youth_Dependency Average Evolution')
axs[9, 0].set_xlabel('Year')
axs[9, 0].spines['right'].set_visible(False)
axs[9, 0].spines['top'].set_visible(False)
axs[9, 1].plot(plot_df['Year'], plot_df['Youth_Dependency_diff'], color='darkseagreen')
axs[9, 1].set_title('Youth_Dependency Average Changes')
axs[9, 1].set_xlabel('Year')
axs[9, 1].spines['right'].set_visible(False)
axs[9, 1].spines['top'].set_visible(False)
axs[9, 2].plot(plot_df['Year'], plot_df['Wage_Gap'], color='darkseagreen')
axs[9, 2].set_title('Wage_Gap Average Evolution')
axs[9, 2].set_xlabel('Year')
axs[9, 2].spines['right'].set_visible(False)
axs[9, 2].spines['top'].set_visible(False)
axs[9, 3].plot(plot_df['Year'], plot_df['Wage_Gap_diff'], color='darkseagreen')
axs[9, 3].set_title('Wage_Gap Average Changes')
axs[9, 3].set_xlabel('Year')
axs[9, 3].spines['right'].set_visible(False)
axs[9, 3].spines['top'].set_visible(False)
plt.savefig(r'Images\stationarity.png')
del fig, axs

#Augmented Dickey-Fuller
lst = list(data.columns)
lst.remove('Municipality')
lst.remove('Year')
adf = []
for var in lst:
    for mun in list(data.Municipality.unique()):
        x = [mun, var]
        X = data.loc[data['Municipality'] == mun].sort_values('Year')[var]
        result = adfuller(X)
        x.append(result[1])
        adf.append(x)
del lst, mun, var, x, X
adf = pd.DataFrame.from_records(adf)
adf.columns = ['Municipality', 'Variable', 'P-Value']
significant5 = adf.loc[adf['P-Value'] <= 0.05]
significant10 = adf.loc[adf['P-Value'] <= 0.1]
