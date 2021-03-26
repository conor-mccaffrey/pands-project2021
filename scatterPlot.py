# Program to output scatter plots of each pair of variables

import numpy as np
import pandas as pd
import sys
import matplotlib as mpl
import os
import matplotlib.pyplot as plt
from PIL import Image # this lets us convert images into arrays
import matplotlib.patches as mpatches # needed for waffle charts
import seaborn as sns


from uploadDataSet import data # importing our data. Again, this wont be necessary for final program
plt.figure() # idea adapted from reference StackOverflow (reference 19) 
sns.set_style("darkgrid") # adapted from StackOverflow (reference 20)
sns.scatterplot(data=data, x=data['SepalLength_cm'], y=data['SepalWidth_cm'], hue = data['Class']) #setting properties of plot (reference 20)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.suptitle('Sepal Length v Sepal Width', fontsize = 12) 
plt.savefig('scatPlotSL_v_SW.png') # saving output to a new file

plt.figure()
sns.scatterplot(data=data, x=data['SepalLength_cm'], y=data['PetalWidth_cm'], hue = data['Class']) 
plt.xlabel('Sepal Length')
plt.ylabel('Petal Width')
plt.suptitle('Sepal Length v Petal Width', fontsize = 12) 
plt.savefig('scatPlotSL_v_PW.png')

plt.figure()
sns.scatterplot(data=data, x=data['SepalLength_cm'], y=data['PetalLength_cm'],hue = data['Class']) 
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.suptitle('Sepal Length v Petal Length', fontsize = 12) 
plt.savefig('scatPlotSL_v_PL.png')

plt.figure()
sns.scatterplot(data=data, x=data['PetalLength_cm'], y=data['PetalWidth_cm'], hue = data['Class'])
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.suptitle('Petal Length v Petal Width', fontsize = 12) 
plt.savefig('scatPlotPL_v_PW.png')

plt.figure()
sns.scatterplot(data=data, x=data['PetalLength_cm'], y=data['SepalWidth_cm'], hue = data['Class']) 
plt.xlabel('Petal Length')
plt.ylabel('Sepal Width')
plt.suptitle('Petal Length v Sepal Width', fontsize = 12) 
plt.savefig('scatPlotPL_v_SW.png')

plt.figure()
sns.scatterplot(data=data, x=data['SepalWidth_cm'], y=data['PetalWidth_cm'], hue = data['Class']) 
plt.xlabel('Sepal Width')
plt.ylabel('Petal Width')
plt.suptitle('Sepal Width v Petal Width', fontsize = 12) 
plt.savefig('scatPlotSW_v_PW.png')

