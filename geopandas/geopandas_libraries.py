# Import the GeoPandas library
import geopandas as gpd
print(gpd.__version__)

# Query the available built-in datasets in GeoPandas
available_datasets = gpd.datasets.available

# Print the list of available datasets
print("Available built-in datasets in GeoPandas:", "\n")
print(available_datasets, "\n")

# Import the GeoPandas library
import geopandas as gpd

# Query the location of the data file
file_name = 'naturalearth_lowres'
file_path = gpd.datasets.get_path(file_name)

# Print the file path of the sample data
print(file_path, "\n")

# Read a built-in dataset (naturalearth_lowres) into a GeoDataFrame
gdf = gpd.read_file(file_path)

# Display the first 3 rows of the GeoDataFrame
gdf.head(10)

# Import the GeoPandas library
import geopandas as gpd

# Query the location of the data file
file_name = 'naturalearth_cities'
file_path = gpd.datasets.get_path(file_name)

# Print the file path of the sample data
print(file_path, "\n")

# Read a built-in dataset (naturalearth_lowres) into a GeoDataFrame
gdf = gpd.read_file(file_path)

# Display the first 3 rows of the GeoDataFrame
gdf.head(10)
