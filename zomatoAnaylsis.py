import numpy as np
import pandas as pd

#Load the data
print("------- Load the data. -------")
df = pd.read_csv("Zomato-data-.csv")
 
pd.set_option('display.max_columns', None)

pd.set_option('display.width', None)

print(df.head())

print(df.shape)

print(df.columns)

#Cleaning the dataset.
print("\n------ Cleaning the dataset. -------")
print(df.isnull().sum())

print(df.info())

print(df.describe())

df1 = df.drop(columns=['book_table','listed_in(type)'])
print(df1.shape)

print(df1.head())
print("\n")

print("Duplicated:",df1.duplicated().sum())

print(df1.drop_duplicates(inplace=True))

print("Duplicated:",df1.duplicated().sum())

# Data Transformation / Preprocessing
print("------- Data Transformation / Preprocessing. -------")

print("Data type of rate:",df1['rate'].dtype)

# Check entries that do NOT contain '/'
invalid_format = df1[~df1['rate'].str.contains('/', na=False)]

print("Number of non-formatted entries:", len(invalid_format))

print(invalid_format['rate'].value_counts())

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

#EDA(Exploratory Data Analysis)
print("\n------ EDA(Exploratory Data Analysis) -------")
#(Q.1)Do more restaurants provide online delivery compared to offline services?
print("\n(Q.1)Do more restaurants provide online delivery compared to offline services?")

print(df1.head(10))

# countYes = df1['online_order'].sum()
# countNo = len(df1) - countYes

countYes = np.sum(df1["online_order"] == 1)
countNo = np.sum(df1["online_order"] == 0)

#Both methods are valid

if countYes > countNo:
    print("The number of restaurants using the online services is:",countYes)
    print("The number of restaurants not using the online services is:",countNo)
    print("Online services win.")
else:
    print("The number of restaurants using the online services is:",countYes)
    print("The number of restaurants not using the online services is:",countNo)
    print("Ofline servces win.")
    
print("Conclusion:")
print("This results suggests that most of the restaurnts does not accept the online orders.\n")

#(Q.2)What price range do couples prefer for dining out?
print("\n(Q.2)What price range do couples prefer for dining out?")
print(df1.head(5))

counts = df1['approx_cost(for two people)'].value_counts()

high_count = counts.max()
highest_value = counts.idxmax()

print("Most Frequent Value :", highest_value)
print("The count of most Frequent value :",high_count)
print("Which is highest among the other prices count")

print("Concluson:")
print("The majority of couples prefer restaurants with an approximate cost of 300 rupees.\n")


#(Q.3)Which types of restaurants are most favored by the general public?

print("(Q.3)Which types of restaurants are most favored by the general public?")

df1['listed_in(type)'] = df['listed_in(type)']
print(df1.head())

preferedoption = df1['listed_in(type)'].value_counts()
print(preferedoption)

prefered_count = counts.max()
Type = preferedoption.idxmax()

print("Most like option:",Type)

print("Conclusion:")
print("Dining restaurants are preferred by a larger number of individuals.\n")

#(Q.4)Identify the Most Voted Restaurant
print("(Q.4)Identify the Most Voted Restaurant")
print(df1.head())

print("\n")

max_votes = df1['votes'].max()
restaurnts_max_voted  = df1.loc[df1['votes'] == max_votes,'name']

print(restaurnts_max_voted)

print("Conclusion:")
print("The Empire Restaurant has the highest voted retaurants\n")

#(Q.5)Ratings Comparison - Online vs Offline Orders

print("(Q.5)Ratings Comparison - Online vs Offline Orders")

print(df1.head())

prefer = df1.groupby('online_order')['rate'].mean()
print(prefer)

max_rate = prefer.max()
online_or_ofline = prefer.idxmax()

print("online vs ofline:",online_or_ofline)

print("conclusion:")
print("Conclusion: Offline orders received lower ratings in comparison to online orders which obtained excellent ratings.\n")

