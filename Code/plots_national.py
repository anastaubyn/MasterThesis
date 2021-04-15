# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:21:08 2021

@author: Ana Clara St. Aubyn

Portuguese National Domestic Violence Plots

"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os, inspect
os.chdir(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))

#Importing Data
data = pd.read_csv(r'Data\national_treated.csv')

#Plot for Total Occurrences
data_total = data[data['Crime']=='Total']
data_total.drop(columns=['Crime'], inplace=True)
data_total = data_total.transpose()
data_total.reset_index(inplace=True)
data_total.rename(columns={data_total.columns[0]: "Year", data_total.columns[1]: "Number of Occurrences"}, inplace=True)

font = FontProperties()
font.set_name('Calibri')

plt.figure(figsize=(14,6))
ax = plt.subplot(111)
ax.plot(data_total['Year'], data_total["Number of Occurrences"], color='darkseagreen')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.text(0.7, -0.15, 'Source: Direção-Geral da Política de Justiça (DGPJ)', transform=ax.transAxes)
ax.set_title('Domestic Violence Occurrences as Registered by Police Authorities', fontsize=16, fontproperties=font)
ax.set_xlabel('Year')
ax.set_ylabel('Number of Occurrences')
plt.savefig(r'Images\national_total.png')

#Plot for Occurrences by Category
data_categories = data.transpose()
data_categories.columns = data_categories.iloc[0]
data_categories = data_categories.iloc[1:]
data_categories.drop(columns=['Total'], inplace=True)
data_categories.reset_index(inplace=True)

plt.figure(figsize=(14,6))
ax = plt.subplot(111)
ax.plot(data_categories['index'], data_categories["Violencia Domestica Conjuge ou Analogo"], linewidth=4, label='Domestic Violence Against Spouse or Analogous',color='darkseagreen')
ax.plot(data_categories['index'], data_categories["Violencia Domestica Menores"], linewidth=4, label='Domestic Violence Against Minors', color='dimgrey')
ax.plot(data_categories['index'], data_categories["Outros Violencia Domestica"], linewidth=4, label='Others', color='silver')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.text(0.7, -0.15, 'Source: Direção-Geral da Política de Justiça (DGPJ)', transform=ax.transAxes)
ax.set_title('Domestic Violence Occurrences as Registered by Police Authorities by Category', fontsize=16, fontproperties=font)
ax.set_xlabel('Year')
ax.set_ylabel('Number of Occurrences')
ax.legend(ncol=1)
plt.savefig(r'Images\national_categories')

#Plot for DVASA
plt.figure(figsize=(14,6))
ax = plt.subplot(111)
ax.plot(data_categories['index'], data_categories["Violencia Domestica Conjuge ou Analogo"], label='Domestic Violence Against Spouse or Analogous',color='darkseagreen')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.text(0.7, -0.15, 'Source: Direção-Geral da Política de Justiça (DGPJ)', transform=ax.transAxes)
ax.set_title('Domestic Violence Against Spouse or Analogous Occurrences as Registered by Police Authorities', fontsize=16, fontproperties=font)
ax.set_xlabel('Year')
ax.set_ylabel('Number of Occurrences')
plt.savefig(r'Images\national_DVASA.png')