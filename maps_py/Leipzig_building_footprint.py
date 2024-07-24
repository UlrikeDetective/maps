import osmnx as ox
from IPython.display import Image

# configure the inline image display
img_folder = "images"
extension = "png"
size = 240

# specify that we're retrieving building features from OSM
tags = {"building": True}

gdf_m = ox.features_from_place("Mitte, Leipzig, Germany", tags)
gdf_proj_m = ox.projection.project_gdf(gdf_m)
fp = f"./{img_folder}/mitte_bldgs.{extension}"
fig, ax = ox.plot_footprints(gdf_proj_m, filepath=fp, dpi=400, save=True, show=False, close=True, bgcolor="w", color="b")
Image(fp, height=size, width=size)
