import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash(__name__)

# Read the data 
df = pd.read_csv('parliamentary-constituency-profiles-data.csv', usecols=[ "Parliamentary Constituency", 'Persons-2008'])

#cleaning data
df = df.dropna()
df = df.reset_index(drop=True)
#Removing the total
df = df[:-2]

# Create the figure
fig = go.Figure(data=go.Scatter(x=df["Parliamentary Constituency"],
                                y=df['Persons-2008'],
                                mode='markers',
                                marker_color=df['Persons-2008'],
                                )) 

fig.update_layout(title='Population in Greater London')

app.layout = html.Div(children=[
    html.H1(children='Visualization of Population in Greater London'),

    html.Div(children='''
        A scatter plot of population in Greater London
    '''),

    dcc.Graph(
        id='example-graph',
        figure= fig,
        style={'width': '200vh', 'height': '90vh'}
        
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)