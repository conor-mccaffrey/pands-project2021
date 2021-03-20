# Output a txt file that summarises each variable through various attributes

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt


from uploadDataSet import data  # found this idea on kite.com (importing the output of one Python file into another Python file).
# This wont be needed when compiling the final program but it's good to have now when performing separate tasks


original_stdout = sys.stdout # Save a reference to the original standard output

with open('variablesSummary.txt', 'w') as text_file: # creating a new .txt file called 'variablesSummary.txt' to store our results and referring to it as 'text_file'
    sys.stdout = text_file # Change the standard output to the file we have just created.  (idea adapted from Stack Abuse (see reference 7))
    print(data.info(), '\n') # print basic info on our dataset such as structure and datatypes, end with a newline character to separate next set of data
    print("Instances of each sample type") 
    print(data["Class"].value_counts(), '\n') # Number of instances in each class (obtained from reference 8)
    print(data.head(8), '\n') # print 8 top rows in dataset
    print(data.sample(20), '\n')  # print 20 random samples
    print(data.describe(), '\n') # This will output basic exploratory analyses (statistial summaries) of the dataset.
    print(data.corr()) # This will display the correlatiopn betweeen 
    
sys.stdout = original_stdout # Reset the standard output to its original value to avoid adding data we dont want to newly created file



