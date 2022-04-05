import pandas as pd
import os
from glob import glob
import csv

# Data Cleaning
def cleanData():


    os.chdir("data/top10")
    stocks = glob("*.csv")
    for i in range(len(stocks) - 1):

        if i == 0:
            file1_Data = pd.read_csv(stocks[i])
        else:
            file1_Data = output

        file2_Data = pd.read_csv(stocks[i + 1])

        # using merge function by setting how='inner'
        output = pd.merge(file1_Data, file2_Data, on='Date', how='inner')

    df = pd.DataFrame(output["Date"])

    for i in range(len(stocks)):
        os.chdir("../top10")
        file_data = pd.read_csv(stocks[i])
        final_output = pd.merge(file_data, df, on="Date", how="inner")
        os.chdir("../cleanData")
        st = 'Output_' + stocks[i]
        final_output.to_csv(st, index=False)

    print("Data has been cleaned and stored in the cleanData directory")


def corelation():
    # User Input
    print("Finding correlation between the stocks")

    K = int(input("Enter lag number: "))
    R = float(input("Enter R number: "))

    # Algorithm
    m = 0
    header = ['Company A', 'Company B', 'Co-relation','Trend']

    os.chdir("../output")
    f = open('final_output.csv', 'w+')

    os.chdir("../cleanData")
    stocks = glob("*.csv")
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
                r = data1.corr(data2, method='pearson')
                temp = temp + k
                if r > R or r < -R:
                    row = []
                    m = m + 1
                    # splitChar = split('.')[0].split('_')[1]
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
    f.close()


if __name__ == '__main__':
    cleanData()
    corelation()
    print("The result is printed as file_output.csv in the output folder.")