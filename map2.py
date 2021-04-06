import plotly.express as px
import pandas as pd
import json
import plotly.io as pio
pio.renderers.default = 'browser'

with open('constituency.json') as json_file:
    geojson = json.load(json_file)


#print(geojson["features"][1]['properties'])

state_id_map = {}
for feature in geojson["features"]:
    feature["id"] = feature["properties"]['PCON13CDO']
    state_id_map[feature["properties"]['PCON13NM']] = feature["id"]

#print(state_id_map)

df = pd.read_csv('Retail_UK.csv')
df['id']=df['Parliamentary Constituency'].apply (lambda x: state_id_map[x])


fig = px.choropleth_mapbox(df,
                           geojson=geojson,
                           locations="id", 
                           featureidkey="properties.LAD19CD",
                           color="Retail",
                           color_continuous_scale='Viridis',
                           range_color=(0, 200),
                           mapbox_style="carto-positron",
                           zoom=8,
                           center = {"lat": 51.5074, "lon": 0.0000},
                           opacity=0.5,
                           hover_name="Retail",
                           labels={'GEO_LABEL':'Local authority'},
                           title="London residents over 100 in the 2011 Census"
                          )

fig.show()