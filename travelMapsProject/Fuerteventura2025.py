# python -m venv myenv
# source myenv/bin/activate
# python -m pip install pandas folium
# python /path_to_file/USA_SF_map2024_V02.py

# To Do - change map tile leaflet + add data from 2023

import os
import pandas as pd
import folium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from folium import CustomIcon

# Load your GPS data from CSV
df = pd.read_csv('/Users/ulrike_imac_air/projects/analysis_my_life/data/photos_gps/2025/Fuerteventura2025_cleaned_info.csv')

# Drop rows where lat or lon is NaN
df_cleaned = df.dropna(subset=['lat', 'lon'])

# Initialize a map centered around the average location in the cleaned data
map_center = [df_cleaned['lat'].mean(), df_cleaned['lon'].mean()]
mymap = folium.Map(location=map_center, zoom_start=10)

# Ensure the custom icon file exists
icon_path = 'analysis/python/redsmallpin.png'
if not os.path.exists(icon_path):
    raise FileNotFoundError(f"Icon file not found: {icon_path}")

# Plot each point on the map with the custom icon
for _, row in df_cleaned.iterrows():
    try:
        print(f"Adding marker: {row['lat']}, {row['lon']}")
        
        # Create custom icon for each marker
        icon = CustomIcon(icon_image=icon_path, icon_size=(32, 32))

        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=f"Elevation: {row.get('elevation', 'N/A')}m",
            icon=icon
        ).add_to(mymap)
    except Exception as e:
        print(f"Error adding marker: {e}")

# Save map as an HTML file
html_file = "fuerteventura2025.html"
mymap.save(html_file)

# Convert HTML map to PNG using Selenium and headless Chrome
png_file = "Fuerteventura2025.png"
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Open the HTML map in a headless browser and take a screenshot
with webdriver.Chrome(service=service, options=options) as driver:
    driver.set_window_size(1200, 800)  # Adjust size as needed
    driver.get(f"file:///{os.path.abspath(html_file)}")  # Correct file URL path
    driver.save_screenshot(png_file)

print(f"Map saved as {png_file}")
