import csv
import numpy as np

# Reading CSV file(s)
with open('data/AAPL.csv', 'r') as AAPL:
    appleData = list(csv.reader(AAPL, delimiter=';'))
 
npAppleData = np.array(appleData)
print(npAppleData)

# ALGORITHM 1: Anomaly price and volume finding algorithm.
# Input : M(i,:), Ms(i,:), prices
# Output : Anomaly price, Anomaly volume


# ALGORITHM 2: Anomaly location finding algorithm.
# Input : Anomaly price, Anomaly volume, T
# Output : Anomaly position
