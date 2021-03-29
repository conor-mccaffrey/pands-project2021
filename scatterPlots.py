# Program to outplut scatter plots of each pair of variables

import numpy as np
import pandas as pd
import sys
import matplotlib as mpl
import os
import matplotlib.pyplot as plt
from PIL import Image # this lets us convert images into arrays
import matplotlib.patches as mpatches # needed for waffle charts
import seaborn as sns
import plotly.express as px


from uploadDataSet import data # importing data

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
