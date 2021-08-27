# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 12:08:35 2021

@author: anacs

First Model
"""
from linearmodels import PooledOLS
import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.diagnostic import het_white, het_breuschpagan
from statsmodels.stats.stattools import durbin_watson

##############################################################################
###                                   Model 1                              ###
##############################################################################

#Importing and preparing data
data = pd.read_csv(r'Data\dfinal.csv')
data.set_index(['Municipality', 'Year'], inplace=True)
data.drop(columns=['Population', 'Population100'], inplace=True)

#Pooled OLS with all variables (Model 1)
exog_vars = list(data.columns)
exog_vars.pop(0)
exog = sm.add_constant(data[exog_vars])
mod = PooledOLS(data.DVASA, exog)
pooled_res = mod.fit(cov_type="clustered", cluster_entity=True)
print(pooled_res)
resids = pooled_res.resids
fitted = pooled_res.fitted_values

#Heteroskedasticity in Model1 Plot
fig, ax = plt.subplots(figsize=(18, 5))
ax.scatter(fitted['fitted_values'], resids, color = 'darkseagreen')
ax.axhline(0, color = 'dimgray', ls = '--')
ax.set_xlabel('Predicted Values')
ax.set_ylabel('Residuals')
ax.set_title('Homoskedasticity Test - Model 1', fontsize=16)
plt.savefig(r'Images\Homo_Model1.png')
del fig, ax

#Heteroskedasticity in Model1 Tests
pooled_OLS_dataset = pd.concat([data, resids], axis=1)
exog = sm.tools.tools.add_constant(data[exog_vars]).fillna(0)
breusch_pagan_test_results = het_breuschpagan(pooled_OLS_dataset['residual'], exog)
labels = ['LM-Stat', 'LM p-val', 'F-Stat', 'F p-val'] 
print(dict(zip(labels, breusch_pagan_test_results)))
del labels

# Autocorrelation of residuals test
durbin_watson_test_results = durbin_watson(pooled_OLS_dataset['residual']) 
print(durbin_watson_test_results)

#Fazer gráficos com as variáveis e os resíduos
fig, axs = plt.subplots(nrows=3, ncols=4, figsize=(18, 10), squeeze=False)
def make_space_above(axes, topmargin=1):
    """ increase figure size to make topmargin (in inches) space for 
        titles, without changing the axes sizes"""
    fig = axes.flatten()[0].figure
    s = fig.subplotpars
    w, h = fig.get_size_inches()

    figh = h - (1-s.top)*h  + topmargin
    fig.subplots_adjust(bottom=s.bottom*h/figh, top=1-topmargin/figh)
    fig.set_figheight(figh)
fig.subplots_adjust(hspace=.4, wspace=.3)
make_space_above(axs, topmargin=1.1) 
fig.suptitle('Residuals vs. Explanatory Variables - Model 1', fontsize=20, y=0.97)
axs[0,0].scatter(pooled_OLS_dataset['Fertility'], pooled_OLS_dataset['residual'], s=15, c='darkseagreen')
axs[0,0].set_title('Fertility vs. Residuals')
axs[0,0].set_xlabel('Fertility')
axs[0,0].set_ylabel('Residuals')
axs[0,1].scatter(pooled_OLS_dataset['Middle_Aged_Women'], pooled_OLS_dataset['residual'], s=15, c='darkseagreen')
axs[0,1].set_title('Middle_Aged_Women vs. Residuals')
axs[0,1].set_xlabel('Middle_Aged_Women')
axs[0,1].set_ylabel('Residuals')
axs[0,2].scatter(pooled_OLS_dataset['Unemployment_Total'], pooled_OLS_dataset['residual'], s=15, c='darkseagreen')
axs[0,2].set_title('Unemployment_Total vs. Residuals')
axs[0,2].set_xlabel('Unemployment_Total')
axs[0,2].set_ylabel('Residuals')
axs[0,3].scatter(pooled_OLS_dataset['Unemployment_Male'], pooled_OLS_dataset['residual'], s=15, c='darkseagreen')
axs[0,3].set_title('Unemployment_Male vs. Residuals')
axs[0,3].set_xlabel('Unemployment_Male')
axs[0,3].set_ylabel('Residuals')
axs[1,0].scatter(pooled_OLS_dataset['Unemployment_Female'], pooled_OLS_dataset['residual'], s=15, c='darkseagreen')
axs[1,0].set_title('Unemployment_Female vs. Residuals')
axs[1,0].set_xlabel('Unemployment_Female')
axs[1,0].set_ylabel('Residuals')
axs[1,1].scatter(pooled_OLS_dataset['Marriages'], pooled_OLS_dataset['residual'], s=15, c='darkseagreen')
axs[1,1].set_title('Marriages vs. Residuals')
axs[1,1].set_xlabel('Marriages')
axs[1,1].set_ylabel('Residuals')
axs[1,2].scatter(pooled_OLS_dataset['Youth_Dependency'], pooled_OLS_dataset['residual'], s=15, c='darkseagreen')
axs[1,2].set_title('Youth_Dependency vs. Residuals')
axs[1,2].set_xlabel('Youth_Dependency')
axs[1,2].set_ylabel('Residuals')
axs[1,3].scatter(pooled_OLS_dataset['Total_Doctors'], pooled_OLS_dataset['residual'], s=15, c='darkseagreen')
axs[1,3].set_title('Total_Doctors vs. Residuals')
axs[1,3].set_xlabel('Total_Doctors')
axs[1,3].set_ylabel('Residuals')
axs[2,0].scatter(pooled_OLS_dataset['SS_Pensions'], pooled_OLS_dataset['residual'], s=15, c='darkseagreen')
axs[2,0].set_title('SS_Pensions vs. Residuals')
axs[2,0].set_xlabel('SS_Pensions')
axs[2,0].set_ylabel('Residuals')
axs[2,1].scatter(pooled_OLS_dataset['GER_Men'], pooled_OLS_dataset['residual'], s=15, c='darkseagreen')
axs[2,1].set_title('GER_Men vs. Residuals')
axs[2,1].set_xlabel('GER_Men')
axs[2,1].set_ylabel('Residuals')
axs[2,2].scatter(pooled_OLS_dataset['Divorces'], pooled_OLS_dataset['residual'], s=15, c='darkseagreen')
axs[2,2].set_title('Divorces vs. Residuals')
axs[2,2].set_xlabel('Divorces')
axs[2,2].set_ylabel('Residuals')
fig.delaxes(axs[2][3])
plt.savefig(r'Images\resid_explanatory_model1.png')
del fig, axs

##############################################################################
###                                   Model 2                              ###
##############################################################################

del breusch_pagan_test_results, durbin_watson_test_results, exog, fitted, mod
del pooled_res, resids, pooled_OLS_dataset

#Pooled OLS according to T tests (Model 2)
exog_vars = list(data.columns)
exog_vars.pop(0)
exog_vars.pop(1)
exog_vars.pop(1)
exog_vars.pop(1)
exog_vars.pop(6)
exog_vars.pop(7)
exog_vars.pop(8)
exog_vars.pop(9)
exog_vars.pop(-2)
exog = sm.add_constant(data[exog_vars])
mod = PooledOLS(data.DVASA, exog)
pooled_res = mod.fit(cov_type="clustered", cluster_entity=True)
print(pooled_res)
resids = pooled_res.resids
fitted = pooled_res.fitted_values

#Heteroskedasticity in Model2 Plot
fig, ax = plt.subplots(figsize=(18, 5))
ax.scatter(fitted['fitted_values'], resids, color = 'darkseagreen')
ax.axhline(0, color = 'dimgray', ls = '--')
ax.set_xlabel('Predicted Values')
ax.set_ylabel('Residuals')
ax.set_title('Homoskedasticity Test - Model 2', fontsize=16)
plt.savefig(r'Images\Homo_Model2.png')
del fig, ax