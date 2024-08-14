import plotly.express as px
import pandas as pd

# Load the car share dataset
df = px.data.carshare()
print(df.head())

# Create the scatter map box
fig = px.scatter_mapbox(
    df,
    lat="centroid_lat",
    lon="centroid_lon",
    color="peak_hour",
    size="car_hours",
    color_continuous_scale=px.colors.cyclical.IceFire,
    size_max=15,
    zoom=10,
    mapbox_style="open-street-map"
)

# Update the layout with a title and margins
fig.update_layout(
    title="Montreal Car Share Data",
    margin={"r":0,"t":0,"l":0,"b":0},
    height=600,
    width=800
)

# Show the map
fig.show()
