mport multiprocessing as mp

import numpy as np
import osmnx as ox

import osmnx as ox

# Define the place and custom filter for railway options
place_name = "Leipzig, Germany"
highway_filter = '["highway"~"motorway|trunk|primary|secondary|tertiary|residential|unclassified|service"]'

# Get the graph for the defined place with the specified custom filter
Leip = ox.graph_from_place(
    place_name,
    retain_all=False,
    truncate_by_edge=True,
    simplify=True,
    custom_filter=highway_filter,
)

# Plot the graph
fig, ax = ox.plot_graph(Leip, node_size=0, edge_color="b", bgcolor="white", edge_linewidth=0.2)
ox.graph_to_gdfs(Leip, nodes=False).explore()

import osmnx as ox

# Define the place and custom filter for railway options
place_name = "Leipzig, Germany"
amenity_filter = '["amenity"~"school|hospital|restaurant|bar|cafe|bank|post_office|police|fire_station"]'

# Get the graph for the defined place with the specified custom filter
Leip = ox.graph_from_place(
    place_name,
    retain_all=False,
    truncate_by_edge=True,
    simplify=True,
    custom_filter=amenity_filter,
)

# Plot the graph
fig, ax = ox.plot_graph(Leip, node_size=0, edge_color="b", bgcolor="white", edge_linewidth=0.2)
ox.graph_to_gdfs(Leip, nodes=False).explore()

import osmnx as ox

# Define the place and custom filter for railway options
place_name = "Leipzig, Germany"
building_filter = '["building"]'

# Get the graph for the defined place with the specified custom filter
Leip = ox.graph_from_place(
    place_name,
    retain_all=False,
    truncate_by_edge=True,
    simplify=True,
    custom_filter=building_filter,
)

# Plot the graph
fig, ax = ox.plot_graph(Leip, node_size=0, edge_color="b", bgcolor="white", edge_linewidth=0.2)
ox.graph_to_gdfs(Leip, nodes=False).explore()

import osmnx as ox

# Define the place
place_name = "San Francisco, California, USA"

# Define custom filters
highway_filter = '["highway"~"motorway|trunk|primary|secondary|tertiary|residential|unclassified|service"]'
amenity_filter = '["amenity"~"school|hospital|restaurant|bar|cafe|bank|post_office|police|fire_station"]'
building_filter = '["building"]'
landuse_filter = '["landuse"~"residential|commercial|industrial|forest|farmland|meadow"]'
natural_filter = '["natural"~"wood|water|beach|coastline|grassland|tree"]'
leisure_filter = '["leisure"~"park|pitch|playground|sports_centre|swimming_pool|garden"]'
shop_filter = '["shop"~"supermarket|convenience|clothes|bakery|pharmacy"]'
tourism_filter = '["tourism"~"hotel|museum|gallery|attraction|zoo|theme_park"]'

# Get the data using filters
G_highways = ox.graph_from_place(place_name, custom_filter=highway_filter)
amenities = ox.features_from_place(place_name, tags={"amenity": True})
buildings = ox.features_from_place(place_name, tags={"building": True})
landuse = ox.features_from_place(place_name, tags={"landuse": True})
natural_features = ox.features_from_place(place_name, tags={"natural": True})
leisure = ox.features_from_place(place_name, tags={"leisure": True})
shops = ox.features_from_place(place_name, tags={"shop": True})
tourism = ox.features_from_place(place_name, tags={"tourism": True})

# Plot the data (example for highways)
fig, ax = ox.plot_graph(G_highways, node_size=0, edge_color="b", bgcolor="white", edge_linewidth=0.2)
fig, ax = ox.plot_footprints(amenities, color="blue", bgcolor="white", show=True, close=False)
fig, ax = ox.plot_footprints(buildings, color="blue", bgcolor="white", show=True, close=False)
fig, ax = ox.plot_footprints(landuse, color="blue", bgcolor="white", show=True, close=False)
fig, ax = ox.plot_footprints(natural_features, color="blue", bgcolor="white", show=True, close=False)
fig, ax = ox.plot_footprints(leisure, color="blue", bgcolor="white", show=True, close=False)
fig, ax = ox.plot_footprints(shops, color="blue", bgcolor="white", show=True, close=False)
fig, ax = ox.plot_footprints(tourism, color="blue", bgcolor="white", show=True, close=False)
