import numpy as np
import pandas as pd

#Load the data
df = pd.read_csv("Zomato-data-.csv")
 
pd.set_option('display.max_columns', None)

pd.set_option('display.width', None)

print(df.head())

print(df.shape)

print(df.columns)

#Cleaning the dataset.
print(df.isnull().head().sum())

print(df.info())

print(df.describe())

df1 = df.drop(columns=['book_table','listed_in(type)'])

print(df1.head())
print("\n")

print("Duplicated:",df1.duplicated().sum())

print(df1.drop_duplicates(inplace=True))

print("Duplicated:",df1.duplicated().sum())

# Data Transformation / Preprocessing

print("Data type of rate:",df1['rate'].dtype)

parts = df1['rate'].str.split('/')
df1['rate'] = parts.str[0].astype(float)

print("Updated Data type of rate:",df1['rate'].dtype)

print(df1.head())
df1.info()

def conversion(value):
    if(value == 'Yes'):
        value = 1
    else:
        value = 0
    return value

df1['online_order'] = df1['online_order'].apply(conversion)

print(df1.head())
df1.info()
