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
'''
sepallengthhist, axes = plt.subplots(figsize=(10,8))
data['SepalLength_cm'].plot(kind='hist',color='blue')
plt.xlabel("Sepal Length")
plt.grid(True)
plt.savefig("23_sepallengthhist")
'''

data['SepalLength_cm'].plot(kind = 'hist')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()