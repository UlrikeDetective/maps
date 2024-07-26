mport multiprocessing as mp

import numpy as np
import osmnx as ox

# get Leipzig tram network
Lei = ox.graph_from_place(
    "Leipzig, Saxony, Germany",
    retain_all=False,
    truncate_by_edge=True,
    simplify=True,
    custom_filter='["railway"~"tram"]',
)

fig, ax = ox.plot_graph(Lei, node_size=0, edge_color="b", bgcolor="white", edge_linewidth=0.2)

import osmnx as ox

# Define the place and custom filter for railway options
place_name = "Leipzig, Germany"
railway_filter = '["railway"~"tram|subway|rail|light_rail|funicular|monorail|narrow_gauge|preserved|miniature"]'

# Get the graph for the defined place with the specified custom filter
Leip = ox.graph_from_place(
    place_name,
    retain_all=False,
    truncate_by_edge=True,
    simplify=True,
    custom_filter=railway_filter,
)

# Plot the graph
fig, ax = ox.plot_graph(SF, node_size=0, edge_color="b", bgcolor="white", edge_linewidth=0.2)
ox.graph_to_gdfs(Leip, nodes=False).explore()

import osmnx as ox

# Define the place and custom filter for railway options
place_name = "San Francisco, California, USA"
railway_filter = '["railway"~"tram|subway|rail|light_rail|funicular|monorail|narrow_gauge|preserved|miniature"]'

# Get the graph for the defined place with the specified custom filter
SF = ox.graph_from_place(
    place_name,
    retain_all=False,
    truncate_by_edge=True,
    simplify=True,
    custom_filter=railway_filter,
)

# Plot the graph
fig, ax = ox.plot_graph(SF, node_size=0, edge_color="b", bgcolor="white", edge_linewidth=0.2)
ox.graph_to_gdfs(SF, nodes=False).explore()
