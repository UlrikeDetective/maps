import multiprocessing as mp

import numpy as np
import osmnx as ox

# download/model a street network for some city then visualize it
Holz = ox.graph_from_place("Holzhausen, Suedost, Leipzig, Saxony, Germany", network_type="drive")
fig, ax = ox.plot_graph(Holz, node_size=0.7, bgcolor="w", edge_color="b")