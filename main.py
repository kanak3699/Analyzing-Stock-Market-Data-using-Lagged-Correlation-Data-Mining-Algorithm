'''
This is the main (only) class for the program. This program analyzes stock market data using lagged correlation algorithm.
The program implements the lagged correlation algorithm as per the research paper. (https://ieeexplore.ieee.org/abstract/document/4783968)
'''

# Importing necessary dependencies.

# Reference for Pandas Documentation - https://pandas.pydata.org/
import pandas as pd
import os
from glob import glob
import csv

'''
This method gets the dataset to perform correlation. The cleaned dataset is stored in the cleanData directory. 

NOTE FOR DATASET TESTING:
    Testing the big data (Forbes 2000, Nasdaq, and NYSE) will take hours to compute as it checks for all the possible correlations between those stocks.
    So, I have created a manual dataset of Top 10 stocks for a quick test, which finds correlation between the top 10 stocks.
    If you want to test any big datasets just uncomment the line below "To test data for " and comment the line below top 10 stocks.
'''
def cleanData():

    # To test data for forbes 2000 stocks
    # os.chdir("data/forbes2000")

    # To test data for nasdaq stocks
    # os.chdir("data/nasdaq")

    # To test data for nyse stocks
    # os.chdir("data/nyse")

    # To test data for top 10 stocks
    os.chdir("data/top10")

    # Getting all the csv files
    stocks = glob("*.csv")

    for i in range(len(stocks) - 1):
        
        if i == 0:
            file1_Data = pd.read_csv(stocks[i])
        else:
            file1_Data = output

        file2_Data = pd.read_csv(stocks[i + 1])

        # Using the merge function by setting how='inner' to get the inner data from csv files.
        output = pd.merge(file1_Data, file2_Data, on='Date', how='inner')
        
    df = pd.DataFrame(output["Date"])

    for i in range(len(stocks)):
        # For forbes 2000 directory
        # os.chdir("../forbes2000")

        # For nasdaq directory
        # os.chdir("../nasdaq")

        # For nyse directory
        # os.chdir("../nyse")

        # For top 10 directory
        os.chdir("../top10")
        
        file_data = pd.read_csv(stocks[i])
        final_output = pd.merge(file_data, df, on="Date", how="inner")
        os.chdir("../cleanData")
        st = 'Output_' + stocks[i]
        final_output.to_csv(st, index=False)
        print("Data has been cleaned for: ", stocks[i])

    print("\n Data has been cleaned and stored in data/cleanData directory")

'''
This method performs correlation between the stocks. It asks user to enter the K (Lag) and R (Correlation). 
The algorithm to perform correlation is adapted from the following paper:
URL:    https://ieeexplore.ieee.org/abstract/document/4783968
DOI:    10.1109/ICIAFS.2008.4783968

REFERENCE: 
C. Fonseka and L. Liyanage, "A Data mining algorithm to analyse stock market data using lagged correlation," 2008 4th International Conference on Information and Automation for Sustainability, 2008, pp. 163-166, doi: 10.1109/ICIAFS.2008.4783968.    

'''

def corelation():
    # Getting User Input.
    K = int(input("Enter lag number: "))
    R = float(input("Enter R number: "))

    m = 0
    # Header for out file (csv).
    header = ['Company A', 'Company B', 'Co-relation','Trend']  

    # Writing the output file.
    os.chdir("../output")
    f = open('final_output.csv', 'w+')

    # Writing the files in cleanData directory.
    os.chdir("../cleanData")
    stocks = glob("*.csv")

    # Looping through the stocks and comparing the csv files data.
    for i in range(len(stocks)):
        for j in range(i + 1, len(stocks) - 1):
            data1 = pd.read_csv(stocks[i])
            data2 = pd.read_csv(stocks[j])
            data1 = data1["Adjusted Close"]
            data2 = data2["Adjusted Close"]
            temp = 0
            k=K
            length = len(data1)
            while temp!=length:
                if length-temp<K:
                    k= length-temp

                data1 = data1[temp:temp+k]
                data2 = data2[temp:temp+k]
                data1 = data1.squeeze()
                data2 = data2.squeeze()

                # REFERENCE : https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html
                r = data1.corr(data2, method='pearson')
                temp = temp + k
                if r > R or r < -R:
                    row = []
                    m = m + 1
                    row.append(stocks[i].split('.')[0].split('_')[1])
                    row.append(stocks[j].split('.')[0].split('_')[1])
                    row.append(r)
                    if r > 0 :
                        status = "UP"
                    elif r < 0:
                        status = "DOWN"
                    else:
                        status = "NEUTRAL"
                    row.append(status)
                    writer = csv.writer(f)
                    if f.tell() == 0:
                        writer.writerow(header)

                    writer.writerow(row)
                    print("Finding correlation between", stocks[i], " ",stocks[j], "has been completed" )
    f.close()


if __name__ == '__main__':
    # Calling the cleanData function to clean the data.
    cleanData()
    # Calling the correlation function to perform correlation using the lagged correlation algorithm.
    corelation()
    print("\n \nThe result is printed as file_output.csv in the data/output directory.")