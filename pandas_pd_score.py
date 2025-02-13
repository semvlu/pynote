import pandas as pd
csvdata= pd.read_csv('score.csv')
num = int(len(csvdata))
i=0
for i in range(num):
    csvdata['Region'] = csvdata['County'].apply(lambda x: x[:3]) # create new column "Region" which is from the first n characters of "County"
print(csvdata)