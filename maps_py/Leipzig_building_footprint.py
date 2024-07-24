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

gdf_no = ox.features_from_place("Nordost, Leipzig, Germany", tags)
gdf_proj_no = ox.projection.project_gdf(gdf_no)
fp = f"./{img_folder}/NO_bldgs.{extension}"
fig, ax = ox.plot_footprints(gdf_proj_no, filepath=fp, dpi=400, save=True, show=False, close=True, bgcolor="w", color="b")
Image(fp, height=size, width=size)

gdf_o = ox.features_from_place("Ost, Leipzig, Germany", tags)
gdf_proj_o = ox.projection.project_gdf(gdf_o)
fp = f"./{img_folder}/mitte_bldgs.{extension}"
fig, ax = ox.plot_footprints(gdf_proj_o, filepath=fp, dpi=400, save=True, show=False, close=True, bgcolor="w", color="b")
Image(fp, height=size, width=size)

gdf_so = ox.features_from_place("Suedost, Leipzig, Germany", tags)
gdf_proj_so = ox.projection.project_gdf(gdf_so)
fp = f"./{img_folder}/SO_bldgs.{extension}"
fig, ax = ox.plot_footprints(gdf_proj_so, filepath=fp, dpi=400, save=True, show=False, close=True, bgcolor="w", color="b")
Image(fp, height=size, width=size)

gdf_s = ox.features_from_place("Sued, Leipzig, Germany", tags)
gdf_proj_s = ox.projection.project_gdf(gdf_s)
fp = f"./{img_folder}/SO_bldgs.{extension}"
fig, ax = ox.plot_footprints(gdf_proj_s, filepath=fp, dpi=400, save=True, show=False, close=True, bgcolor="w", color="b")
Image(fp, height=size, width=size)

gdf_sw = ox.features_from_place("Suedwest, Leipzig, Germany", tags)
gdf_proj_m = ox.projection.project_gdf(gdf_sw)
fp = f"./{img_folder}/SW_bldgs.{extension}"
fig, ax = ox.plot_footprints(gdf_proj_sw, filepath=fp, dpi=400, save=True, show=False, close=True, bgcolor="w", color="b")
Image(fp, height=size, width=size)

gdf_w = ox.features_from_place("West, Leipzig, Germany", tags)
gdf_proj_w = ox.projection.project_gdf(gdf_w)
fp = f"./{img_folder}/W_bldgs.{extension}"
fig, ax = ox.plot_footprints(gdf_proj_w, filepath=fp, dpi=400, save=True, show=False, close=True, bgcolor="w", color="b")
Image(fp, height=size, width=size)

gdf_aw = ox.features_from_place("Altwest, Leipzig, Germany", tags)
gdf_proj_aw = ox.projection.project_gdf(gdf_aw)
fp = f"./{img_folder}/AW_bldgs.{extension}"
fig, ax = ox.plot_footprints(gdf_proj_aw, filepath=fp, dpi=400, save=True, show=False, close=True, bgcolor="w", color="b")
Image(fp, height=size, width=size)

gdf_nw = ox.features_from_place("Nordwest, Leipzig, Germany", tags)
gdf_proj_nw = ox.projection.project_gdf(gdf_nw)
fp = f"./{img_folder}/NW_bldgs.{extension}"
fig, ax = ox.plot_footprints(gdf_proj_nw, filepath=fp, dpi=400, save=True, show=False, close=True, bgcolor="w", color="b")
Image(fp, height=size, width=size)

gdf_n = ox.features_from_place("Nord, Leipzig, Germany", tags)
gdf_proj_n = ox.projection.project_gdf(gdf_n)
fp = f"./{img_folder}/Nord_bldgs.{extension}"
fig, ax = ox.plot_footprints(gdf_proj_n, filepath=fp, dpi=400, save=True, show=False, close=True, bgcolor="w", color="b")
Image(fp, height=size, width=size)
