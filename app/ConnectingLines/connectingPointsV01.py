import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from PIL import Image


LABEL_OFFSETS = {
    "Barcelona, Spain": (0.15, 0.12),
    "Valencia, Spain": (0.12, -0.18),
    "Tarifa, Spain": (-0.35, -0.10),
    "Sevilla, Spain": (-0.30, 0.20),
    "Cadiz, Spain": (0.15, -0.25),
}


def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="city_mapper")
    location = geolocator.geocode(city_name)
    return location.latitude, location.longitude


def save_image(coordinates, cities):
    fig, ax = plt.subplots(figsize=(8, 6))

    lat, lon = zip(*coordinates)

    ax.scatter(lon, lat, color="#B77651", zorder=5)
    ax.plot(lon, lat, color="#01393D", linewidth=3, zorder=3)

    for i, city in enumerate(cities):
        dx, dy = LABEL_OFFSETS.get(city, (0.1, 0.1))
        ax.text(
            lon[i] + dx,
            lat[i] + dy,
            city,
            fontsize=14,
            fontweight="bold",
            zorder=10,
            bbox=dict(facecolor="#58989F", edgecolor="none", alpha=0.85, pad=0.3)
        )

    ax.set_facecolor("#58989F")
    ax.axis("off")

    plt.savefig("city_map_manual.png", dpi=300, bbox_inches="tight", pad_inches=0)
    plt.close()


cities = [
    "Barcelona, Spain",
    "Valencia, Spain",
    "Tarifa, Spain",
    "Sevilla, Spain",
    "Cadiz, Spain"
]

coordinates = [get_coordinates(city) for city in cities]
save_image(coordinates, cities)
Image.open("city_map_manual.png").show()
