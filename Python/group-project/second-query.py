import pandas as pd


df = pd.read_csv("movies_table.csv", usecols = ['id','title'])
print(df)