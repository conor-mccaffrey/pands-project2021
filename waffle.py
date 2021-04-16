# Waffle Chart of Species Types
# importing all necessary libraries

import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle
  
# creation of a dataframe
from uploadDataSet import data # importing dataset

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