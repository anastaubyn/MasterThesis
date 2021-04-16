# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 17:31:02 2021

@author: anacs

Plots Literature Review
"""

import numpy as np
import matplotlib.pyplot as plt

#Plot Age of Victims 2013-2017
categories = ['18-25', '26-35', '36-45', '46-55', '56-64', '65+']
age_general = [2271, 4414, 6177, 4366, 2444, 3525]
age_male = [279, 353, 509, 461, 373, 770]
number_processes_gen = sum(age_general)
number_processes_male = sum(age_male)
age_male = [int(round(x*100/number_processes_male, 0)) for x in age_male]
age_general = [int(round(x*100/number_processes_gen, 0)) for x in age_general]

x = np.arange(len(categories))

plt.figure(figsize=(14,6))
ax = plt.subplot(111)
ax.bar(x - 0.4/2, age_general, width=0.4, label='Percentage of Processes in General Report',color='darkseagreen')
ax.bar(x + 0.4/2, age_male, width=0.4, label='Percentage of Processes in Male Only Report', color='dimgrey')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.text(0.6, -0.15, 'Source: Associação Portuguesa de Apoio à Vítima (APAV)', transform=ax.transAxes)
ax.set_title('Age of Domestic Violence Victims 2013-2017', fontsize=16)
ax.set_xlabel('Age Group')
ax.set_ylabel('Percentage of Processes')
#ax.set_xticklabels(data.index)
ax.set_xticks(x)
ax.set_xticklabels(categories)
for i, v in enumerate(age_general):
    ax.text(i-0.3, v+0.2, str(v)+'%', color='darkseagreen')
for i, v in enumerate(age_male):
    ax.text(i+0.1, v+0.2, str(v)+'%', color='dimgrey')
ax.legend(ncol=1)
plt.savefig(r'Images\victims_age_2013_2017.png')