# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 12:08:35 2021

@author: anacs

First Model
"""
from linearmodels import PooledOLS
import statsmodels.api as sm
import pandas as pd


data = pd.read_csv(r'Data\dfinal.csv')
data.set_index(['Municipality', 'Year'], inplace=True)

exog_vars = ['Unemployment_Total', 'GER_Men', 'SS_Pensions', 'Monthly_Gain', 'Total_Doctors', 'Fertility', 'Youth_Dependency']
exog = sm.add_constant(data[exog_vars])
mod = PooledOLS(data.DVASA, exog)
pooled_res = mod.fit()
print(pooled_res)
