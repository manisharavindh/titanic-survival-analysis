import numpy as np
import pandas as pd

df = pd.read_csv("data/train.csv")

print(df.shape)
print('----- ----- ----- ----- ----- -----')
print(df.info())
print('----- ----- ----- ----- ----- -----')
print(df.head())
print('----- ----- ----- ----- ----- -----')
print(df.isnull().sum())
print('----- ----- ----- ----- ----- -----')
print(df.describe())