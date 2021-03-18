import numpy as np
import pandas as pd
import sys
import matplotlib as mpl
import os
import matplotlib.pyplot as plt
from PIL import Image # this lets us convert images into arrays
import matplotlib.patches as mpatches # needed for waffle charts


# Upload our dataset and add some structure to it
data = pd.read_csv('iris.data', header=None)  # reading in the data file 
data.columns = ['SepalLength_cm','SepalWidth_cm','PetalLength_cm','PetalWidth_cm','Class'] # adding column names to files
#print(data) # to confirm that we have uploaded the dataset without any issues

# carrying out some basic functions to test the flexibility of the dataset (i.e to manipulations)
#print(data.head(8))  
#print(data.sample(20))  
#print(data.shape) # finding out more attributes of the dataset structure, this time the number of rows and columns (this also works in verifying we have all the data)