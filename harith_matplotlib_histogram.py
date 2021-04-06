import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from sklearn import preprocessing
import numpy as np
import os

# Import Data
DATA_DIR = 'data'
data = os.path.join(DATA_DIR,'parliamentary-constituency-profiles-data.csv')
df = pd.read_csv(data, usecols=[ "Parliamentary Constituency", 'Persons-2008',"aged 0-14-2008","aged 15-34-2008","aged 35-54-2008","aged 55-74-2008","aged 75+-2008"])

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


#defining each category
x = df['Parliamentary Constituency']
age7 = df["aged 0-14-2008"]
age15 = df["aged 15-34-2008"]
age35 = df["aged 35-54-2008"]
age55 = df["aged 55-74-2008"]
age75 = df["aged 75+-2008"]

#defining the top of the each category
age7_15 = df["aged 0-14-2008"]+df["aged 15-34-2008"]
age7_35 = df["aged 0-14-2008"]+df["aged 15-34-2008"]+df["aged 35-54-2008"]
age7_55 = df["aged 0-14-2008"]+df["aged 15-34-2008"]+df["aged 35-54-2008"]+df["aged 55-74-2008"]
age7_75 = df["aged 0-14-2008"]+df["aged 15-34-2008"]+df["aged 35-54-2008"]+df["aged 55-74-2008"]+df["aged 75+-2008"]


#plotting the bar plot
plt.bar(x,age7 ,0.4,label="aged 0-14")
plt.bar(x,age15,0.4,bottom = age7, label="aged 15-34")
plt.bar(x,age35,0.4,bottom = age7_15, label="aged 35-54")
plt.bar(x,age55,0.4,bottom = age7_35, label="aged 55-74")
plt.bar(x,age75,0.4,bottom = age7_55 , label="aged 75+")

#detailing the plot
plt.xlabel('Areas in London')
plt.ylabel('Population distribution, %')
plt.title('Population distribution in top '+str(n)+' areas in London')
plt.legend()

# Show the major grid lines with dark grey lines
plt.grid(b=True, which='major', color='#666666', linestyle='-')

# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.show()