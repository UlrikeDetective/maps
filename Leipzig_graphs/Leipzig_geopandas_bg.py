import geopandas as gpd
import geodatasets
import contextily as cx


leipzig_gdf = gpd.read_file("/Geodaten der Statistischen Bezirke der Stadt Leipzig - GeoJSON-2.json")

# Plot Leipzig
ax = leipzig_gdf.plot(figsize=(10, 10), alpha=0.5, edgecolor="k")

leipzig_gdf02 = gpd.read_file("/Ortsteile_Leipzig_UTM33N.json")

# Plot Leipzig
ax = leipzig_gdf02.plot(figsize=(10, 10), alpha=0.5, edgecolor="k")

leipzig_gdf02_wm = leipzig_gdf02.to_crs(epsg=3857)

lx = leipzig_gdf02_wm.plot(figsize=(10, 10), alpha=0.5, edgecolor="k")
cx.add_basemap(lx)

lx = leipzig_gdf02_wm.plot(figsize=(10, 10), alpha=0.5, edgecolor="k")
cx.add_basemap(lx, source=cx.providers.CartoDB.PositronNoLabels, zoom=12)
cx.add_basemap(lx, source=cx.providers.CartoDB.PositronOnlyLabels, zoom=10)

lx = leipzig_gdf02_wm.plot(figsize=(10, 10), alpha=0.5, edgecolor="k")
cx.add_basemap(lx, source=cx.providers.CartoDB.PositronNoLabels)
cx.add_basemap(lx, source=cx.providers.CartoDB.PositronOnlyLabels)

lx = leipzig_gdf02_wm.plot(figsize=(10, 10), alpha=0.5, edgecolor="k")
cx.add_basemap(lx, zoom=12)
