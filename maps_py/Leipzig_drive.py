import multiprocessing as mp

import numpy as np
import osmnx as ox

np.random.seed(0)

# download/model a street network for Leipzig and the suburbs of Leipzig then visualize it - using drive
Z = ox.graph_from_place("Leipzig, Saxony, Germany", network_type="drive")
fig, ax = ox.plot_graph(Z, node_size=0.7, bgcolor="w", edge_color="b")

M = ox.graph_from_place("Mitte, Leipzig, Saxony, Germany", network_type="drive")
fig, ax = ox.plot_graph(M, node_size=0.7, bgcolor="w", edge_color="b")

NO = ox.graph_from_place("Nordost, Leipzig, Saxony, Germany", network_type="drive")
fig, ax = ox.plot_graph(NO, node_size=0.7, bgcolor="w", edge_color="b")

O = ox.graph_from_place("Ost, Leipzig, Saxony, Germany", network_type="drive")
fig, ax = ox.plot_graph(O, node_size=0.7, bgcolor="w", edge_color="b")

SO = ox.graph_from_place("Suedost, Leipzig, Saxony, Germany", network_type="drive")
fig, ax = ox.plot_graph(SO, node_size=0.7, bgcolor="w", edge_color="b")

S = ox.graph_from_place("Sued, Leipzig, Saxony, Germany", network_type="drive")
fig, ax = ox.plot_graph(S, node_size=0.7, bgcolor="w", edge_color="b")

SW = ox.graph_from_place("Suedwest, Leipzig, Saxony, Germany", network_type="drive")
fig, ax = ox.plot_graph(SW, node_size=0.7, bgcolor="w", edge_color="b")

W = ox.graph_from_place("West, Leipzig, Saxony, Germany", network_type="drive")
fig, ax = ox.plot_graph(W, node_size=0.7, bgcolor="w", edge_color="b")

AW = ox.graph_from_place("Altwest, Leipzig, Saxony, Germany", network_type="drive")
fig, ax = ox.plot_graph(AW, node_size=0.7, bgcolor="w", edge_color="b")

NW = ox.graph_from_place("Nordwest, Leipzig, Saxony, Germany", network_type="drive")
fig, ax = ox.plot_graph(NW, node_size=0.7, bgcolor="w", edge_color="b")

N = ox.graph_from_place("Nord, Leipzig, Saxony, Germany", network_type="drive")
fig, ax = ox.plot_graph(N, node_size=0.7, bgcolor="w", edge_color="b")
