import osmnx as ox

# Get the buildings data for a specific place
gdf_s = ox.features_from_place("Sued, Leipzig, Germany", tags={"building": True})
# Define columns to display in the tooltip
cols = ["height", "addr:housenumber", "addr:street", "addr:postcode"]
# Explore the data using a different tile provider
gdf_s.explore(tiles="CartoDB Positron", tooltip=cols)

# explore a neighborhood's buildings + street network interactively
NO = "Nordost, Leipzig, Germany"
cols = ["height", "addr:housenumber", "addr:street", "addr:postcode"]
G = ox.graph_from_place(NO, network_type="drive", truncate_by_edge=True)
gdf = ox.features_from_place(NO, tags={"building": True})
m = gdf.explore(tiles=tiles, tooltip=cols)
ox.graph_to_gdfs(G, nodes=False).explore(m=m, color="yellow")

# Common Tile Providers:
# OpenStreetMap
gdf_s.explore(tiles="OpenStreetMap", tooltip=cols)

# Stamen Terrain
gdf_s.explore(tiles="Stamen Terrain", tooltip=cols)

#Stamen Toner
gdf_s.explore(tiles="Stamen Toner", tooltip=cols)

#Stamen Watercolor
gdf_s.explore(tiles="Stamen Watercolor", tooltip=cols)

#CartoDB Positron
gdf_s.explore(tiles="CartoDB Positron", tooltip=cols)

#CartoDB Dark Matter
gdf_s.explore(tiles="CartoDB Dark Matter", tooltip=cols)

#OpenTopoMap
gdf_s.explore(tiles="OpenTopoMap", tooltip=cols)

# Esri World Imagery
gdf_s.explore(tiles="Esri WorldImagery", tooltip=cols)

#Other Tile Providers:
#Esri World Street Map
gdf_s.explore(tiles="Esri WorldStreetMap", tooltip=cols)

#Esri DeLorme
gdf_s.explore(tiles="Esri DeLorme", tooltip=cols)

#Esri National Geographic
gdf_s.explore(tiles="Esri NatGeoWorldMap", tooltip=cols)

#Hike & Bike
gdf_s.explore(tiles="HikeBike.HikeBike", tooltip=cols)

#NASAGIBS.ViirsEarthAtNight2012
gdf_s.explore(tiles="NASAGIBS.ViirsEarthAtNight2012", tooltip=cols)
