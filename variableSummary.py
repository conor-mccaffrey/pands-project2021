# Output a txt file that summarises each variable through various attributes
import os
import sys
import pandas as pd

from uploadDataSet import data  # found this idea on kite.com (importing the output of one Python file into another Python file)

with open('variablesSummary.txt', 'w') as text_file:
    print(data.head(5))
