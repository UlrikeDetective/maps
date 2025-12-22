import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from PIL import Image


# -----------------------------
# Get GPS coordinates for a city
# -----------------------------
def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="city_mapper")
    location = geolocator.geocode(city_name)
    return (location.latitude, location.longitude)


# -----------------------------
# Plot cities (screen display)
# -----------------------------
def plot_cities(coordinates, cities):
    latitudes, longitudes = zip(*coordinates)

    plt.figure(figsize=(8, 6))
    plt.scatter(longitudes, latitudes, color="#6F452D", zorder=10)

    for i, city in enumerate(cities):
        plt.text(
            longitudes[i] + 0.1,
            latitudes[i] + 0.1,
            city,
            fontsize=14,
            fontweight="bold"
        )

    # Dotted connecting route
    plt.plot(
        longitudes,
        latitudes,
        color="#01393D",
        linewidth=3,
        linestyle=":",
        zorder=3
    )

    plt.gca().set_facecolor("#58989F")
    plt.axis("off")  # ✅ remove axes, ticks, coordinates

    plt.show()


# -----------------------------
# Calculate distances
# -----------------------------
def calculate_distances(coordinates):
    distances = []
    for i in range(len(coordinates) - 1):
        distance = round(
            geodesic(coordinates[i], coordinates[i + 1]).kilometers, 1
        )
        distances.append(distance)
    return distances


# -----------------------------
# Save clean PNG image
# -----------------------------
def save_image(coordinates, cities):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)

    latitudes, longitudes = zip(*coordinates)

    ax.scatter(longitudes, latitudes, color="#B77651", zorder=5)
    ax.plot(longitudes, latitudes, color="#01393D", linewidth=3, zorder=3)

    for i, city in enumerate(cities):
        ax.text(
            longitudes[i] + 0.1,
            latitudes[i] + 0.1,
            city,
            fontsize=14,
            fontweight="bold"
        )

    ax.set_facecolor("#58989F")
    ax.axis("off")  # ✅ remove axes in saved file

    plt.savefig(
        "city_map.png",
        dpi=300,
        bbox_inches="tight",
        pad_inches=0,
        facecolor=fig.get_facecolor()
    )
    plt.close(fig)


# -----------------------------
# Display saved image
# -----------------------------
def display_image():
    img = Image.open("city_map.png")
    img.show()


# -----------------------------
# Main execution
# -----------------------------
cities = [
    "Barcelona, Spain",
    "Valencia, Spain",
    "Tarifa, Spain",
    "Sevilla, Spain",
    "Cadiz, Spain"
]

coordinates = [get_coordinates(city) for city in cities]

plot_cities(coordinates, cities)

distances = calculate_distances(coordinates)
print("Rounded distances between cities in kilometers:", distances)

save_image(coordinates, cities)
display_image()
