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
    plt.scatter(longitudes, latitudes, color="red", zorder=5)
    
    for i, city in enumerate(cities):
        plt.text(longitudes[i] + 0.1, latitudes[i] + 0.1, city, fontsize=9)
    
    plt.plot(longitudes, latitudes, color="blue", linewidth=2, zorder=3)
    plt.gca().set_facecolor('lightblue')
    plt.grid(True)
    
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()

def save_image(coordinates, cities):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    
    latitudes, longitudes = zip(*coordinates)
    ax.scatter(longitudes, latitudes, color="red", zorder=5)
    ax.plot(longitudes, latitudes, color="blue", linewidth=2, zorder=3)
    
    for i, city in enumerate(cities):
        ax.text(longitudes[i] + 0.1, latitudes[i] + 0.1, city, fontsize=9)
    
    ax.set_facecolor("lightblue")
    
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    
    plt.savefig("city_map.png", bbox_inches='tight')

def display_image():
    img = Image.open("city_map.png")
    img.show()

cities = ["New York, USA", "London, UK", "Paris, France", "Berlin, Germany"]
coordinates = [get_coordinates(city) for city in cities]

plot_cities(coordinates, cities)
save_image(coordinates, cities)
display_image()