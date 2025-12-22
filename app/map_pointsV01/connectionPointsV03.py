import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from adjustText import adjust_text
from PIL import Image


def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="city_mapper")
    location = geolocator.geocode(city_name)
    return location.latitude, location.longitude


def save_image(coordinates, cities):
    fig, ax = plt.subplots(figsize=(8, 6))
    lat, lon = zip(*coordinates)

    ax.scatter(lon, lat, color="#B77651", zorder=10)
    ax.plot(lon, lat, color="#01393D", linewidth=3, linestyle=":", zorder=3)

    texts = []
    for i, city in enumerate(cities):
        texts.append(
            ax.text(
                lon[i],
                lat[i],
                city,
                fontsize=14,
                fontweight="bold",
                bbox=dict(facecolor="#58989F", edgecolor="none", alpha=0.55, pad=0.9),
                zorder=12
            )
        )

    adjust_text(
        texts,
        ax=ax,
        expand_points=(2.5, 2.5), # distance from points
        expand_text=(2.0, 2.0), # distance between labels
        force_points=0.6, # strength of repulsion from points
        force_text=0.6, # strength of repulsion from other labels
        arrowprops=dict(
            arrowstyle="-",
            color="#01393D",
            linewidth=1)
    )

    ax.set_facecolor("#58989F")
    ax.axis("off")

    plt.savefig("city_map_auto.png", dpi=300, bbox_inches="tight", pad_inches=0)
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
Image.open("city_map_auto.png").show()
