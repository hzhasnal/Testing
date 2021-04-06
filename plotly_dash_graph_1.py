import plotly.graph_objects as go
import pandas as pd

# Read the data 
df = pd.read_csv('parliamentary-constituency-profiles-data.csv', usecols=[ "Parliamentary Constituency", 'Persons-2008'])

#cleaning data
df = df.dropna()
df = df.reset_index(drop=True)
#Removing the total
df = df[:-2]

fig = go.Figure(data=go.Scatter(x=df["Parliamentary Constituency"],
                                y=df['Persons-2008'],
                                mode='markers',
                                marker_color=df['Persons-2008'],
                                )) # hover text goes here

fig.update_layout(title='Population in Greater London')
fig.show()