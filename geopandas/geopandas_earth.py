# Import the necessary library
import geopandas as gpd

# Load a sample GeoDataFrame 
gdf = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Plot the country-level world map
gdf.plot(edgecolor = 'red')

# Dissolve polygons by the 'continent' attribute to 
# combine countries into continents
gdf_dissolved = gdf.dissolve(by='continent')

# Display the dissolved GeoDataFrame
print("Dissolved GeoDataFrame:", "\n")
display(gdf_dissolved)

# Print the size of the GeoDataFrame before and after the operation
print("Number of records before the dissolve: ", len(gdf), "\n")
print("Number of records before the dissolve: ", len(gdf_dissolved), "\n")

# Plot the dissolved GeoDataFrame to visualize the combined continents
gdf_dissolved.plot(edgecolor = 'red')
