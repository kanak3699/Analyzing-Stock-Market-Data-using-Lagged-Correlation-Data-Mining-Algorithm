import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Reading CSV file(s)

df = pd.read_csv(r'data/sp500/csv/AAPL.csv')
T = df.to_numpy()
print(T)



# ALGORITHM 1: Anomaly price and volume finding algorithm.
# Input : M(i,:), Ms(i,:), prices
# Output : Anomaly price, Anomaly volume



# ALGORITHM 2: Anomaly location finding algorithm.
# Input : Anomaly price, Anomaly volume, T
# Output : Anomaly position
