import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from PIL import Image

def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="city_mapper")
    location = geolocator.geocode(city_name)
    return (location.latitude, location.longitude)

def plot_cities(coordinates, cities):
    latitudes, longitudes = zip(*coordinates)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(longitudes, latitudes, color="#6F452D", zorder=7)
    
    for i, city in enumerate(cities):
        plt.text(longitudes[i] + 0.1, latitudes[i] + 0.1, city, fontsize=9)
    
    # Draw dotted lines connecting the cities
    plt.plot(longitudes, latitudes, color="#BED0D0", linewidth=3, linestyle=":", zorder=3)

    plt.gca().set_facecolor('lightblue')
    plt.grid(True)
    
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()

def calculate_distances(coordinates):
    distances = []
    for i in range(len(coordinates) - 1):
        # Calculate distance and round to 2 decimal places (or change as needed)
        distance = round(geodesic(coordinates[i], coordinates[i+1]).kilometers, 1)
        distances.append(distance)
    return distances
distances = calculate_distances(coordinates)
print("Rounded distances between cities in kilometers:", distances)


def save_image(coordinates, cities):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    
    latitudes, longitudes = zip(*coordinates)
    ax.scatter(longitudes, latitudes, color="#B77651", zorder=5)
    ax.plot(longitudes, latitudes, color="#01393D", linewidth=2, zorder=3)
    
    for i, city in enumerate(cities):
        ax.text(longitudes[i] + 2.9, latitudes[i] + 0.2, city, fontsize=12)
    
    ax.set_facecolor("#58989F")
    
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    
    plt.savefig("city_map.png", bbox_inches='tight')

def display_image():
    img = Image.open("city_map.png")
    img.show()

cities = ["Barcelona, Spain", "Valencia, Spain", "Tarifa, Spain", "Sevilla, Spain", "Cadiz, Spain"]
coordinates = [get_coordinates(city) for city in cities]

plot_cities(coordinates, cities)
save_image(coordinates, cities)
display_image()
