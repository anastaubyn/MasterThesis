# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 19:07:01 2021

@author: anacs

Theoretical Plots
"""

import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Residuals (Modelling Issues)
y = []
for i in range (0,101):
    y.append(random.random()*-3)
for i in range (0,101):
    y.append(random.random()*3)
x= []
for i in range (0,202):
    x.append(random.random()*10)
x_hetero = [2, 3, 3.5, 6, 11, 12, 13, 13.5, 15, 17, 17,5, 18, 19, 18, 19, 19, 20, 20, 20, 21, 22, 22.5, 23, 23.2, 24, 24.7, 25, 25.2, 27, 26.2, 28, 28.3, 29, 29.2, 30]
y_hetero = [40, 41, 10, -15, -40, -5, 0, -10, 45, 50, -100, -90, -50, 120, 90, 20, 110, 100, -120, 0, -130, 100, -50, 80, 100, 130, -200, 10.5, 180, -40.7, 0.3, 100, 250, -270, -50, 60.2]

n = 202        # elements number
x_poli = list(range(n))
x_poli = [i/100 for i in x_poli]
def GetPolyData(x):    
    return np.sin(x) + np.random.uniform(-.2, .2, n) 
y_poli = GetPolyData(x_poli)
poli_x = np.array(x_poli)
poli_y = np.array(y_poli)

fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(18, 5), squeeze=False)
def make_space_above(axes, topmargin=1):
    """ increase figure size to make topmargin (in inches) space for 
        titles, without changing the axes sizes"""
    fig = axes.flatten()[0].figure
    s = fig.subplotpars
    w, h = fig.get_size_inches()

    figh = h - (1-s.top)*h  + topmargin
    fig.subplots_adjust(bottom=s.bottom*h/figh, top=1-topmargin/figh)
    fig.set_figheight(figh)
make_space_above(axs, topmargin=1) 
fig.suptitle('Diagnostic Residual Plots', fontsize=20, y=0.97)
axs[0,0].scatter(x, y, c='darkseagreen')
axs[0,0].set_title('Residual Plot Without Red Flags')
axs[0,0].set_xlabel('X')
axs[0,0].set_ylabel('Residuals')
axs[0,1].scatter(x_hetero, y_hetero, c='darkseagreen')
axs[0,1].set_title('Residual Plot With Heteroskedasticity')
axs[0,1].set_xlabel('X')
axs[0,1].set_ylabel('Residuals')
axs[0,2].scatter(poli_x, poli_y, c='darkseagreen')
axs[0,2].set_title('Residual Plot With Wrong Functional Form')
axs[0,2].set_xlabel('X')
axs[0,2].set_ylabel('Residuals')
plt.savefig(r'Images\Theo_ResidualPlots.png')

del i, n, axs, fig, poli_x, poli_y, x, y, x_hetero, x_poli, y_hetero, y_poli

# Probability Density Functions
data = pd.read_csv(r'Data\dfinal.csv')
plt.figure(figsize=(14,6))
ax = sns.distplot(data['DVASA'], hist=False, kde=True, bins=int(180/5), color = 'darkseagreen', kde_kws={'linewidth': 2})
plt.plot([data["DVASA"].mean(), data["DVASA"].mean()], [0, 5.254], ls='--', color='dimgray')
ax.set_title('Probability Density Function for DVASA')
sns.despine()
plt.savefig(r'Images\DVASA_DensityFunction.png')

new_data = data.loc[data['GER'] == data['GER'].mode()[1]]
plt.figure(figsize=(14,6))
ax = sns.distplot(new_data['DVASA'], hist=False, kde=True, bins=int(180/5), color = 'darkseagreen', kde_kws={'linewidth': 2})
plt.plot([new_data["DVASA"].mean(), new_data["DVASA"].mean()], [0, 4.38], ls='--', color='dimgray')
ax.set_title('Conditional Probability Density Function for DVASA (GER = 70,16)')
sns.despine()
plt.savefig(r'Images\DVASA_ConditionalDensityFunction.png')

z = np.polyfit(data['GER'], data['DVASA'], 1)
p = np.poly1d(z)
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(14, 6), squeeze=False)
fig.suptitle('Graphical Relation Between GER and DVASA', fontsize=20, y=0.97)
axs[0,0].scatter(data['GER'], data['DVASA'], c='darkseagreen', s=3)
axs[0,0].spines['right'].set_visible(False)
axs[0,0].spines['top'].set_visible(False)
axs[0,0].set_title('Dispersion Plot for GER and DVASA')
axs[0,0].set_xlabel('GER')
axs[0,0].set_ylabel('DVASA')
axs[0,1].scatter(data['GER'], data['DVASA'], c='darkseagreen', s=3)
axs[0,1].plot(data['GER'],p(data['GER']),linestyle='dashed', linewidth=1, color='dimgray')
axs[0,1].spines['right'].set_visible(False)
axs[0,1].spines['top'].set_visible(False)
axs[0,1].set_title('Dispersion Plot for GER and DVASA')
axs[0,1].set_xlabel('GER')
axs[0,1].set_ylabel('DVASA')
plt.savefig(r'Images\dispersion_DVASAvsGER.png')