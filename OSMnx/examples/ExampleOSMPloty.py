import plotly.express as px
import pandas as pd

# Load your custom dataset
df = pd.read_csv('/Users/ulrike_imac_air/projects/maps/OSMnx/examples/data.csv')

# Create the scatter map box
fig = px.scatter_mapbox(
    df,
    lat="latitude",  # Replace with your latitude column
    lon="longitude",  # Replace with your longitude column
    color="region",  # Replace with your color column
    size="population",  # Replace with your size column
    color_continuous_scale=px.colors.cyclical.IceFire,
    size_max=15,
    zoom=10,
    mapbox_style="open-street-map"
)

# Update the layout with a title and margins
fig.update_layout(
    title="Custom Data Visualization",
    margin={"r":0,"t":0,"l":0,"b":0},
    height=600,
    width=800
)

# Show the map
fig.show()
