import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from sklearn import preprocessing
import numpy as np

# Import Data
df = pd.read_csv('parliamentary-constituency-profiles-data.csv', usecols=[ "Parliamentary Constituency", 'Persons-2008',"Males-2008","Females-2008"])

#cleaning data
df = df.dropna()
df = df.reset_index(drop=True)
#Removing the total
df = df[:-2]
df = df.sort_values(by='Persons-2008', ascending=False)

#defining max counties
n = 6
length = len(df)
df = df[:-(length - n)]
print(df)

#normalize
al_df = df.drop(["Parliamentary Constituency"], axis=1)
d = preprocessing.normalize(al_df, axis=0)
names = al_df .columns
scaled_df = pd.DataFrame(d, columns=names)
print(scaled_df)



x = df['Parliamentary Constituency']
male = al_df["Males-2008"]
female = al_df["Females-2008"]

plt.bar(x,male,0.4,label='male')
plt.bar(x,df["Females-2008"],0.4,bottom = male, label='female')

plt.xlabel('Counties')
plt.ylabel('Population distribution')
plt.title('Population distribution in top '+str(n)+' areas in London')
plt.legend()
plt.show()


