import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates


xpoints = np.array(range(1,100))
ypoints = xpoints + xpoints 
plt.scatter(xpoints, ypoints, label = 'Random')
plt.show()