import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os

app = dash.Dash(__name__)

# Read the data 
DATA_DIR = 'data'
data = os.path.join(DATA_DIR,'parliamentary-constituency-profiles-data.csv')
df = pd.read_csv(data, usecols=[ "Parliamentary Constituency", 'Persons-2008'])

#cleaning data
df = df.dropna()
df = df.reset_index(drop=True)
df = df[:-2] #Removing the total
df_up = df.sort_values(by='Persons-2008', ascending=False) # sort in ascending order

#html
fig_names = ['fig1', 'fig2']
fig_dropdown = html.Div([
    dcc.Dropdown(
        id='fig_dropdown',
        options=[{'label': x, 'value': x} for x in fig_names],
        value=None
    )])
fig_plot = html.Div(id='fig_plot')
app.layout = html.Div([fig_dropdown, fig_plot])
    
#dropdown menu
@app.callback(
dash.dependencies.Output('fig_plot', 'children'),
[dash.dependencies.Input('fig_dropdown', 'value')])
def update_output(fig_name):
    return name_to_figure(fig_name)

#Plotting the figures
def name_to_figure(fig_name):
    figure = go.Figure()
    if fig_name == 'fig1':
        figure = go.Figure(data=go.Scatter(x=df["Parliamentary Constituency"],
                                y=df['Persons-2008'],
                                mode='markers',
                                marker_color=df['Persons-2008']
                                )) 
        
        figure.update_layout(template="plotly_dark", title='Scatter Plot of Population in Greater London')

    elif fig_name == 'fig2': 
        figure = go.Figure(data=go.Scatter(x=df_up["Parliamentary Constituency"],
                                y=df_up['Persons-2008'],
                                mode='markers',
                                marker_color=df_up['Persons-2008'],
                                )) 
        figure.update_layout(template="plotly_dark",title='Scatter Plot of Population in Greater London by descending order')

    return dcc.Graph(id='example-graph',
        figure= figure,
        style={'width': '220vh', 'height': '100vh'}
        
    )


if __name__ == '__main__':
    app.run_server(debug=True)
   #use_reloader=False