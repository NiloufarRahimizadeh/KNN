import itertools
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.ticker import NullFormatter
import matplotlib.ticker as ticker
import pandas as pd 
from sklearn import preprocessing

df = pd.read_csv('teleCust1000t.csv')
df.head()
# df['custcat'].value_counts()
df.hist(column='income')
