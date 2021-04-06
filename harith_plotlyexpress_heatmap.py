import plotly.express as px
import pandas as pd
import json
import plotly.io as pio
import os

pio.renderers.default = 'browser'

# Read the data 
DATA_DIR = 'data'
data = os.path.join(DATA_DIR,'parliamentary-constituency-profiles-data.csv')
data = pd.read_csv(data, usecols=["Area Code", "Parliamentary Constituency", "Property & Business Services-2004"])

#Read the Json File
with open('constituency.json') as json_file:
    la_geojson = json.load(json_file)

state_id_map = {}
for feature in la_geojson["features"]:
    feature["id"] = feature["properties"]['PCON13CDO']
    state_id_map[feature["properties"]['PCON13NM']] = feature["id"]

# Create the choropleth mapbox
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

fig.show()