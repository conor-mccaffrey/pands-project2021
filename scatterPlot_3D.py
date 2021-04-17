# 3D Scatter Plots

import plotly.express as px  # new library
from uploadDataSet import data # won't be required for main program


fig = px.scatter_3d(data, x='SepalLength_cm', y='SepalWidth_cm', z='PetalWidth_cm',
                    color='PetalLength_cm', symbol='Class') # compiled from reference 28
fig.update_layout(legend=dict(yanchor="top", y=0.90, xanchor="left",x=0.2)) # positioning the legend so it is separate from the color bar chart (reference 29)
fig.write_image('variablesPlot3D.png', width=1800, height=900) # setting height and width variables 
