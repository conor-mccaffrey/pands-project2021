# Scatterplot of each variable together for rapid visual assessment

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from uploadDataSet import data # importing dataset
data.columns = ['SepalLength_cm','SepalWidth_cm','PetalLength_cm','PetalWidth_cm','Class'] # adding column names to files

# create a figure 'fig' with axis 'ax1' with 3x2 configuration # reference 22
fig, ax1 = plt.subplots(3,2, figsize=(25,20)) # adapted from kaggle.com (reference 22)
fig.suptitle('Scatterplots of Iris Fisher Data Variables', style = 'italic', size = 25) # Overall title and editing font for appearance

sns.set(font_scale=1.2) # increasing size of legend (reference 23)

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

