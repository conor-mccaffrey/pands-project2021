# Histograms of each variable

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

sns.displot(data['SepalLength_cm'], kde= False, bins = 15, color = 'green', edgecolor = 'orange', alpha=0.6) # setting kde as False in order to remove the density line as it is not relavant to task
# also altered alpha value to change transparency of the graph (adapted from Reference 13)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.suptitle('Sepal Length', fontsize = 12) # adding main title to histogram and setting fontsize
plt.ylim(0,25) # setting y-axis limits
plt.xlim(3,10) # setting x-axis limits
plt.grid(ls = '--', lw = '0.1', color = '#BEBEBE') # modifying grid lines so that they dont 'overpower' the data and used hex value for colour
plt.savefig('Sepal_Length.png') # saving output to specified .png file

sns.displot(data['SepalWidth_cm'], kde= False, bins = 15, color = 'yellow', edgecolor = 'orange', alpha=0.6)
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.suptitle('Sepal Width', fontsize = 12) 
plt.ylim(0,50) 
plt.xlim(0,6) 
plt.grid(ls = '--', lw = '0.1', color = '#BEBEBE') 
plt.savefig('Sepal_Width.png') 

sns.displot(data['PetalLength_cm'], kde= False, bins = 15, color = 'blue', edgecolor = 'orange', alpha=0.6)
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.suptitle('Petal Length', fontsize = 12) 
plt.ylim(0,50) 
plt.xlim(0,10) 
plt.grid(ls = '--', lw = '0.1', color = '#BEBEBE') 
plt.savefig('Petal Length.png') 


sns.displot(data['PetalWidth_cm'], kde= False, bins = 15, color = 'purple', edgecolor = 'orange', alpha=0.6)
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')
plt.suptitle('Petal Width', fontsize = 12) 
plt.ylim(0,40) 
plt.xlim(0,4) 
plt.grid(ls = '--', lw = '0.1', color = '#BEBEBE') 
plt.savefig('Petal_Width.png') 