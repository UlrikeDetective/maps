import geopandas as gpd
import folium
import contextily as ctx
import matplotlib.pyplot as plt  # Added missing import

# 1. Load spatial data
# Ensure this path is correct for your local machine
cities = gpd.read_file('/Users/ulrike_imac_air/projects/maps/Shapefiles/san_francisco_locations.shp')

# 2. Create interactive map (Folium)
# cities.explore() returns a folium map object
m = cities.explore(color='red', marker_kwds={"radius": 5})

# 3. Add static visualization with basemap (Matplotlib + Contextily)
fig, ax = plt.subplots(figsize=(12, 8))
# Ensure the data is in Web Mercator (EPSG:3857) for contextily basemaps
cities_3857 = cities.to_crs(epsg=3857) 
cities_3857.plot(ax=ax, color='red', markersize=50)
ctx.add_basemap(ax, crs=cities_3857.crs.to_string()) 

# To display both in a notebook:
plt.show() # Shows the static map
m          # Shows the interactive map