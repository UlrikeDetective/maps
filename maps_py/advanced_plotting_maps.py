import matplotlib.pyplot as plt
import osmnx as ox

place = "Leipzig, Germany"
G = ox.graph_from_place(place, network_type="drive")

# get n evenly-spaced colors from some matplotlib colormap
ox.plot.get_colors(n=5, cmap="PuBu")

# get node colors by linearly mapping an attribute's values to a colormap
nc = ox.plot.get_node_colors_by_attr(G, attr="y", cmap="PuBu")
fig, ax = ox.plot_graph(G, node_color=nc, edge_linewidth=0.3, bgcolor="w")

# when num_bins is not None, bin the nodes/edges then assign one color to each bin
# also set equal_size=True for equal-sized quantiles (requires unique bin edges!)
ec = ox.plot.get_edge_colors_by_attr(G, attr="length", num_bins=5)

# otherwise, when num_bins is None (default), linearly map one color to each node/edge by value
ec = ox.plot.get_edge_colors_by_attr(G, attr="length")

# plot the graph with colored edges
fig, ax = ox.plot_graph(G, node_size=5, edge_color=ec, bgcolor="w")
