import urllib.parse
import matplotlib.pyplot as plt

import geopandas as gpd
import pandas as pd

# these are the rough bounds of the earthquake and its aftershocks
minlatitude, maxlatitude = 27, 29
minlongitude, maxlongitude = 84, 87

# limiting the search to April and May 2015, and only those >= 5 magnitude
CATALOG_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query.geojson"
params = {
    "starttime": "2015-04-01",
    "endtime": "2015-05-31",
    "maxlatitude": maxlatitude,
    "minlatitude": minlatitude,
    "maxlongitude": maxlongitude,
    "minlongitude": minlongitude,
    "minmagnitude": 5,
    "eventtype": "earthquake",
    "orderby": "time",
}
columns = ["mag", "time", "geometry"]

def plot_earthquakes(quakes, nepal):
    fig, ax = plt.subplots(figsize=(10, 8))
    # Plot Nepal's boundary
    nepal.plot(ax=ax, color="none", edgecolor="black", linewidth=1)
    # Plot earthquakes as scatter points
    quakes.plot(
        ax=ax,
        kind="scatter",
        x="longitude",
        y="latitude",
        c="mag",
        cmap="Reds",
        colorbar=True,
        alpha=0.7,
        label="Magnitude",
    )
    plt.title("Earthquakes in Nepal (April-May 2015)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend()
    plt.show()

def main():
    url = f"{CATALOG_URL}?{urllib.parse.urlencode(params)}"
    quakes = gpd.read_file(url, columns=columns)

    # get the national boundary of Nepal
    boundary_url = "https://media.githubusercontent.com/media/wmgeolab/geoBoundaries/refs/heads/main/releaseData/gbOpen/NPL/ADM0/geoBoundaries-NPL-ADM0.geojson"
    nepal = gpd.read_file(boundary_url)

    # ensure both dataframes are in the same CRS
    quakes = quakes.to_crs(nepal.crs)

    # filter earthquakes to those within Nepal's boundaries
    quakes = quakes[quakes.within(nepal.iloc[0]['geometry'])]

    # sort from earliest to latest
    # localize the datetime to Nepal's datetime
    quakes = quakes.sort_values("time", ascending=True, ignore_index=True)
    quakes["time"] = pd.to_datetime(quakes["time"], unit="ms").dt.tz_localize(
        tz="Asia/Kathmandu",
    )

    # for working with matplotlib, add separate latitude/longitude columns
    quakes = quakes.join(
        quakes.get_coordinates().rename(columns=dict(y="latitude", x="longitude"))
    )
    plot_earthquakes(quakes, nepal)

if __name__ == "__main__":
    main()