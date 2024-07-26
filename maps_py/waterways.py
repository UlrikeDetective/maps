mport multiprocessing as mp

import numpy as np
import osmnx as ox

# Define the place and custom filter for railway options
place_name = "Leipzig, Germany"
waterway_filter = '["waterway"~"canal|river|ditch|stream|drain"]'

# Get the graph for the defined place with the specified custom filter
Leip = ox.graph_from_place(
    place_name,
    retain_all=False,
    truncate_by_edge=True,
    simplify=True,
    custom_filter=waterway_filter,
)

# Plot the graph
fig, ax = ox.plot_graph(Leip, node_size=0, edge_color="b", bgcolor="white", edge_linewidth=0.2)
ox.graph_to_gdfs(Leip, nodes=False).explore()
