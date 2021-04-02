# Final program that outputs a summary of each variable to a single text file,
# saves a histogram of each variable to png files, 
# and outputs a scatter plot of each pair of variables.

# Author: Conor McCaffrey

import numpy as np
import pandas as pd
import sys
import matplotlib as mpl
import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches # needed for waffle charts

# Upload our dataset and add some structure to it. I've wrapped this in a try/except block to demonstrate knowledge and also to 
# confirm to the user the upload was successful
try:
    data = pd.read_csv('iris.data', header=None)  # reading in the data file 
    data.columns = ['SepalLength_cm','SepalWidth_cm','PetalLength_cm','PetalWidth_cm','Class'] # adding column names to files
except BaseException as Exception:
    print('We have hit a snag, try that again')
else:
    print('Upload of dataset successful') # to confirm that we have uploaded the dataset without any issues.


# Output a txt file that summarises each variable through various attributes

original_stdout = sys.stdout # Save a reference to the original standard output

with open('variablesSummary.txt', 'w') as text_file: # creating a new .txt file called 'variablesSummary.txt' to store our results and referring to it as 'text_file'
    sys.stdout = text_file # Change the standard output to the file we have just created.  (idea adapted from Stack Abuse (see reference 7))
    print(data.info(), '\n') # print basic info on our dataset such as structure and datatypes, end with a newline character to separate next set of data
    print("Instances of each sample type") # for clarity
    print(data["Class"].value_counts(), '\n') # Number of instances in each class (obtained from reference 8)
    print(data.head(8), '\n') # print 8 top rows in dataset
    print(data.sample(20), '\n')  # print 20 random samples
    print(data.describe(), '\n') # This will output basic exploratory analyses (statistial summaries) of the dataset.
    print(data.corr()) # This will display the correlation betweeen each variable
    

sys.stdout = original_stdout # Reset the standard output to its original value to avoid adding data we dont want to newly created file

