# Output a txt file that summarises each variable through various attributes
import os
import sys
import pandas as pd

#from uploadDataSet import data  # found this idea on kite.com (importing the output of one Python file into another Python file)
'''
with open('variablesSummary.txt', 'w') as text_file:
    print("The differenty classes of Iris are", data.groupby('Class').size(), file=text_file)
    print(data.describe(), file=text_file)
    print(data.corr(), file=text_file)
   # print(sum_data)
'''
try:
    data = pd.read_csv('iris.data', header=None)  # reading in the data file 
    data.columns = ['SepalLength_cm','SepalWidth_cm','PetalLength_cm','PetalWidth_cm','Class'] # adding column names to files
except BaseException as Exception:
    print('We have hit a snag, try that again')
else:
    print('Upload of dataset successful') # to confirm that we have uploaded the dataset without any issues
    #print(data.head(8)) 
    #print(data.sample(20))  
    #print(data.shape)


original_stdout = sys.stdout # Save a reference to the original standard output

with open('variablesSummary.txt', 'w') as text_file:
    sys.stdout = text_file # Change the standard output to the file we created.
    print("The differenty classes of Iris are", data.groupby('Class').size())
    print(data.describe())
    print(data.corr())
    sys.stdout = original_stdout # Reset the standard output to its original value

print ('hello')