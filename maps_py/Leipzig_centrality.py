import multiprocessing as mp

import numpy as np
import osmnx as ox

np.random.seed(0)

# convert graph to line graph so edges become nodes and vice versa
edge_centrality = nx.closeness_centrality(nx.line_graph(Z))
nx.set_edge_attributes(Z, edge_centrality, "edge_centrality")

ec = ox.plot.get_edge_colors_by_attr(Z, "edge_centrality", cmap="inferno")
fig, ax = ox.plot_graph(Z, edge_color=ec, edge_linewidth=2, node_size=0)
