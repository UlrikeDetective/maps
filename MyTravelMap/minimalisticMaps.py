import sys
from functools import partial
import geopandas as gpd
from geopandas.tools import geocode
from geopy.geocoders import Nominatim
import matplotlib.pyplot as plt
import networkx as nx
import osmnx as ox

# From OpenStreetMap to Minimalistic City Maps
# How to make minimalistic city maps from OpenStreetMap data
# In this post, I’ll walk through how to download street network data from OpenStreetMap and visualize it with Python. At the heart of the operations lies the OSMnx, GeoPandas and MatPlotLib, so let’s start with importing the necessary libraries.

# Geocoding our City
# We need to select a city that we want to map, and define coordinate reference system to use. In this example, we will also use a buffer to define the area that we later want to retrieve OpenStreetMap data from. Buffering the geocoded coordinates of our city allows us to get an area of interest, and that area will be circular, which gives a nice looking visualization. We can first define our parameters:

# Use command-line argument for city name, default to Rotterdam if not provided
city_name = sys.argv[1] if len(sys.argv) > 1 else "Osaka, Japan"
buffer = 5000
crs = 3035

# Next, we can use Nominatim through the geopy library together with partial from functools to geocode the given city name, in our case Amsterdam in the Netherlands.

geolocator = Nominatim(user_agent="OSM_map")
geocode2 = partial(geolocator.geocode, language="en")
cities_df = geocode(city_name, provider='nominatim', user_agent='OSM_map', timeout=4)
cities_df = cities_df.to_crs(epsg=crs)

# Now, we have a geocoded point based on the city name we provided earlier. What we can do next, is then to buffer around this point, using the buffer variable we defined earlier. This number is the distance in meters that we buffer around the point. We also change the active geometry column to the buffer-column, as this is what we want to use to retrieve data later on. And lastly here, we reproject the GeoDataFrame to work with OSMnx.

cities_df['buffer'] = cities_df['geometry'].buffer(buffer)
# Set the active geometry column to 'buffer'
cities_df = cities_df.set_geometry('buffer')
cities_df = cities_df.to_crs(epsg=4326)

# OpenStreetMap data
# Now that we have an area polygon, we can go ahead and use OSMnx to download the road network within that area. In our case, we can download both the networks that are drivable by car and by bikes and then combine them.

drive_graph = ox.graph_from_polygon(cities_df['buffer'].iloc[0], network_type='drive')
bike_graph = ox.graph_from_polygon(cities_df['buffer'].iloc[0], network_type='bike')
graph = nx.compose(drive_graph, bike_graph)
nodes, edges = ox.graph_to_gdfs(graph)

# This code creates a graph with OSMnx, one for the drivable network and one for the bikeable network. They are then combined into one graph, before splitting the nodes and edges into separate variables. We can now use the edges to visualize the street network of Amsterdam.

# Visualizing the Street Network
# For the visualization, we can use matplotlib to make a simple plot with the edges visualized with white lines. This plot can now either be saved and taken into a different photo editing program, or you could add a background color using the ax.facecolor setting like below.

fig, ax = plt.subplots(figsize=(100,100))
fig.patch.set_facecolor('#75BFD3')
edges.plot(ax=ax, color='white', linewidth=4)
ax.set_axis_off()
# Save the plot
plt.savefig("maps/osaka_map.png", format='png', dpi=150)
plt.close()
