import pandas as pd
csvdata= pd.read_csv("fundscale-1.csv", delimiter=";", encoding='utf-8')

print(csvdata.shape) # (n,m) n= row, m=column
print(csvdata.index) 
print(csvdata.info())
print(csvdata.describe()) # statistical data
print(csvdata.dropna()) # remove null, N/A value
print(csvdata.head(5)) # fetch the first n files, head(n)
print(csvdata.columns) # column names
a=csvdata['組合型基金'][1:6]
b=csvdata['組合型基金'].between(100000000000,120000000000) # show boolean value of the data 
print(csvdata.ETF[b]) #csvdata."column_name"[b], print the column which satisfy b

c=(csvdata[(csvdata['組合型基金'] > 110000000000) & (csvdata['ETF'] > 100000000000)])
print(csvdata.iloc[1:3]) # fetch data from count from 1 to 3, start w/ 0.
print(csvdata.iloc[2,3]) # [row, column] start from [0,0]
print(c.sort_values(by=['組合型基金'], ascending=False))
print(c['ETF'].mean()) # average
print(c['ETF'].sum()) 
