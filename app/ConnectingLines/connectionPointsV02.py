import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from PIL import Image


LABEL_OFFSETS = {
    "Barcelona, Spain": (0.2, 0.2),
    "Valencia, Spain": (0.25, -0.2),
    "Tarifa, Spain": (-0.45, -0.15),
    "Sevilla, Spain": (-0.35, 0.25),
    "Cadiz, Spain": (0.25, -0.3),
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
        dx, dy = LABEL_OFFSETS[city]
        ax.annotate(
            city,
            xy=(lon[i], lat[i]),
            xytext=(lon[i] + dx, lat[i] + dy),
            fontsize=14,
            fontweight="bold",
            arrowprops=dict(arrowstyle="-", linewidth=1, color="#01393D"),
            bbox=dict(facecolor="#58989F", edgecolor="none", alpha=0.85, pad=0.3),
            zorder=10
        )

    ax.set_facecolor("#58989F")
    ax.axis("off")

    plt.savefig("city_map_leaders.png", dpi=300, bbox_inches="tight", pad_inches=0)
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
Image.open("city_map_leaders.png").show()
