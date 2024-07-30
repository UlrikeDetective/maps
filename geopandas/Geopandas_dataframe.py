import pandas as pd

# Define a list of dictionaries with city 
# names and their geographic locations
df_cities = pd.DataFrame([
    {'name': 'Budapest',    'longitude': 19.0402,   'latitude': 47.4979},
    {'name': 'Vienna',      'longitude': 16.3738,   'latitude': 48.2082},
    {'name': 'Barcelona',   'longitude': 2.1734,    'latitude': 41.3851},
    {'name': 'New York',    'longitude': -74.006,   'latitude': 40.7128},
    {'name': 'Los Angeles', 'longitude': -118.2437, 'latitude': 34.0522},
    {'name': 'Helsinki',    'longitude': 24.9354,   'latitude': 60.1695},
    {'name': 'Dublin',      'longitude': -6.2603,   'latitude': 53.3498},
    {'name': 'London',      'longitude': -0.1278,   'latitude': 51.5074},
    {'name': 'Amsterdam',   'longitude': 4.9041,    'latitude': 52.3676}
])

# Display the first 5 rows of the DataFrame
print("Pandas DataFrame:", "\n")
display(df_cities.head(5))
