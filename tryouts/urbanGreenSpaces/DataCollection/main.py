from owslib.wfs import WebFeatureService
from downloader import (download_osm_data,
                        download_osm_buildings,
                        download_demography_data,
                        download_road_network)
import pandas as pd

# Example usage:
if __name__ == '__main__':
    print("Hello Ulrike")

    # Download Leipzig road network
    download_road_network("Leipzig, Germany", "data/Leipzig_roads_highways.geojson")

    # Load and process Leipzig population density data for 2024
    csv_path = "Bevölkerungsbestand_Einwohnerdichte_Stadtbezirke.csv"
    df = pd.read_csv(csv_path)
    df.columns = [col.strip().replace('\ufeff', '') for col in df.columns]
    # Only keep rows where 'Sachmerkmal' is 'Einwohnerdichte'
    df = df[df['Sachmerkmal'] == 'Einwohnerdichte']
    # Select relevant columns
    result = df[["Gebiet", "2024"]].copy()
    # Convert density to float (replace comma with dot, remove quotes)
    result["2024"] = result["2024"].astype(str).str.replace(",", ".").str.replace('"', '').astype(float)
    print("\nEinwohnerdichte Leipzig 2024 by Stadtbezirk:")
    print(result)

    """
    # Use the base WFS URL (no GetCapabilities params!)
    url = "https://gdi.berlin.de/services/wfs/ua_einwohnerdichte_2023"

    wfs = WebFeatureService(url=url, version="2.0.0")
    print("\nAvailable Layers:")
    for layer in list(wfs.contents):
        print("🔹", layer)


    # ------- Download Demography Data -------
    base_url = "https://gdi.berlin.de/services/wfs/ua_einwohnerdichte_2023"
    layer = "ua_einwohnerdichte_2023:einwohnerdichte2023"
    output_path = "data/berlin_population_density.geojson"

    download_demography_data(base_url, layer, output_path)

# download_osm_data("Berlin, Germany", "data/berlin_green.geojson")

# ------- Download the Green Area -------
# download_osm_buildings("Mitte, Berlin, Germany", "data/berlin_mitte_buildings.geojson")
# OR
# --- bbox = (52.54, 52.49, 13.42, 13.37)  # North, South, East, West
# --- download_osm_buildings("Berlin", "data/berlin_subset.geojson", bbox=bbox)

"""