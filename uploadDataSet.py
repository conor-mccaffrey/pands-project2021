# pands-project2021
# Programming and Scripting 2021
# Author : Conor McCaffrey

import pandas as pd

# Upload our dataset and add some structure to it
names = ['SepalLength','SepalWidth','PetalLength','PetalWidth','Class'] # from researching the dataset, I found what each column of data represents and wanted to reflect this in the dataset
data = pd.read_csv('iris.data', names = names)  # reading in the data file and applying our column names
print(data.head())