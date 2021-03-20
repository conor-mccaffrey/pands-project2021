# Project for Programming and Scripting module GMIT 2021 (pands-project 2021)
## Author : Conor McCaffrey
![Iris_Flower](https://i.imgur.com/v3zQOXw.jpg)

The Iris Flower [source = Dr Shahin Rostam, 2020. Part 1 - Dataset Analysis. [Online]. [17 March 2021]. Available from: https://datacrayon.com/posts/machine-learning/ml-with-kaggle/machine-learning-with-kaggle-kernels-part-1/ ] 

## Introduction 
This README file will serve as both an introduction to Fisher's Iris Dataset and as evidence of the applicability of Python in investigating datasets. I also intend to use this README file as a tool, demonstrating my thought process for using certain attributes, methodologies and functions when describing the data. The main goal here is to be able to demonstrate the knowledge I have gained throughout the module and use this knowledge to be able to discern information from the Iris Dataset.

I have structured the README file as follows:

    1. Overview of the Iris Dataset (background, application to Python)
    2. Investigation of the Fisher's Iris Data Set
    3. Conclusion
    4. References

## Overview of Iris Dataset, it's attributes, and it's application to Python

The Iris Fisher Dataset was first created in 1936 by Sir Ronald Aylmer Fisher [1]. The dataset was desribed in his landmark paper 'The Use of Multiple Measurements in Taxonomic Problems' (1936), attibuting the actual collection of the data to Dr. Edgar Anderson [1]. The Iris Dataset is essentially a multivariate dataset, containing 150 measurements of iris petal and sepal lengths and widths, with 50 measurements for each of the species 'setosa','versicolor' and 'virginica' [2]. It is important to note that these measurements are in centimetres (cm). One class (sertosa) is linerally separable from the other two classes [3].

The measurements obtained were used to create a linear discriminant model to classify the species [4]. The dataset has become commonplace in computer science, in particlar pattern recognition literature [3]. The Iris Fischer Dataset has been used for data analyses so frequently that it can be accessed without needing to find a source, through both R and Python in the machine-learning (ML) package Scikit-learn [5]

![1_uo6VfVH87jRjMZWVdwq3Vw](https://i.imgur.com/UJsxRwe.png)

Overview of Petal and Sepal on Iris Flower [Source = https://medium.com/@Nivitus./iris-flower-classification-machine-learning-d4e337140fa4]

I intend to use this dataset to demonstrate my knowledge of Python, gained throughout the module. I will, in particular, be using the Pandas, Numpy, Matplotlib and perhaps Seabron modules throughout the project. These modules will be installed when required.

The overall goal is to use these modules (and by extension, Python) to describe the Iris dataset in detail and, display visually, certain attributes of the data which I believe are important to highlight. By doing this I will also, in essence, provide evidence of the suitability of Python towards analysing large datasets.

## Investigation of the Fisher's Iris Data Set  

### Project Plan

To maintain structure and organisation during the project, I have set out a project plan for the investigation of the data-set. This is to ensure focus during the project and to avoid going down any rabbit holes.

    1. Create a repository on GitHub which I will clone onto Visual Studio as outlined during Week01 of the module, using SSH. I will call the repository 'pands-project2021' as requested.
    2. I will download the data for Fisher's Iris Data Set from the UCI Machine Learning Repository (http://archive.ics.uci.edu/ml/datasets/Iris) and add it to my repository using the Pandas 'read_csv' atttribute.
    3. I will carry out exploratory research on the dataset to familiarise myself with the data and it's potential for Python analysis and reference all items I extract information from.
    4. I will then consider what type of analysis is relavant for this data set and investigate how to carry it out, drawing on various resources which will be references. This work will be stored in various different files.
    5. I will update the README file as I progress, and then compile all my work into a program called 'analysis.py'

### Importing Libraries

To begin, I first imported the libraries I believed would be beneficial to visually describing the dataset.

```Python
import numpy as np
import pandas as pd
import sys
import matplotlib as mpl
import os
import matplotlib.pyplot as plt
import seaborn as sbn
from PIL import Image # this lets us convert images into arrays
import matplotlib.patches as mpatches # needed for waffle charts
```
The libraries I imported are all quite standard for data visualisation, with perhaps Image (from PIL) (6) and matplotlib.patches being the exception. I have imported these module to have the option of creating arrays from images and waffle charts. I will decide later in the project if they are needed or not but just to have the option.



#### Download and Addition of Dataset to Repository

The CSV file of the Iris Fisher Dataset was retrieved from the UCI Machine Learning Repository and saved locally (3). The CSV file was read into our repository usind the Pandas 'read_csv' method. Column names were added in order to provide some structre to the dataset to faciliate downstream manipulations. I also added 'cm' to each column name just to highlight the measurement were made in centimetres when compiling the data. I added this block of code in a try/except block to demonstrate further learning and also to confirm to the user their upload was successful.

```Python
# Upload our dataset and add some structure to it (wrapped in try/except block)
try:
    data = pd.read_csv('iris.data', header=None)  # reading in the data file 
    data.columns = ['SepalLength_cm','SepalWidth_cm','PetalLength_cm','PetalWidth_cm','Class'] # adding column names to files
except BaseException as Exception:  # a blanket approach for catching errors, not the best way normally but sufficent in this scenario I believe
    print('We have hit a snag, try that again')
else:
    print('Upload of dataset successful') # to confirm that we have uploaded the dataset without any issues
    
```
I thought of including some commented-out code that I could use to verify the dataset was read in correctly. These were simple data manipulations to test the robustness of the data to user queries. For example, 'data.head(8)' would print out the top 8 rows of our data. Prior knowledge of the datset structure allows this function to confirm you have uploaded the dataset correctly. I then decided instead to wrap the code in a try/except block and move the code I was going to use into the 'variablesSummary.py' file for neatness.

#### Exploratory analysis of the Iris Fisher Dataset

Now it is time to gain a high-level understanding of the data we have. The logical first step here then is to investigate the structure of our data and to calculate general statistical features such as mean, standard deviation, max/min values and interquartile ranges. We will also look at testing the robustness of our data in order to confirm we can carry out queries on the dataset. I included the newline character after each 'print' function in order to spearate the data to make it neater for the end-user.

```Python

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
```
I have added a lot of commments in order to describe step-by-step the working of the program 'variablesSummary.py'. There are some main points to highlight.
I began by changing the standard output (adapted from reference 7) so that our code would re-direct to a newly created file called 'variablesSummary.txt'. I then made sure to reset the standard output at the end of our program. I called the 'info()' method in order to discern basic structural information from our dataset. This includes the number of columns/rows, the datatypes present and also, importantly, the presence/absence of NULL values in our data. I called the '.value_counts()' method to confirm the number of values in each grouping. The 'describe()' method provides a tabular summary of basic statistical features which will be explained in greater detail later in the section.

The 'corr()' method is an extra piece of information I thought to be important to include as it tells us how correlated secitons of our data is, i.e does an increase in one parameter result in an increase (positive correlation) or a decrease (negative correlation) in another parameter (9). In theory:
* '1' is total positive correlation
* '0' is no linear correlation
* '-1' is total negative coorelation

##### Basic Structural Information of Dataset

To begin, I wanted to find out the basic structure, datatypes and general information on the dataset:

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column          Non-Null Count  Dtype  
---  ------          --------------  -----  
 0   SepalLength_cm  150 non-null    float64
 1   SepalWidth_cm   150 non-null    float64
 2   PetalLength_cm  150 non-null    float64
 3   PetalWidth_cm   150 non-null    float64
 4   Class           150 non-null    object 
dtypes: float64(4), object(1)
memory usage: 6.0+ KB
None 

Instances of each sample type
Iris-setosa        50
Iris-virginica     50
Iris-versicolor    50
Name: Class, dtype: int64 

```
We can see from the resulting text that we have 150 entries and 5 columns. The values are of type 'float' and we have no NULL values, which is an important piece of information to know as otherwise are results could be skewed. The second set of data tells us we have 50 values for each class, which does not come as a surprise as we previously knew we have 150 entries, but it is always good to confirm.

##### Verification of the success of basic data manipulations
In order to verify that simple manipulations could be carried out on our dataset, I called the 'head()' and 'sample()' methods. The 'head()' method prints out the top rows in the dataset, depending on the argument you pass through. The 'sample()' method returns a random sleection of the data

```

   SepalLength_cm  SepalWidth_cm  PetalLength_cm  PetalWidth_cm        Class
0             5.1            3.5             1.4            0.2  Iris-setosa
1             4.9            3.0             1.4            0.2  Iris-setosa
2             4.7            3.2             1.3            0.2  Iris-setosa
3             4.6            3.1             1.5            0.2  Iris-setosa
4             5.0            3.6             1.4            0.2  Iris-setosa
5             5.4            3.9             1.7            0.4  Iris-setosa
6             4.6            3.4             1.4            0.3  Iris-setosa
7             5.0            3.4             1.5            0.2  Iris-setosa 

     SepalLength_cm  SepalWidth_cm  PetalLength_cm  PetalWidth_cm            Class
59              5.2            2.7             3.9            1.4  Iris-versicolor
74              6.4            2.9             4.3            1.3  Iris-versicolor
110             6.5            3.2             5.1            2.0   Iris-virginica
26              5.0            3.4             1.6            0.4      Iris-setosa
78              6.0            2.9             4.5            1.5  Iris-versicolor
76              6.8            2.8             4.8            1.4  Iris-versicolor
27              5.2            3.5             1.5            0.2      Iris-setosa
42              4.4            3.2             1.3            0.2      Iris-setosa
105             7.6            3.0             6.6            2.1   Iris-virginica
139             6.9            3.1             5.4            2.1   Iris-virginica
19              5.1            3.8             1.5            0.3      Iris-setosa
4               5.0            3.6             1.4            0.2      Iris-setosa
120             6.9            3.2             5.7            2.3   Iris-virginica
124             6.7            3.3             5.7            2.1   Iris-virginica
9               4.9            3.1             1.5            0.1      Iris-setosa
30              4.8            3.1             1.6            0.2      Iris-setosa
13              4.3            3.0             1.1            0.1      Iris-setosa
126             6.2            2.8             4.8            1.8   Iris-virginica
46              5.1            3.8             1.6            0.2      Iris-setosa
7               5.0            3.4             1.5            0.2      Iris-setosa 

```

We can see that the methods worked as expected from analysing the 'ID' numbers. The top 8 rows were printed from our first method and a 20 random samples were printed from our second method.

##### Summary of each Variable in the Iris Fisher Dataset
This step is the 'meat' of the first section in our project. I used the 'describe()' method in order to retieve a tabulated statistical summary of our data. The main points of interest for me are the mean, standard deviation (std), the minimum value (min) and the maximum value(max). I have also called the 'corr()' method in order to determine if there is an correlation between certain parameters of our data (as described in the earlier section)

````
       SepalLength_cm  SepalWidth_cm  PetalLength_cm  PetalWidth_cm
count      150.000000     150.000000      150.000000     150.000000
mean         5.843333       3.054000        3.758667       1.198667
std          0.828066       0.433594        1.764420       0.763161
min          4.300000       2.000000        1.000000       0.100000
25%          5.100000       2.800000        1.600000       0.300000
50%          5.800000       3.000000        4.350000       1.300000
75%          6.400000       3.300000        5.100000       1.800000
max          7.900000       4.400000        6.900000       2.500000 

                SepalLength_cm  SepalWidth_cm  PetalLength_cm  PetalWidth_cm
SepalLength_cm        1.000000      -0.109369        0.871754       0.817954
SepalWidth_cm        -0.109369       1.000000       -0.420516      -0.356544
PetalLength_cm        0.871754      -0.420516        1.000000       0.962757
PetalWidth_cm         0.817954      -0.356544        0.962757       1.000000

````

The take-away points of this are:

* We have 150 values (counts) for each class, this tells us all data has been read into the calculation based on our previous results.
* The mean values of Sepal length and Sepal width are higher than their Petal counterparts. This would immediately suggest that Sepals are larger than Petals.
* The standard deviations of the Sepal length and Sepal width are quite lower than the Petal length and Petal width results. This suggests that despite the higher values for Sepals, there is more variance within the Petal results. This gives me greater confidence in the significance of our findings for the 'mean' results.
* The min/max values tie in with our hypothesis now that Sepals are larger than Petals
* We can see that there is a strong positive coorelation between Petal length and Petal width and no real correlation between Sepal length and Sepal width. This suggests that any major insights we find might be related to petals more so than sepals. We will see later on. 

## Conclusion

## References
    1. Yong, Cui 2020. The Iris Dataset — A Little Bit of History and Biology. [Online]. [17 March 2021]. Available from: https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5
    
    2. Dam, Kerstin & Hafen, Ryan & Gibson, Tara & Critchlow, Terence. (2013). Power Grid Data Analysis with R and Hadoop. 10.1016/b978-0-12-411511-8.00001-3.
   
    3. Marshall, Michael 2019. Iris Data Set. [Online]. [17 March 2021]. Available from: http://archive.ics.uci.edu/ml/datasets/Iris
    
    4. Santos, Rafael. 2019. Data Science Example - Iris dataset. [Online]. [17 March 2021]. Available from: http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html
    
    5. Dphansen (N.D.). Iris demo data set for tutorials - SQL machine learning. [online] docs.microsoft.com. Available at: https://docs.microsoft.com/en-us/sql/machine-learning/tutorials/demo-data-iris-in-sql?view=sql-server-ver15 [Accessed 17 Mar. 2021].
    
    6. Readthedocs.io. (2011). Image Module — Pillow (PIL Fork) 6.2.1 documentation. [online] Available at: https://pillow.readthedocs.io/en/stable/reference/Image.html.
    
    7. Stack Abuse. Writing to a File with Python’s print() Function. [online] Available at: https://stackabuse.com/writing-to-a-file-with-pythons-print-function/ [Accessed 18 Mar. 2021] 
    
    8. Avuluri, V.S.R. (2019). Exploratory Data Analysis of IRIS Data Set Using Python. [online] Medium. Available at: https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d [Accessed 20 Mar. 2021].
    
    9. kaggle.com. Simple analysis of Iris dataset. [online] Available at: https://www.kaggle.com/danalexandru/simple-analysis-of-iris-dataset [Accessed 20 Mar. 2021].




 

 

‌



