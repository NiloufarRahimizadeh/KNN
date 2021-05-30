# import itertools
# from os import X_OK
import numpy as np 
# import matplotlib.pyplot as plt 
# import matplotlib.ticker as ticker
import pandas as pd 
from sklearn import preprocessing

df = pd.read_csv('teleCust1000t.csv')
columns = [ 'tenure','age', 'marital', 'address', 'income', 'ed', 'employ','retire', 'gender', 'reside']
X = df[columns].values

X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))
