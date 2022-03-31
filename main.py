import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from glob import glob
import csv


clean_data_location = "/Users/kanakprajapati/Downloads/CSCI 4144 - Data Warehousing/Data-Mining-to-analyze-stock-market-data-using-Lagged-Correlation/data/cleanData/"
output_location = "/Users/kanakprajapati/Downloads/CSCI 4144 - Data Warehousing/Data-Mining-to-analyze-stock-market-data-using-Lagged-Correlation/data/output/"
# arr = np.zeros((len(stocks)))
# print(stocks) # The sequence of file reading

# Data Cleaning
def cleanData():

    os.chdir("data/top10")
    stocks = glob("*.csv")
    for i in range(len(stocks) - 1):
        #     df = pd.read_csv(i, parse_dates=['Date'], index_col='Date')
        # index 0 = Date and index 5 = Close |  Date and Close Price Columns
        if i == 0:
            data1 = pd.read_csv(stocks[i])
        else:
            data1 = output1

        data2 = pd.read_csv(stocks[i + 1])

        # using merge function by setting how='inner'
        output1 = pd.merge(data1, data2,
                           on='Date',
                           how='inner')

    df = pd.DataFrame(output1["Date"])

    for i in range(len(stocks)):
        data = pd.read_csv(stocks[i])
        final_output = pd.merge(data, df, on="Date", how="inner")

        st =  clean_data_location + 'Output_' + stocks[i]

        final_output.to_csv(st, index=False)



def corelation():
    # User Input

    K = int(input("Enter lag number: "))
    R = float(input("Enter R number: "))

    # Algorithm
    m = 0
    header = ['Company A', 'Company B', 'Co-relation']

    output_file = output_location + 'final_output.csv'
    f = open(output_file, 'w+')

    os.chdir("../cleanData")
    stocks = glob("*.csv")
    for i in range(len(stocks)):
        for j in range(i + 1, len(stocks) - 1):
            data1 = pd.read_csv(stocks[i])
            data2 = pd.read_csv(stocks[j])
            data1 = data1["Adjusted Close"]
            data2 = data2["Adjusted Close"]
            data1 = data1[:K]
            data2 = data2[:K]
            data1 = data1.squeeze()
            data2 = data2.squeeze()
            r = data1.corr(data2, method='pearson')
            l = []
            if r > R or r < -R:
                m = m + 1
                #splitChar = split('.')[0].split('_')[1]
                l.append(stocks[i])
                l.append(stocks[j])
                l.append(r)
                writer = csv.writer(f)
                if f.tell() == 0:
                    writer.writerow(header)

                writer.writerow(l)
    f.close()


if __name__ == '__main__':
    cleanData()
    corelation()