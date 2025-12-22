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

    # Route + points
    ax.scatter(lon, lat, color="#B77651", zorder=5)
    ax.plot(lon, lat, color="#01393D", linewidth=3, linestyle=":", zorder=3)

    texts = []

    for i, city in enumerate(cities):
        # IMPORTANT: offset in *points*, not degrees
        text = ax.annotate(
            city,
            xy=(lon[i], lat[i]),
            xytext=(1, -1),          # 👈 guaranteed distance
            textcoords="offset points",
            fontsize=14,
            fontweight="bold",
            bbox=dict(
                facecolor="#58989F",
                edgecolor="none",
                alpha=0.85,
                pad=0.3
            ),
            arrowprops=dict(
                arrowstyle="-",
                color="#52D714",
                linewidth=1
            ),
            zorder=2
        )
        texts.append(text)

    # Optional: refine label spacing between themselves
    adjust_text(
        texts,
        ax=ax,
        only_move={"points": "y", "text": "xy"},
        force_text=13.3
    )

    ax.set_facecolor("#58989F")
    ax.axis("off")

    plt.savefig(
        "city_map_auto_spacing.png",
        dpi=300,
        bbox_inches="tight",
        pad_inches=0
    )
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
Image.open("city_map_auto_spacing.png").show()
