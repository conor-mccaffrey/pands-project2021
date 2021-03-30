# Program to output correlation plot on species. Follow on analyses from results of distribution of species data in histograms/scatter plots

import numpy as np
import pandas as pd
import sys
import matplotlib as mpl
import os
import matplotlib.pyplot as plt
from PIL import Image # this lets us convert images into arrays
import matplotlib.patches as mpatches # needed for waffle charts
import seaborn as sns


from uploadDataSet import data
setosa = data.loc[0:49] # splitting data by class (reference 24)
versicolor = data.loc[50:99]
virginica = data.loc[100:149]

sns.set(font_scale=2) # increasing font size of colour bar and x,y axes
fig, ax1 = plt.subplots(3, figsize=(25,20)) # setting up our subplot as per previous examples
# setting attributes of correlation heatmap
sns.heatmap(setosa.corr(), annot=True, cmap='YlGnBu' , cbar = True, linecolor='green', annot_kws={'size': 15}, robust = True, ax=ax1[0]) # 'annot_kws' will increase the size of the figures in the cell
ax1[0].set_title('Setosa', fontsize=30) # setting individual titles

sns.heatmap(versicolor.corr(), annot=True, cmap='YlGnBu' , cbar = True, linecolor='green', robust= True, annot_kws={'size': 15}, ax=ax1[1]) 
ax1[1].set_title('Versicolor', fontsize=30)

sns.heatmap(virginica.corr(), annot=True, cmap='YlGnBu' , cbar = True, linecolor='green', robust= True, annot_kws={'size': 15}, ax=ax1[2]) 
ax1[2].set_title('Virginica', fontsize=30)

fig.savefig('correlationSpecies.png')
