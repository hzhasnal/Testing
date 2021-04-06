import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

# Create a Dash app and use the dash-bootstrap-components stylesheet
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Read the data
data = pd.read_csv('parliamentary-constituency-profiles-data (1).csv', skiprows=[1])

# Create the bar chart
fig = px.bar(data, x="GEO_LABEL", y="POPULATION", color="Mean Income")

fig.update_layout(
    title='Population v.s. Mean Income',
    xaxis=dict(
        title='London Area',
    ),
    yaxis=dict(
        title='Population',
    ),
)



# Create the app layout
app.layout = html.Div(children=[
    html.H1(children='Market Pontential in Greater London'),

    html.Div(children='''
        A bar chart of population with mean income in Greater London
    '''),

    dcc.Graph(
        figure= fig,
        style={'width': '200vh', 'height': '90vh'}

    )
])

# Run the web app server (turn off reloader as we are running it inside a Jupyter notebook)
if __name__ == '__main__':
    app.run_server(port=8050, debug=True, use_reloader=False)
