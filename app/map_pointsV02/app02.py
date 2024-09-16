import matplotlib.pyplot as plt
import numpy as np
import geopy.distance

cities = [
    ("City A", (47.6062, -122.3321)),  # Seattle
    ("City B", (37.7749, -122.4194)),  # San Francisco
    ("City C", (40.7128, -74.0060)),  # New York City
    # ... add more cities as needed
]

distances = []
for i in range(len(cities) - 1):
    city1_coords = cities[i][1]
    city2_coords = cities[i + 1][1]
    distance = geopy.distance.distance(city1_coords, city2_coords).km
    # Round the distance to one decimal place
    distance = round(distance, 1)
    distances.append(distance)

plt.figure(figsize=(10, 8))
ax = plt.gca()
ax.set_facecolor("blue")  # Change background color to blue

x_coords = [city[1][0] for city in cities]
y_coords = [city[1][1] for city in cities]
plt.scatter(x_coords, y_coords, color="yellow", marker="o")

for i in range(len(cities) - 1):
    plt.plot([x_coords[i], x_coords[i + 1]], [y_coords[i], y_coords[i + 1]], color="white", linestyle="--")
    # Use f-string to format distance with one decimal place
    plt.text((x_coords[i] + x_coords[i + 1]) / 2, (y_coords[i] + y_coords[i + 1]) / 2, f"{distance:.1f} km", color="white")

# Add city names next to the points with larger font size
for city, coords in cities:
    plt.text(coords[0] - 0.52, coords[1] + 2.02, city, color="white", fontsize=14)

plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.gca().invert_yaxis()  # This line inverts the y-axis
plt.title("City Connections")
plt.grid(True)
plt.show()
