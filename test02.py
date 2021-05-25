import itertools
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker
import pandas as pd 
from sklearn import preprocessing

df = pd.read_csv('teleCust1000t.csv')
df.head()
# print(df)




X = df[[ 'tenure','age', 'marital', 'address', 'income', 'ed', 'employ','retire', 'gender', 'reside']] .values  #.astype(float)
# print(X[0:5])
y = df['custcat'].values

print(y[0:5])

X = preprocessing.StandardScaler().fit(X).transform(int(X).astype(float))
print(X[0:5])