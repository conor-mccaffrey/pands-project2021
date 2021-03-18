
import pandas as pd

# Upload our dataset and add some structure to it
data = pd.read_csv('iris.data', header=None)  # reading in the data file 
data.columns = ['SepalLength_cm','SepalWidth_cm','PetalLength_cm','PetalWidth_cm','Class'] # adding column names to files using examples as seen in https://stackoverflow.com/questions/35415241/adding-column-names-to-csv-file-python
#print(data) # to confirm that we have uploaded the dataset without any issues

# carrying out some basic functions to test the flexibility of the dataset (i.e to manipulations)
print(data.head(8))  # obtained from https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/  printing top 8 rows
print(data.sample(20))  # obtained from https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ printing 20 random samples
print(data.shape) # finding out more attributes of the dataset structure, this time the number of rows and columns (this also works in verifying we have all the data)