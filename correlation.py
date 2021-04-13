# Product a heatmap of correlations between variables

from uploadDataSet import data # Not needed for final program
import seaborn as sns
import matplotlib.pyplot as plt

# information generated from reference 14
correlationVariablePlot = plt.subplots(figsize=(8,8)) # setting size of output
# setting attributes of correlation heatmap
correlationVariablePlot =sns.heatmap(data.corr(), annot=True, cmap='YlOrRd' ,square=True, cbar = True, linecolor='green', robust= True) 
plt.savefig("correlationPlot.png") # save output to 'correlationPlot.png'