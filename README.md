# Project for Programming and Scripting module GMIT Data Analytics 2021 (pands-project 2021)
## Author : Conor McCaffrey
![Iris_Flower](https://i.imgur.com/v3zQOXw.jpg)

The Iris Flower [source = Dr Shahin Rostam, 2020. Part 1 - Dataset Analysis. [Online]. [17 March 2021]. Available from: https://datacrayon.com/posts/machine-learning/ml-with-kaggle/machine-learning-with-kaggle-kernels-part-1/ ] 

## Introduction 
This README file will serve as both an introduction to Fisher's Iris Dataset and as evidence of the applicability of Python in investigating datasets. I also intend to use this README file as a resource, demonstrating my thought process for using certain attributes, methodologies and functions when describing the data. The main goal here is to be able to demonstrate the knowledge I have gained throughout the module and use this knowledge to be able to discern information from the Iris Dataset.

I have structured the README file as follows:

    1. Overview of the Iris Dataset (background, application to Python)
    2. Investigation of the Fisher's Iris Data Set
    3. Conclusion
    4. References

## 1) Overview of Iris Dataset, it's attributes and it's application to Python

The Iris Fisher Dataset was first created in 1936 by Sir Ronald Aylmer Fisher (1). The dataset was described in his landmark paper 'The Use of Multiple Measurements in Taxonomic Problems' (1936), attributing the actual collection of the data to Dr. Edgar Anderson (1). The Iris Dataset is essentially a multivariate dataset, containing 150 measurements of iris petal and sepal lengths and widths, with 50 measurements for each of the species 'setosa','versicolor' and 'virginica' (2). It is important to note that these measurements are in centimetres (cm). One class (sertosa) is linerally separable from the other two classes (3). We will display this fact through Python in our investigation. 

The measurements obtained were used to create a linear discriminant model to classify the species (4). The dataset has become commonplace in computer science, in particlar pattern recognition literature and data visualisations (3). The Iris Fisher Dataset has been used for data analyses so frequently that it can be accessed without needing to find a source, through both R and Python in the machine-learning (ML) package Scikit-learn (5). Further demonstrating the modern application of the Iris dataset, it is being increasingly incorporated into advances in machine learning (ML) teachings (10,11). 

![1_uo6VfVH87jRjMZWVdwq3Vw](https://i.imgur.com/UJsxRwe.png)

Overview of Petal and Sepal on Iris Flower [Source = https://medium.com/@Nivitus./iris-flower-classification-machine-learning-d4e337140fa4]

I intend to use this dataset to demonstrate my knowledge of Python, gained throughout the module. I will, in particular, be using the Pandas, Numpy, Matplotlib and perhaps Seabron modules throughout the project. These modules will be installed when required.

The overall goal is to use these modules (and by extension, Python) to describe the Iris dataset in detail and, display visually, certain attributes of the data which I believe are important to highlight. By doing this I will also, in essence, provide evidence of the suitability of Python towards analysing large datasets.

## 2) Investigation of the Fisher's Iris Data Set  

### Project Plan

To maintain structure and organisation during the project, I have set out a project plan for the investigation of the data-set. This is to ensure focus during the project and to avoid going down any rabbit holes.

    1. Create a repository on GitHub which I will clone onto Visual Studio as outlined during Week01 of the module, using SSH. I will call the repository 'pands-project2021' as requested.
    2. I will download the data for Fisher's Iris Data Set from the UCI Machine Learning Repository (http://archive.ics.uci.edu/ml/datasets/Iris) and add it to my repository using the Pandas 'read_csv' atttribute.
    3. I will carry out exploratory research on the dataset to familiarise myself with the data and it's potential for Python analysis and reference all items I extract information from.
    4. I will then consider what type of analyses is relavant for this data set and investigate how to carry it out, drawing on various resources which will be referenced. This work will be stored in various different files.
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
import seaborn as sns
import plotly.express as px
from pywaffle import Waffle
```
The libraries I imported are all quite standard for data analyses and visualisation. I have imported these modules to have the option of creating arrays from images and waffle charts. I considered importing modules such as Image (from PIL (6)) but then decided not to as I couldn't truely justify it's applicibality towards this dataset. I will decide later in the project if they are needed or not but just to have the option.

### Download and Addition of the Dataset to Repository


The CSV file of the Iris Fisher Dataset was retrieved from the UCI Machine Learning Repository and saved locally (3). The CSV file was read into our repository using the Pandas 'read_csv' method. Column names were added in order to provide some structure to the dataset to faciliate downstream manipulations. I also added 'cm' to each column name just to highlight the measurements were made in centimetres when compiling the data. I added this block of code in a try/except block to demonstrate further learning and also to confirm to the user their upload was successful.

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

### Exploratory analysis of the Iris Fisher Dataset

Now it is time to gain a high-level understanding of the data we have. The logical first step here then is to investigate the structure of our data and to calculate general statistical features such as mean, standard deviation, max/min values and interquartile ranges. We will also look at testing the robustness of our data in order to confirm we can carry out queries on the dataset. I included the newline character after each 'print' function in order to spearate the data to make it neater for the end-user.

```Python
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

The 'corr()' method is an extra piece of information I thought to be important to include as it tells us how correlated secitons of our data is, i.e does an increase in one parameter result in an increase (positive correlation) or a decrease (negative correlation) in another parameter (9). I will construct a heatmap in a later section in order to visualy examine the correlations between parameters. In theory:
* '1' is total positive correlation
* '0' is no linear correlation
* '-1' is total negative coorelation

#### *Basic Structural Information of Dataset*

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
We can see from the resulting text that we have 150 entries and 5 columns. The values are of type 'float' and we have no NULL values, which is an important piece of information to know as otherwise our results could be mis-represented. The second set of data tells us we have 50 values for each class, which does not come as a surprise as we knew we had 150 entries, but it is always good to confirm.

#### *Verification of the success of basic data manipulations*
In order to verify that simple manipulations could be carried out on our dataset, I called the 'head()' and 'sample()' methods. The 'head()' method prints out the top rows in the dataset, depending on the argument you pass through. The 'sample()' method returns a random selection of the data.

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

#### *Summary of each Variable in the Iris Fisher Dataset*
This step is the 'meat' of the first section in our project. I used the 'describe()' method in order to retieve a tabulated statistical summary of our data. The main points of interest for me are the mean, standard deviation (std), the minimum value (min) and the maximum value(max). I have also called the 'corr()' method in order to determine if there is an correlation between certain parameters of our data (as previously described)

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
* The median values (50%) suggests the distibution in the Sepal data may be slightly positively skewed with perhaps negative skew being displayed in the Petal data but later analyses will reveal more on this.
* We can see that there is a strong positive coorelation between Petal length and Petal width and no real correlation between Sepal length and Sepal width. This suggests that any major insights we find might be related to petals more so than sepals. We will see later on. 
  
### Visualisation of the Iris Fisher Dataset

#### *Simple Waffle Chart of Species*

Just to aid in the visualisation of the datset, I constructed a simple waffle chart demonstrating the distribution of the dataset betweeen each species type. The code was developed from reference 27 (27).

```Python
df = pd.DataFrame({
    'iris_Type': ['Setosa', 'Virginica', 'Versicolor'],
    'Frequency': [50, 50, 50]
})


fig = plt.figure(
    FigureClass=Waffle, 
    rows=5,
    values=df.Frequency,
    labels=list(df.iris_Type),
    legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)}

)

plt.savefig('waffleChart.png')
```

![waffleChart](https://i.imgur.com/ZFB3D22.png)

There is no new information to be garnered here, merely visualtion that we have an equal quantity of each of the iris species. 

#### *Analysis of each variable through Histograms*

The next step is to be able to visually inspect our data. To achieve this, histograms of each variable (Sepal length/width, Petal length/width) were created. The histograms displayed the ranges (in cm) of each variable plotted against the frequencies. This provides additional information about the distribution of the data across each variable. An example of the code is as follows : 

```Python

sns.displot(data['SepalLength_cm'], kde= False, bins = 15, color = 'green', edgecolor = 'orange', alpha=0.6) # setting kde as False in order to remove the density line as it is not relavant to task
# also altered alpha value to change transparency of the graph (adapted from Reference 13)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.suptitle('Sepal Length', fontsize = 12) # adding main title to histogram and setting fontsize
plt.ylim(0,25) # setting y-axis limits
plt.xlim(3,10) # setting x-axis limits
plt.grid(ls = '--', lw = '0.1', color = '#BEBEBE', axis = 'y') # modifying grid lines so that they dont 'overpower' the data and used hex value for colour
plt.savefig('sepalLengthHist.png') # saving output to specified .png file

```
I leaned heavily on Seaborn and Matplotlib libraries for creating the histograms. I edited the features in order to make the histograms more aesthetically pleasing and therefore more accessible for the end-user. I set different axes limits for each histogram to aid their appearance. I removed the density line as it is not requested for the task and changed the 'alpha' setting (from it's default of 0.5) to alter the transparancy of the graph.

#### *Histogram Analyses*
![sepalLengthHist](https://i.imgur.com/i6X0u9V.png)
![sepalWidthHist](https://i.imgur.com/GVth4Dv.png)
![petalLengthHist](https://i.imgur.com/ik8Ffd7.png)![petalWidthHist](https://i.imgur.com/ouqGiWe.png)


The above histograms display the results for Sepal and Petal data. It is immediately noticable that the tabular statistical summary we produced earlier does not tell the full story and the benefits of the histograms are clear. We can see how the distribution of the data differs between Sepal and Petal. This ties in with our findings on the standard deviation in the statistical summary. The data variance is much less pronounced in the Sepal data. We can clearly see outliers in the Petal data which may warrent further invesitgation down the line. These outliers in Petal data may be skewing the mean and median also to an extent. The Sepal width data depicts what appears to be almost perfect Gaussian distibution. This is unsurprising as the Sepal width data also has the lowest value for standard deviation. 

#### *Subplot of all histograms in Dataset*

For clarity's sake, I also compiled a program that would display histograms of all the variants so far in one output. This can be good for a quick overview of the data. 

```Python
data.hist(figsize = (9,6))
plt.savefig('overviewHist.png')

```

![overviewHist](https://i.imgur.com/zl9CzW8.png)

The take-away points of this are:
*  The Petal data has a lot more variance than the Sepal data 
*  We may have outliers present in the Petal data that are skewing the distribution of the data 

#### *Correlation Map of Data for Statistical Summary* 

In order to aid in the visualisation of the correlation data from our 'variablesSummary.txt' output, it is wise to construct a heatmap of the correlation data. This was heavily drawn on 'Seaborn.pydata.org' (reference 14). The resulting heatmap provides a visual summary of the 'corr()' method output previously attained.

```Python

# information generated from reference 14
correlationVariablePlot = plt.subplots(figsize=(8,8)) # setting size of output
# setting attributes of correlation heatmap
correlationVariablePlot =sns.heatmap(data.corr(), annot=True, cmap='rainbow' ,square=True, cbar = True, linecolor='green', robust= True)  
plt.savefig("correlationPlot.png") # save output to 'correlationPlot.png'
```

![correlationPlot](https://i.imgur.com/Ur6GT5i.png)

There is no new information here that we are not aware of previously, but it does help us confirm the strong positive coorelation between Petal length and Petal width. It also seems there may be a slight positive correlation between Sepal length and Petal length.

#### *Test for Outliers*

As a result of the earlier discussion regarding the potential presence of outliers, it is prudent to attempt to confirm if indeed outliers are present within our dataset. We will not exclude any potential outliers from later analyses but it may help our thinking in later sections. Boxplots and swarmplots (to allow greater inspection of datapoints) were constructed for each variable, adapted from DEV Community (15). 

```Python
fig, axes = plt.subplots(2, 2, figsize=(12, 12)) # setting layout and size of plts. 
fig.suptitle('Boxplots of Iris Fisher Data Variables', style = 'italic') # Overall title and editing font for appearance

sns.boxplot(ax=axes[0 ,0], data=data['SepalLength_cm'], x=data['Class'], y=data['SepalLength_cm'], showfliers=False)  # setting axes, boxplot position
sns.swarmplot(ax=axes[0 ,0], data=data['SepalLength_cm'], x=data['Class'], y=data['SepalLength_cm'], color = '#554444', s=4) # constructing swarmplot as per reference 16
sns.boxplot(ax=axes[0 ,1], data=data['SepalWidth_cm'], x=data['Class'], y=data['SepalWidth_cm'], showfliers=False) # setting axes, boxplot position
sns.swarmplot(ax=axes[0 ,1], data=data['SepalWidth_cm'], x=data['Class'], y=data['SepalWidth_cm'], color = '#0D0D0D', s=4) # adding properties to swarmplot
sns.boxplot(ax=axes[1 ,0], data=data['PetalLength_cm'], x=data['Class'], y=data['PetalLength_cm'], showfliers=False) # setting axes, boxplot position
sns.swarmplot(ax=axes[1 ,0], data=data['PetalLength_cm'], x=data['Class'], y=data['PetalLength_cm'], color = '#943126', s=4)
sns.boxplot(ax=axes[1 ,1], data=data['PetalWidth_cm'], x=data['Class'], y=data['PetalWidth_cm'], showfliers=False) # setting axes, boxplot position
sns.swarmplot(ax=axes[1 ,1], data=data['PetalWidth_cm'], x=data['Class'], y=data['PetalWidth_cm'], color = '#0E6655', s=4)
plt.savefig('boxplots.png') # save output to new file
```
The code used for constructing the boxplots and swamplots were adapted from reference 15 and 17. We edited the properties of the boxplot through consultation of 'seaborn.pydata.org' (16). Boxplots and swarmplots, used concurrently, are an extremely effective method of visualising outliers. We can immediately identify datapoints that lie outside the range of ??1.5 * interquartile range (IQR), thereby allowing classification as an outlier (18).

![boxplots](https://i.imgur.com/A03TrtN.png)

We can see outliers are present in each of our variables. The iris-Virginica class contains the most pronounced outliers in Sepal width and Sepal length. We can also see the wide variance in the Virginica data across each variable. The iris-Setosa data is interesting in the fact that the Petal data is compact (excluding the two outliers in each variable) but varied in Sepal data. There is also a clear distinction in the size of Petals in the class 'Setosa' compared to the other two classes. We can also see the wide variance of the Sepal data in general, owing in part to their larger size.

#### *Scatterplots of each pair of variables*
The next step in our project is to be able to visualise each pair of variables through scatterplot analyses. Scatterplots hold some advantage over boxplots in the fact they are more visually accessible. Scatterplots facilitate the inspection of datapoints in a more detailed manner than histograms. The code to construct the scatterplots is shown below. The Plotly library was used for construction of each scatterplot. I feel the aesthetics of Plotly are nicer than both matplotlib and Seaborn. The Plotly library was installed in the same manner ('pip install') as other libraries and sourced from 'Plotly.com' (19). The code for constructing each scatter plot was obtained from the same source (20) and adapted to display each pair of variables. I also decided to add histograms for each variable on some of the scatterplots. This gives us an even greater insight into the distribution of datapoints between each species. 

```Python
# using newly imported Plotly library. Setting properties of scatterplot and saving outputs to separate 
# .png files.

fig = px.scatter(data, x='SepalWidth_cm', y='SepalLength_cm', color='Class', 
            template='plotly_dark', title = 'SepalWidth v SepalLength', marginal_x = 'histogram') 
fig.write_image('scatPlotSWSL.png')


fig = px.scatter(data, x='PetalLength_cm', y='SepalWidth_cm', color='Class',
           template='plotly_dark', title = 'PetalLength v SepalWidth', marginal_x = 'histogram')
fig.write_image('scatPlotPLSW.png')

fig = px.scatter(data, x='PetalLength_cm', y='PetalWidth_cm', color='Class',
            template='plotly_dark', title = 'PetalLength v PetalWidth', marginal_y = 'histogram')
fig.write_image('scatPlotPLPW.png')

fig = px.scatter(data, x='SepalLength_cm', y='PetalLength_cm', color='Class',
            template='plotly_dark', title = 'SepalLength v PetalLength', marginal_x = 'histogram')
fig.write_image('scatPlotSLPL.png')

fig = px.scatter(data, x='SepalLength_cm', y='PetalWidth_cm', color='Class',
            template='plotly_dark', title = 'SepalLength v PetalWidth')
fig.write_image('scatPlotSLPW.png')

fig = px.scatter(data, x='SepalWidth_cm', y='PetalWidth_cm', color='Class',
            template='plotly_dark', title = 'SepalWidth v PetalWidth')
fig.write_image('scatPlot_SWPW.png')

```

The resulting outputs (each scatterplot was saved to a separate .png file for easier access) are shown below. In general, we can see the divergence between the setosa class and the virginica/versicolor class more clearly using scatterplots. In Plotly, outputs are generally displayed on a webpage however the output can be redirected to a file saved locally (21). 

![scatPlotSWSL](https://i.imgur.com/Ck45AKO.png)


As will be the theme for all these scatterplots, we can see differences here between the setosa class and the remaining two classes. The difference between versicolor and virginica is negligible. The sepal width of the setosa class is trending higher. This can be confirmed by analysing the accompanying histogram.

![scatPlotSLPW](https://i.imgur.com/lRVPm6e.png)

A much more distinctive separation between setosa and versicolor/virginica is evident in petal length and sepal width. The virginica/versicolor data is slightly interspersed while the setosa data is much more clustered. 

![scatPlotSLPL](https://i.imgur.com/Wra87H6.png)

Once again, the setosa data is clearly divergent from the remaining two classes of Iris flower. The setosa petal/sepal length is smaller than the other two classes. The virginica class appears to have larger sepal/petal lengths, however they are quite similar. Analysis of the histogram data for Sepal Length confirms that the iris setosa is shorter in length. The resulting histogram analysis displays the extent of iris virginica/versicolor inter-relation and the distinction between setosa and the remaining two iris species. 


![scatPlotPLPW](https://i.imgur.com/ZAf2XJT.png)

For the petal data, we can see a clear distinction between the setosa class and the virginica/versicolor class. This ties in with the data we have seen previously. There is more of a distinction between virginica and versicolor here also, with the virginica class or Iris having larger petal attributes.


![scatPlotPLSW](https://i.imgur.com/bSSEUXb.png)

In this plot, we can see the clustering effect of setosa once again. We can also see a wide variance in each of the classes. It is interesting to note the clustering of setosa even when sepal and petal attributes are combined. This gives us greater confidence in the validity of our results. From analysing the histogram for Petal length, it can be seen just how divergent the setosa petal lengths are compared to iris virginica and iris versicolor.

![scatPlot_SWPW](https://i.imgur.com/fSsWYSp.png)

In this final plot, we confirm the clustering of the setosa class or Iris. it is also clear that there is interspersion between the virginica/versicolor classes. We can still gauge that the petal width of the virginica class is trending higher however this is not as pronounced as the setosa data.

The main take-away point here is that we can clearly see the clustering effect of the setosa Iris class when compared to the virginica/versicolor Iris classes. 

#### *Subplot of all Scatterplots*
To facilitate rapid analyses of all scatterplot data, it is wise to construct a program that outputs all scatterplots to a single .png file. To complete this, the Seaborn library was used.

```Python

fig, ax1 = plt.subplots(3,2, figsize=(25,20)) # adapted from kaggle.com (reference 22)
fig.suptitle('Scatterplots of Iris Fisher Data Variables', style = 'italic', size = 25) # Overall title and editing font for appearance

sns.set(font_scale=1.2) # increasing size of legend (23)

# 1st plot
sns.scatterplot(data=data, x='SepalLength_cm', y='SepalWidth_cm', hue='Class', ax=ax1[0, 0]) 
ax1[0,0].set_xlabel('Sepal Length ', fontsize='large', fontweight='bold')
ax1[0,0].set_ylabel('Sepal Width ', fontsize='large', fontweight='bold')

# 2nd plot
sns.scatterplot(data=data, x='SepalWidth_cm', y='SepalLength_cm', hue='Class', ax=ax1[0, 1]) 
ax1[0,1].set_xlabel('Sepal Width ', fontsize='large', fontweight='bold')
ax1[0,1].set_ylabel('Sepal Length ', fontsize='large', fontweight='bold')

# 3rd plot
sns.scatterplot(data=data, x='SepalLength_cm', y='PetalLength_cm', hue='Class', ax=ax1[1, 0]) 
ax1[1,0].set_xlabel('Sepal Length ', fontsize='large', fontweight='bold')
ax1[1,0].set_ylabel('Petal Length ', fontsize='large', fontweight='bold')

# 4th plot
sns.scatterplot(data=data, x='SepalWidth_cm', y='PetalLength_cm', hue='Class', ax=ax1[1, 1]) 
ax1[1,1].set_xlabel('Sepal Width ', fontsize='large', fontweight='bold')
ax1[1,1].set_ylabel('Petal Length ', fontsize='large', fontweight='bold')


# 5th plot
sns.scatterplot(data=data, x='SepalLength_cm', y='PetalWidth_cm', hue='Class', ax=ax1[2, 0]) 
ax1[2,0].set_xlabel('Sepal Length ', fontsize='large', fontweight='bold')
ax1[2,0].set_ylabel('Petal Width ', fontsize='large', fontweight='bold')

# 6th plot
sns.scatterplot(data=data, x='SepalWidth_cm', y="PetalWidth_cm", hue='Class', ax=ax1[2, 1]) 
ax1[2,1].set_xlabel('Sepal Width ', fontsize='large', fontweight='bold')
ax1[2,1].set_ylabel('Petal Width ', fontsize='large', fontweight='bold')


fig.savefig('overviewScat.png')

```
This code was heavily adapted from reference 22. Although it is not quite as easy to visualise individual datapoints, it is beneficial to have a resource containing all the scatterplots together for general rapid analysis.

![overviewScat](https://i.imgur.com/tA0od24.png)

#### *Correlation Plot by Species*

From analysing the scatterplot results and examining how the setosa class was linearly divergent from the virginica and versicolor class, I thought it would be interesting to construct a correlation matrix of each species to determine if we could discern any more information from it. The code used was as follows:

```Python
setosa = data.loc[0:49] # splitting data by class (reference 24)
versicolor = data.loc[50:99]
virginica = data.loc[100:149]

sns.set(font_scale=2) # increasing font size of colour bar and x,y axes
fig, ax1 = plt.subplots(3, figsize=(25,20)) # setting up our subplot as per previous examples
# setting attributes of correlation heatmap
sns.heatmap(setosa.corr(), annot=True, cmap='YlGnBu' , cbar = True, linecolor='green', annot_kws={'size': 15}, robust = True, ax=ax1[0]) # 'annot_kws' will increase the size of the figures in the cell
ax1[0].set_title('Setosa', fontsize=30) # setting individual titles

sns.heatmap(versicolor.corr(), annot=True, cmap='YlGnBu' , cbar = True, linecolor='green', robust= True, annot_kws={'size': 15}, ax=ax1[1]) 
ax1[1].set_title('Versicolor', fontsize=30)

sns.heatmap(virginica.corr(), annot=True, cmap='YlGnBu' , cbar = True, linecolor='green', robust= True, annot_kws={'size': 15}, ax=ax1[2]) 
ax1[2].set_title('Virginica', fontsize=30)

fig.savefig('correlationSpecies.png')

```
I began by splitting the dataset based on each class (24). Once the dataset was split, I created the subplots as used previously for the scatterplots (22). I increased the font-size so that everything would be visible even when preparing three correlation heatmaps (25). I constructed the heatmaps in the same format used for the scatterplots and gave each heatmap it's own title and increased the annotation size using a GeekforGeeks example (26).

![correlationSpecies](https://i.imgur.com/5kNeapz.png)

We can see some differences in our correlations here when compared with our 'overall' correlation heatmap in an earlier section. In the 'overall' correlation plot, the main finding was the strong postive correlation between Petal length and Petal width. This finding is only maintained in the versicolor correlation heatmap. The correlation in setosa and virginica is negligible. Another finding from our 'overall' correlation plot was that there may be a slight positive correlation between Sepal length and Petal length. This finding is maintained in the versicolor and virginica correlation plots but not in the setosa. Once again, we are experiencing divergences between setosa and the other iris classes. 
Some new information also comes to light as a result of the species correlations plots. We can see a strong positive correlation between Sepal width and Sepal length in the setosa class. 

The take away points from this are:
* When examining datasets, it is best to be inquisitive. This species correlation plot was only constructed as a result of observing how the data was distributed in the scatter plots.
* The strong correlation for Petal length/width is only maintained in the versicolor class.
* The slight positive correlation Sepal length/Petal length is maintained in the versicolor and virginica classes.
* Setosa class once again diverges from the other iris classes in Sepal correlations.


#### *3D Scatter Plot of all Variables*
As a summary of the work we have carried out, I thought it would be nice to produce a 3D scatterplot of each of our variables. This, in addition to the scatterplot overview produced earlier, would give a simple summation of the most interesting result we discerned from the data: the ability to distinguish between the iris setosa class and the virginica/versicolor classes. The code to produce this scatter plot was as follows: 

```Python

fig = px.scatter_3d(data, x='SepalLength_cm', y='SepalWidth_cm', z='PetalWidth_cm',
                    color='PetalLength_cm', symbol='Class') # compiled from reference 28
fig.update_layout(legend=dict(yanchor="top", y=0.90, xanchor="left",x=0.2)) # positioning the legend so it is separate from the color bar chart (reference 29)
fig.write_image('variablesPlot3D.png', width=1800, height=900) # setting height and width variables 

```
The code was compiled by consulting the plotly website (28) and the legend was re-positioned from the same source (29). A fourth dimension was added by setting the colour to 'PetalLength_cm', thereby altering the colour of each data point on the basis of petal length.

![variablesPlot3D](https://i.imgur.com/RL3UO3z.png)

While there is no new information here, we can once again see how the setosa class is separate from the virginica/versicolor classes. The png file of the result isn't as beneficial as the proper result (where you can move the scatterplot graph) but we can still discern our overall result from it.


## 3) Conclusion

The main take-away points of each body-of-work has been discussed at the end of each section so I want to use this conclusion to discuss the project as a whole and my approach to investigating the dataset. This README serves as my thought-process throughout the course of my investigative analyses and what paths I decided to follow. I thought it prudent to construct the boxplots, for example, upon seeing evidence from the histograms that we may have outliers. I feel (hope) this was the overall aim of the project: to enable critial thinking and problem solving. The results from the scatter plots (displaying setosa's divergence from virginica/versicolor) prompted me to focus the end of the project on the species as opposed to the variables. To this end, I constructed the correlation plots focusing on the species and also the 3D scatter plot. It was fascinating to see the differences in results when comparing the correlation plots by variables and the correlation plots by species. I did not expect to see this and it proves how it can be beneficial to really dive into the data as opposed to making assumptions based solely on a high-level understanding of the data. I also decided to gain experience in using other libraries in displaying data. I installed plotly as when I was researching different libraries, I felt the range of possibilities was greater with plotly than with seaborn. I also used seaborn just to show I was not actively trying to avoid it!
I feel I have displayed the applicability of using Python to investigate a dataset and also displayed my knowledge of Python to date. 

## 4) References
    1. Yong, Cui 2020. The Iris Dataset ??? A Little Bit of History and Biology. [Online]. [17 March 2021]. Available from: https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5
    
    2. Dam, Kerstin & Hafen, Ryan & Gibson, Tara & Critchlow, Terence. (2013). Power Grid Data Analysis with R and Hadoop. 10.1016/b978-0-12-411511-8.00001-3.
   
    3. Marshall, Michael 2019. Iris Data Set. [Online]. [17 March 2021]. Available from: http://archive.ics.uci.edu/ml/datasets/Iris
    
    4. Santos, Rafael. 2019. Data Science Example - Iris dataset. [Online]. [17 March 2021]. Available from: http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html
    
    5. Dphansen (N.D.). Iris demo data set for tutorials - SQL machine learning. [online] docs.microsoft.com. Available at: https://docs.microsoft.com/en-us/sql/machine-learning/tutorials/demo-data-iris-in-sql?view=sql-server-ver15 [Accessed 17 Mar. 2021].
    
    6. Readthedocs.io. (2011). Image Module ??? Pillow (PIL Fork) 6.2.1 documentation. [online] Available at: https://pillow.readthedocs.io/en/stable/reference/Image.html.
    
    7. Stack Abuse. Writing to a File with Python???s print() Function. [online] Available at: https://stackabuse.com/writing-to-a-file-with-pythons-print-function/ [Accessed 18 Mar. 2021] 
    
    8. Avuluri, V.S.R. (2019). Exploratory Data Analysis of IRIS Data Set Using Python. [online] Medium. Available at: https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d [Accessed 20 Mar. 2021].
    
    9. kaggle.com. Simple analysis of Iris dataset. [online] Available at: https://www.kaggle.com/danalexandru/simple-analysis-of-iris-dataset [Accessed 20 Mar. 2021].
    
    10. kaggle.com. Iris Dataset ML and Deep Learning from scratch. [online] Available at: https://www.kaggle.com/kamrankausar/iris-dataset-ml-and-deep-learning-from-scratch [Accessed 20 Mar. 2021].
    
    11. datarepository.wolframcloud.com. Machine Learning | Wolfram Data Repository. [online] Available at: https://datarepository.wolframcloud.com/category/Machine-Learning [Accessed 20 Mar. 2021].
    
    12. www.nbshare.io. How to Plot a Histogram in Python. [online] Available at: https://www.nbshare.io/notebook/204214467/How-to-Plot-a-Histogram-in-Python/ [Accessed 21 Mar. 2021].
    
    13. matplotlib.org. Text properties and layout ??? Matplotlib 3.1.2 documentation. [online] Available at: https://matplotlib.org/3.1.1/tutorials/text/text_props.html.
   
    14. seaborn.pydata.org. seaborn.heatmap ??? seaborn 0.10.1 documentation. [online] Available at: https://seaborn.pydata.org/generated/seaborn.heatmap.html.
    
    15. DEV Community. Subplotting with matplotlib and seaborn. [online] Available at: https://dev.to/thalesbruno/subplotting-with-matplotlib-and-seaborn-5ei8 [Accessed 24 Mar. 2021].
    
    16. seaborn.pydata.org. seaborn.boxplot ??? seaborn 0.11.1 documentation. [online] Available at: https://seaborn.pydata.org/generated/seaborn.boxplot.html [Accessed 24 Mar. 2021].
    
    17. www.kite.com. Code Faster with Line-of-Code Completions, Cloudless Processing. [online] Available at: https://www.kite.com/python/docs/seaborn.swarmplot [Accessed 24 Mar. 2021].
    
    18. Sharma, N. (2018). Ways to Detect and Remove the Outliers. [online] Towards Data Science. Available at: https://towardsdatascience.com/ways-to-detect-and-remove-the-outliers-404d16608dba.
    
    19. plotly.com.. Plotly Express. [online] Available at: https://plotly.com/python/plotly-express/. [Accessed 27 Mar. 2021].
   
    20. plotly.com. (n.d.). Scatter Plots. [online] Available at: https://plotly.com/python/line-and-scatter/. [Accessed 27 Mar. 2021].

    21. plotly.com. Static Image Export. [online] Available at: https://plotly.com/python/static-image-export/ [Accessed 27 Mar. 2021].
    
    22. kaggle.com. How to do subplots - Iris Dataset. [online] Available at: https://www.kaggle.com/dcstang/how-to-do-subplots-iris-dataset [Accessed 27 Mar. 2021].
    
    23. Moonbooks.org. (2020). How to increase the size of axes labels on a seaborn heatmap in python ? [online] Available at: https://moonbooks.org/Articles/How-to-increase-the-size-of-axes-labels-on-a-seaborn-heatmap-in-python-/ [Accessed 27 Mar. 2021].
   
    24. www.shanelynn.ie. Python Pandas iloc, loc, and ix for DataFrame selection. [online] Available at: https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/ [Accessed 30 Mar. 2021].
    
    25. Like Geeks. (2019). Seaborn heatmap tutorial (Python Data Visualization) - Like Geeks. [online] Available at: https://likegeeks.com/seaborn-heatmap-tutorial/. [Accessed 30 Mar. 2021].
    
    26. GeeksforGeeks. (2020). How to increase the size of the annotations of a seaborn heatmap in Python? [online] Available at: https://www.geeksforgeeks.org/how-to-increase-the-size-of-the-annotations-of-a-seaborn-heatmap-in-python/ [Accessed 30 Mar. 2021].
    
    27. jonathansoma.com. Creating Waffle Charts in pandas. [online] Available at: http://jonathansoma.com/lede/foundations-2018/matplotlib/creating-waffle-charts-in-pandas/ [Accessed 2 Apr. 2021].
    
    28. plotly.com. 3D Scatter Plots. [online] Available at: https://plotly.com/python/3d-scatter-plots/ [Accessed 2 Apr. 2021].
    
    29. plotly.com. Legends. [online] Available at: https://plotly.com/python/legend/#legend-positioning [Accessed 2 Apr. 2021].










    

















 


 



 




 

 

???



