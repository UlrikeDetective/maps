import multiprocessing as mp

import numpy as np
import osmnx as ox

np.random.seed(0)

# download/model a street network for some city then visualize it
Z = ox.graph_from_place("Leipzig, Saxony, Germany", network_type="drive")
fig, ax = ox.plot_graph(Z, node_size=0.7, bgcolor="w", edge_color="b")

M = ox.graph_from_place("Mitte, Leipzig, Saxony, Germany", network_type="drive")
fig, ax = ox.plot_graph(M, node_size=0.7, bgcolor="w", edge_color="b")

S = ox.graph_from_place("Sued, Leipzig, Saxony, Germany", network_type="drive")
fig, ax = ox.plot_graph(S, node_size=0.7, bgcolor="w", edge_color="b")
