# 3D Scatter Plots

import plotly.express as px
from uploadDataSet import data


fig = px.scatter_3d(data, x='SepalLength_cm', y='SepalWidth_cm', z='PetalWidth_cm',
                    color='PetalLength_cm', symbol='Class')
fig.update_layout(legend=dict(yanchor="top", y=0.90, xanchor="left",x=0.2))
fig.write_image('3DvariablesPlot.png', width=1800, height=900)
