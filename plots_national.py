# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 15:21:08 2021

@author: Ana Clara St. Aubyn

Gráficos Violência Doméstica Nacional

"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#importar os dados
data = pd.read_csv(r'C:\Users\anacs\Documents\NOVA IMS\Mestrado\Tese\Dados\nacional_tratados.csv')

#gráfico para o total
data_total = data[data['Tipo_Crime']=='Total']
data_total.drop(columns=['Tipo_Crime'], inplace=True)
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

#gráfico para as categorias
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

#grafico para domestica conjuge
plt.figure(figsize=(14,6))
ax = plt.subplot(111)
ax.plot(data_categories['index'], data_categories["Violencia Domestica Conjuge ou Analogo"], label='Domestic Violence Against Spouse or Analogous',color='darkseagreen')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.text(0.7, -0.15, 'Source: Direção-Geral da Política de Justiça (DGPJ)', transform=ax.transAxes)
ax.set_title('Domestic Violence Against Spouse or Analogous Occurrences as Registered by Police Authorities', fontsize=16, fontproperties=font)
ax.set_xlabel('Year')
ax.set_ylabel('Number of Occurrences')
#ax.legend(ncol=1)