import numpy as np
import pandas as pd

df = pd.read_csv("data/train.csv")

print(df.shape)
print(df.info())
print(df.head())

df.isnull().sum()
df.duplicated().sum()
df.describe()

df.loc[df['Age'].argmin()]