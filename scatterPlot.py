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
sns.set_style("darkgrid") # adapted from StackOverflow (reference 19)
sns.scatterplot(data=data, x=data["SepalLength_cm"], y=data["SepalWidth_cm"], hue=data['Class']) #setting properties of plot (reference 20)