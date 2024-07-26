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
