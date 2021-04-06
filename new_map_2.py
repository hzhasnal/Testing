import pandas as pd
import plotly.express as px  
import plotly.graph_objects as go
import json

import dash  
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ---------- Import and clean data (importing csv into pandas)
# df = pd.read_csv("intro_bees.csv")
df = pd.read_csv('parliamentary-constituency-profiles-data.csv', usecols=["Area Code", "Parliamentary Constituency", "Property & Business Services-2004"])

with open('constituency.json') as json_file:
    la_geojson = json.load(json_file)

state_id_map = {}
for feature in la_geojson["features"]:
    feature["id"] = feature["properties"]['PCON13CDO']
    state_id_map[feature["properties"]['PCON13NM']] = feature["id"]

# App layout
app.layout = html.Div([

    html.H1("London", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_type",
                 options=[
                     {"label": "Retail", "value": 'Retail'},
                     {"label": "Manufacturing", "value": 'Manufacturing'},],
                 multi=False,
                 value='Retail',
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_map', figure={})

])
# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_map', component_property='figure')],
    [Input(component_id='slct_type', component_property='value')]
)
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Year"] == option_slctd]
    dff = dff[dff["Affected by"] == "Varroa_mites"]

    # Plotly Express
    fig = px.choropleth_mapbox(data,
                           geojson=la_geojson,
                           locations="Parliamentary Constituency", 
                           featureidkey="properties.PCON13NM",
                           color="Property & Business Services-2004",
                           color_continuous_scale=px.colors.sequential.YlOrRd,
                           range_color=(0, 60),
                           mapbox_style="carto-positron",
                           zoom=9,
                           center = {"lat": 51.5074, "lon": 0.0000},
                           opacity=0.5,
                           hover_name="Parliamentary Constituency",
                           labels={'GEO_LABEL':'Property & Business Services Density'},
                           template='plotly_dark',
                           title="Property & Business Services Density in London"
                          )

    return container, fig
    
if __name__ == '__main__':
    app.run_server(debug=True)