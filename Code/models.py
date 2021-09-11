# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 12:08:35 2021

@author: anacs

Models
"""
from linearmodels import PooledOLS
import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.stattools import durbin_watson

##############################################################################
###                              Pre-Modelling                             ###
##############################################################################

#Importing and preparing data
data = pd.read_csv(r'Data\dfinal.csv')
data.set_index(['Municipality', 'Year'], inplace=True)
data.drop(columns=['Population', 'Population100'], inplace=True)

#Plotting Variables with DVASA
fig, axs = plt.subplots(nrows=5, ncols=4, figsize=(18, 16.666), squeeze=False)
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
fig.suptitle('Explanatory Variables vs. DVASA', fontsize=20, y=0.97)
axs[0,0].scatter(data['Fertility'], data['DVASA'], s=5, c='darkseagreen')
axs[0,0].set_title('Fertility vs. DVASA')
axs[0,0].set_xlabel('Fertility')
axs[0,0].set_ylabel('DVASA')
axs[0,1].scatter(data['Middle_Aged_Women'], data['DVASA'], s=5, c='darkseagreen')
axs[0,1].set_title('Middle_Aged_Women vs. DVASA')
axs[0,1].set_xlabel('Middle_Aged_Women')
axs[0,1].set_ylabel('DVASA')
axs[0,2].scatter(data['Unemployment_Total'], data['DVASA'], s=5, c='darkseagreen')
axs[0,2].set_title('Unemployment_Total vs. DVASA')
axs[0,2].set_xlabel('Unemployment_Total')
axs[0,2].set_ylabel('DVASA')
axs[0,3].scatter(data['Unemployment_Male'], data['DVASA'], s=5, c='darkseagreen')
axs[0,3].set_title('Unemployment_Male vs. DVASA')
axs[0,3].set_xlabel('Unemployment_Male')
axs[0,3].set_ylabel('DVASA')
axs[1,0].scatter(data['Unemployment_Female'], data['DVASA'], s=5, c='darkseagreen')
axs[1,0].set_title('Unemployment_Female vs. DVASA')
axs[1,0].set_xlabel('Unemployment_Female')
axs[1,0].set_ylabel('DVASA')
axs[1,1].scatter(data['Marriages'], data['DVASA'], s=5, c='darkseagreen')
axs[1,1].set_title('Marriages vs. DVASA')
axs[1,1].set_xlabel('Marriages')
axs[1,1].set_ylabel('DVASA')
axs[1,2].scatter(data['Youth_Dependency'], data['DVASA'], s=5, c='darkseagreen')
axs[1,2].set_title('Youth_Dependency vs. DVASA')
axs[1,2].set_xlabel('Youth_Dependency')
axs[1,2].set_ylabel('DVASA')
axs[1,3].scatter(data['Total_Doctors'], data['DVASA'], s=5, c='darkseagreen')
axs[1,3].set_title('Total_Doctors vs. DVASA')
axs[1,3].set_xlabel('Total_Doctors')
axs[1,3].set_ylabel('DVASA')
axs[2,0].scatter(data['SS_Pensions'], data['DVASA'], s=5, c='darkseagreen')
axs[2,0].set_title('SS_Pensions vs. DVASA')
axs[2,0].set_xlabel('SS_Pensions')
axs[2,0].set_ylabel('DVASA')
axs[2,1].scatter(data['GER_Men'], data['DVASA'], s=5, c='darkseagreen')
axs[2,1].set_title('GER_Men vs. DVASA')
axs[2,1].set_xlabel('GER_Men')
axs[2,1].set_ylabel('DVASA')
axs[2,2].scatter(data['Divorces'], data['DVASA'], s=5, c='darkseagreen')
axs[2,2].set_title('Divorces vs. DVASA')
axs[2,2].set_xlabel('Divorces')
axs[2,2].set_ylabel('DVASA')
axs[2,3].scatter(data['Elderly_Dependency'], data['DVASA'], s=5, c='darkseagreen')
axs[2,3].set_title('Elderly_Dependency vs. DVASA')
axs[2,3].set_xlabel('Elderly_Dependency')
axs[2,3].set_ylabel('DVASA')
axs[3,0].scatter(data['Men65'], data['DVASA'], s=5, c='darkseagreen')
axs[3,0].set_title('Men65 vs. DVASA')
axs[3,0].set_xlabel('Men65')
axs[3,0].set_ylabel('DVASA')
axs[3,1].scatter(data['Monthly_Gain'], data['DVASA'], s=5, c='darkseagreen')
axs[3,1].set_title('Monthly_Gain vs. DVASA')
axs[3,1].set_xlabel('Monthly_Gain')
axs[3,1].set_ylabel('DVASA')
axs[3,2].scatter(data['Wage_Gap'], data['DVASA'], s=5, c='darkseagreen')
axs[3,2].set_title('Wage_Gap vs. DVASA')
axs[3,2].set_xlabel('Wage_Gap')
axs[3,2].set_ylabel('DVASA')
axs[3,3].scatter(data['Female_Doctors'], data['DVASA'], s=5, c='darkseagreen')
axs[3,3].set_title('Female_Doctors vs. DVASA')
axs[3,3].set_xlabel('Female_Doctors')
axs[3,3].set_ylabel('DVASA')
axs[4,0].scatter(data['Mental_Health'], data['DVASA'], s=5, c='darkseagreen')
axs[4,0].set_title('Mental_Health vs. DVASA')
axs[4,0].set_xlabel('Mental_Health')
axs[4,0].set_ylabel('DVASA')
axs[4,1].scatter(data['GER'], data['DVASA'], s=5, c='darkseagreen')
axs[4,1].set_title('GER vs. DVASA')
axs[4,1].set_xlabel('GER')
axs[4,1].set_ylabel('DVASA')
axs[4,2].scatter(data['GER_Women'], data['DVASA'], s=5, c='darkseagreen')
axs[4,2].set_title('GER_Women vs. DVASA')
axs[4,2].set_xlabel('GER_Women')
axs[4,2].set_ylabel('DVASA')
axs[-1, -1].axis('off')
plt.savefig(r'Images\exp_vs_dvasa.png')
del fig, axs

##############################################################################
###                                   Model 1                              ###
##############################################################################

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

#Heteroskedasticity in Model2 Tests
pooled_OLS_dataset = pd.concat([data, resids], axis=1)
exog = sm.tools.tools.add_constant(data[exog_vars]).fillna(0)
breusch_pagan_test_results = het_breuschpagan(pooled_OLS_dataset['residual'], exog)
labels = ['LM-Stat', 'LM p-val', 'F-Stat', 'F p-val'] 
print(dict(zip(labels, breusch_pagan_test_results)))
del labels

# Autocorrelation of residuals test
durbin_watson_test_results = durbin_watson(pooled_OLS_dataset['residual']) 
print(durbin_watson_test_results)

##############################################################################
###                                   Model 3                              ###
##############################################################################

data['ln_DVASA'] = np.log(data['DVASA'])

#Pooled OLS with all variables in log-lin (Model 3)
exog_vars = list(data.columns)
exog_vars.pop(0)
exog_vars.pop(-1)
exog = sm.add_constant(data[exog_vars])
mod = PooledOLS(data.ln_DVASA, exog)
pooled_res = mod.fit(cov_type="clustered", cluster_entity=True)
print(pooled_res)
resids = pooled_res.resids
fitted = pooled_res.fitted_values

##############################################################################
###                                   Model 4                              ###
##############################################################################

data['ln_Men65'] = np.log(data['Men65'])
data['ln_Monthly_Gain'] = np.log(data['Monthly_Gain'])
data['ln_Middle_Aged_Women'] = np.log(data['Middle_Aged_Women'])
data['ln_Elderly_Dependency'] = np.log(data['Elderly_Dependency'])
data['ln_GER'] = np.log(data['GER'])
data['ln_GER_Men'] = np.log(data['GER_Men'])

#Pooled OLS with variables in log-lin and log-log (Model 4)
exog_vars = list(data.columns)
exog_vars.pop(0)
exog_vars.pop(-7)
exog_vars.pop(1)
exog_vars.pop(1)
exog_vars.pop(1)
exog_vars.pop(1)
exog_vars.pop(4)
exog_vars.pop(4)
exog_vars.pop(5)
exog_vars.pop(6)
exog_vars.pop(7)
exog_vars.pop(7)
exog = sm.add_constant(data[exog_vars])
mod = PooledOLS(data.ln_DVASA, exog)
pooled_res = mod.fit(cov_type="clustered", cluster_entity=True)
print(pooled_res)
resids = pooled_res.resids
fitted = pooled_res.fitted_values

#Heteroskedasticity in Model4 Tests
pooled_OLS_dataset = pd.concat([data, resids], axis=1)
exog = sm.tools.tools.add_constant(data[exog_vars]).fillna(0)
breusch_pagan_test_results = het_breuschpagan(pooled_OLS_dataset['residual'], exog)
labels = ['LM-Stat', 'LM p-val', 'F-Stat', 'F p-val'] 
print(dict(zip(labels, breusch_pagan_test_results)))
del labels

##############################################################################
###                                   Model 5                              ###
##############################################################################

data = pd.read_csv(r'Data\dfinal.csv')
dummies = pd.get_dummies(data['Year'])
del dummies[list(dummies.columns)[0]]
for col in list(dummies.columns):
    dummies[col] = dummies[col].astype(int)
del col
data_dummies = pd.concat([data, dummies], axis=1)
data_dummies.set_index(['Municipality', 'Year'], inplace=True)
data_dummies.drop(columns=['Population', 'Population100'], inplace=True)

exog_vars = list(data_dummies.columns)
exog_vars.pop(0)
exog = sm.add_constant(data_dummies[exog_vars])
mod = PooledOLS(data_dummies.DVASA, exog)
fe_res = mod.fit(cov_type="clustered", cluster_entity=True)
print(fe_res)
resids = fe_res.resids

#Heteroskedasticity in Model5 Tests
pooled_OLS_dataset = pd.concat([data_dummies, resids], axis=1)
exog = sm.tools.tools.add_constant(data_dummies[exog_vars]).fillna(0)
breusch_pagan_test_results = het_breuschpagan(pooled_OLS_dataset['residual'], exog)
labels = ['LM-Stat', 'LM p-val', 'F-Stat', 'F p-val'] 
print(dict(zip(labels, breusch_pagan_test_results)))
del labels

# Autocorrelation of residuals test
durbin_watson_test_results = durbin_watson(pooled_OLS_dataset['residual']) 
print(durbin_watson_test_results)

del breusch_pagan_test_results, dummies, durbin_watson_test_results, exog, exog_vars, mod, resids, pooled_OLS_dataset
del fe_res

##############################################################################
###                                   Model 6                              ###
##############################################################################

exog_vars = list(data_dummies.columns)
exog_vars.pop(0)
exog_vars.pop(2)
exog_vars.pop(20)
exog_vars.pop(12)
exog_vars.pop(12)
exog_vars.pop(9)
exog = sm.add_constant(data_dummies[exog_vars])
mod = PooledOLS(data_dummies.DVASA, exog)
fe_res = mod.fit(cov_type="clustered", cluster_entity=True)
print(fe_res)
resids = fe_res.resids

#Heteroskedasticity in Model6 Tests
pooled_OLS_dataset = pd.concat([data_dummies, resids], axis=1)
exog = sm.tools.tools.add_constant(data_dummies[exog_vars])
breusch_pagan_test_results = het_breuschpagan(pooled_OLS_dataset['residual'], exog)
labels = ['LM-Stat', 'LM p-val', 'F-Stat', 'F p-val'] 
print(dict(zip(labels, breusch_pagan_test_results)))
del labels

# Autocorrelation of residuals test
durbin_watson_test_results = durbin_watson(pooled_OLS_dataset['residual']) 
print(durbin_watson_test_results)

del exog, mod, fe_res, breusch_pagan_test_results, pooled_OLS_dataset, resids, durbin_watson_test_results

##############################################################################
###                                   Model 7                              ###
##############################################################################

exog_vars.pop(8)
exog_vars.pop(8)
exog_vars.pop(3)
exog_vars.pop(1)
exog_vars.pop(13)
exog = sm.add_constant(data_dummies[exog_vars])
mod = PooledOLS(data_dummies.DVASA, exog)
fe_res = mod.fit(cov_type="clustered", cluster_entity=True)
print(fe_res)

#Heteroskedasticity in Model7 Tests
resids = fe_res.resids
pooled_OLS_dataset = pd.concat([data_dummies, resids], axis=1)
exog = sm.tools.tools.add_constant(data_dummies[exog_vars])
breusch_pagan_test_results = het_breuschpagan(pooled_OLS_dataset['residual'], exog)
labels = ['LM-Stat', 'LM p-val', 'F-Stat', 'F p-val'] 
print(dict(zip(labels, breusch_pagan_test_results)))
del labels

# Autocorrelation of residuals test
durbin_watson_test_results = durbin_watson(pooled_OLS_dataset['residual']) 
print(durbin_watson_test_results)
