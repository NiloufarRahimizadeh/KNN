import itertools
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.ticker as ticker
import pandas as pd 
from sklearn import preprocessing

df = pd.read_csv('teleCust1000t.csv')
df = df['custcat'].value_counts()
print(df.head())
df.hist(bins=15)
plt.show()