# Final program that outputs a summary of each variable to a single text file, saves a histogram of each variable to png files, 
# and outputs a scatter plot of each pair of variables.
# GMIT Programming and Scripting Project2021 (analysis of Iris Fisher Datset)

# Author: Conor McCaffrey

# Importing required libraries
import numpy as np
import pandas as pd
import sys
import matplotlib as mpl
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from pywaffle import Waffle


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

# Waffle Chart of Species Types
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

# Histograms of each variable

sns.displot(data['SepalLength_cm'], kde= False, bins = 15, color = 'green', edgecolor = 'orange', alpha=0.6) # setting kde as False in order to remove the density line as it is not relavant to task
# also altered alpha value to change transparency of the graph (adapted from Reference 13)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.suptitle('Sepal Length', fontsize = 12) # adding main title to histogram and setting fontsize
plt.ylim(0,25) # setting y-axis limits
plt.xlim(3,10) # setting x-axis limits
plt.grid(ls = '--', lw = '0.1', color = '#BEBEBE', axis = 'y') # modifying grid lines so that they dont 'overpower' the data and used hex value for colour
plt.savefig('sepalLengthHist.png') # saving output to specified .png file

sns.displot(data['SepalWidth_cm'], kde= False, bins = 15, color = 'yellow', edgecolor = 'orange', alpha=0.6)
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')
plt.suptitle('Sepal Width', fontsize = 12) 
plt.ylim(0,50) 
plt.xlim(0,6) 
plt.grid(ls = '--', lw = '0.1', color = '#BEBEBE', axis = 'y') 
plt.savefig('sepalWidthHist.png') 

sns.displot(data['PetalLength_cm'], kde= False, bins = 15, color = 'blue', edgecolor = 'orange', alpha=0.6)
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.suptitle('Petal Length', fontsize = 12) 
plt.ylim(0,50) 
plt.xlim(0,10) 
plt.grid(ls = '--', lw = '0.1', color = '#BEBEBE', axis = 'y') 
plt.savefig('petalLengthHist.png') 

sns.displot(data['PetalWidth_cm'], kde= False, bins = 15, color = 'purple', edgecolor = 'orange', alpha=0.6)
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')
plt.suptitle('Petal Width', fontsize = 12) 
plt.ylim(0,40) 
plt.xlim(0,4) 
plt.grid(ls = '--', lw = '0.1', color = '#BEBEBE', axis = 'y') 
plt.savefig('petalWidthHist.png') 

# Histograms of each variable together for rapid visual assessment

data.hist(figsize = (9,6))
plt.savefig('overviewHist.png')


# Product a heatmap of correlations between variables
# information generated from reference 14
correlationVariablePlot = plt.subplots(figsize=(8,8)) # setting size of output
# setting attributes of correlation heatmap
correlationVariablePlot =sns.heatmap(data.corr(), annot=True, cmap='YlOrRd' ,square=True, cbar = True, linecolor='green', robust= True) 
plt.savefig("correlationPlot.png") # save output to 'correlationPlot.png'


# Testing for Outliers using BoxPlots
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

# Program to outplut scatter plots of each pair of variables

# using newly imported Plotly library. Setting properties of scatterplot and saving outputs to separate .png files.

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


# Scatterplot of each variable together for rapid visual assessment
# create a figure 'fig' with axis 'ax1' with 3x2 configuration # reference 22
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

# Program to output correlation plot on species. Follow-on analyses from results of distribution of species data in histograms/scatter plots
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


# 3D Scatter Plots

fig = px.scatter_3d(data, x='SepalLength_cm', y='SepalWidth_cm', z='PetalWidth_cm',
                    color='PetalLength_cm', symbol='Class') # compiled from reference 28
fig.update_layout(legend=dict(yanchor="top", y=0.90, xanchor="left",x=0.2)) # positioning the legend so it is separate from the color bar chart (reference 29)
fig.write_image('variablesPlot3D.png', width=1800, height=900) # setting height and width variables 
