import folium

# Create a basic map centered at a location (latitude, longitude)
map = folium.Map(location=[37.7749, -122.4194], zoom_start=13)

# Add a simple marker (customize with different icon colors and shapes)
folium.Marker(
    location=[37.7749, -122.4194],
    popup="San Francisco",
    icon=folium.Icon(color="green", icon="info-sign")
).add_to(map)

# Add a circle marker with a specific color and radius
folium.CircleMarker(
    location=[37.7749, -122.4194],
    radius=10,
    popup="Custom Circle Marker",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc"
).add_to(map)

# Save the map to an HTML file
map.save("custom_map.html")
