# Testing for Outliers using BoxPlots
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import seaborn as sns


from uploadDataSet import data

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
fig.suptitle('Boxplots of Iris Fisher Data Variables', style = 'italic',)

sns.boxplot(ax=axes[0 ,0], data=data['SepalLength_cm'], x=data['Class'], y=data['SepalLength_cm'], showfliers=False)  # setting axes, boxplot position
sns.swarmplot(ax=axes[0 ,0], data=data['SepalLength_cm'], x=data['Class'], y=data['SepalLength_cm'], color = '#554444', s=4) # constructing swarmplot as per reference 16
sns.boxplot(ax=axes[0 ,1], data=data['SepalWidth_cm'], x=data['Class'], y=data['SepalWidth_cm'], showfliers=False) # setting axes, boxplot position
sns.swarmplot(ax=axes[0 ,1], data=data['SepalWidth_cm'], x=data['Class'], y=data['SepalWidth_cm'], color = '#0D0D0D', s=4)
sns.boxplot(ax=axes[1 ,0], data=data['PetalLength_cm'], x=data['Class'], y=data['PetalLength_cm'], showfliers=False) # setting axes, boxplot position
sns.swarmplot(ax=axes[1 ,0], data=data['PetalLength_cm'], x=data['Class'], y=data['PetalLength_cm'], color = '#943126', s=4)
sns.boxplot(ax=axes[1 ,1], data=data['PetalWidth_cm'], x=data['Class'], y=data['PetalWidth_cm'], showfliers=False) # setting axes, boxplot position
sns.swarmplot(ax=axes[1 ,1], data=data['PetalWidth_cm'], x=data['Class'], y=data['PetalWidth_cm'], color = '#0E6655', s=4)
plt.show()