import numpy as np
import pandas as pd
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt


# Upload our dataset and add some structure to it. I've wrapped this in a try/except block to demonstrate knowledge and also to 
# confirm to the user the upload was successful
try:
    data = pd.read_csv('iris.data', header=None)  # reading in the data file 
    data.columns = ['SepalLength_cm','SepalWidth_cm','PetalLength_cm','PetalWidth_cm','Class'] # adding column names to files
except BaseException as Exception:
    print('We have hit a snag, try that again')
else:
    print('Upload of dataset successful') # to confirm that we have uploaded the dataset without any issues.
