import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from glob import glob

# Reading all CSV file(s)
os.chdir("data/top10")
stocks = glob("*.csv")
arr = np.zeros((len(stocks)))
print(stocks) # The sequence of file reading


os.chdir("data/output")
stocks = glob("*.csv")
arr = np.zeros((len(stocks)))
print(stocks) # The sequence of file reading

K = int(input("Enter lag number: "))
R = int(input("Enter R number: "))

m = 0

for i in range(len(stocks)):
    for j in range(i+1,len(stocks)-1):
        data1 = pd.read_csv(stocks[i])
        data2 = pd.read_csv(stocks[j])
        data1 = data1["Adjusted Close"]
        data2 = data2["Adjusted Close"]
        data1 = data1[:K]
        data2 = data2[:K]
        data1 = data1.squeeze()
        data2= data2.squeeze()
        r = data1.corr(data2,method='pearson')
        l=[]
        if r > R or r < -R :
            m = m + 1
            l.append(stocks[i])
            l.append(stock)
            with open (final_output+".csv",'a') as f_object:
                writer_object = writer(f_object)
  
                # Pass the list as an argument into
                # the writerow()
                writer_object.writerow(List)

                #Close the file object
                f_object.close()
        
        
output1 = pd.DataFrame()
for i in range(len(stocks)-1):
    
#     df = pd.read_csv(i, parse_dates=['Date'], index_col='Date')
    # index 0 = Date and index 5 = Close |  Date and Close Price Columns
    
    if i == 0:
        data1 = pd.read_csv(stocks[i])
    else:
        data1 = output1
    
    data2 = pd.read_csv(stocks[i+1])
  
    # using merge function by setting how='inner'
    output1 = pd.merge(data1, data2, 
                   on='Date', 
                   how='inner')
    

df = pd.DataFrame(output1["Date"])
start_date = '18.05.2012'
end_date = '14.02.2022'
for i in range(len(stocks)):
    data  = pd.read_csv(stocks[i])
    final_output = pd.merge(data,df,on="Date",how="inner")
    st = 'Output_'+stocks[i]
    final_output.to_csv(st,index=False)
    
    print(final_output)

    

