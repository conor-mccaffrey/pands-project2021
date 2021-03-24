# Histograms of each variable together for rapid visual assessment

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from uploadDataSet import data 

data.hist(figsize = (9,6))
plt.savefig('overviewHist.png')
