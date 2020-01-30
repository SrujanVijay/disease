import numpy as np
from sklearn import preprocessing, train_test_split, neighbors
import pandas as pd

df=pd.read_csv('Training.csv')
print(df.head())