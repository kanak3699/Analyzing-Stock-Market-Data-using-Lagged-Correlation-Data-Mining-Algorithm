import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from glob import glob

# Reading all CSV file(s)
os.chdir("data/top10")
strain = glob("*.csv")
arr = np.zeros((len(strain)))
print(strain) # The sequence of file reading


for filename in strain:
    df = pd.read_csv(filename, parse_dates=['Date'], index_col='Date')
    print(df)
