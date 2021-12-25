import csv
import pandas as pd

df= pd.read_csv('final_stars.csv')


del df['Unnamed: 0']
del df['Unnamed: 6']
del df['Unnamed: 0.1']
del df['Star_name.1']
del df['Distance.1']
del df['Mass.1']
del df['Radius.1']
del df['Luminosity']

df= df[df['Distance'].notna()]
df= df[df['Mass'].notna()]
df= df[df['Radius'].notna()]
df= df[df['Star_name'].notna()]

print(df.columns)
print(df.head())

df.to_csv('main_stars.csv')