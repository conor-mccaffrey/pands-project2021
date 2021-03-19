# Output a txt file that summarises each variable through various attributes
import os
import sys
import pandas as pd

from uploadDataSet import data  # found this idea on kite.com (importing the output of one Python file into another Python file)


original_stdout = sys.stdout # Save a reference to the original standard output
'''
with open('variablesSummary.txt', 'w') as text_file:
    sys.stdout = text_file # Change the standard output to the file we have just created.  (idea adapted from Stack Abuse (see reference 7))
    print("The differenty classes of Iris are", data.groupby('Class').size())
    print(data.describe())#
    print(data.corr()) #
    print(data.head(8)) # print 8 top rows in dataset
    print(data.sample(20))  # print 20 random samples
    print(data.shape) # finding out more attributes of the dataset structure, this time the number of rows and columns (this also works in verifying we have all the data)
    sys.stdout = original_stdout # Reset the standard output to its original value to avoid adding data we dont want to newly created file

'''

#print(data.info())
#print(data.isnull().sum())

