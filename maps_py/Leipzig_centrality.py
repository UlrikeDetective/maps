import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# Ensure you have a graph object Z loaded in your code before this step

# Calculate edge centrality
Z = ox.graph_from_place("Leipzig, Saxony, Germany", network_type="drive")
edge_centrality = nx.closeness_centrality(nx.line_graph(Z))
nx.set_edge_attributes(Z, edge_centrality, "edge_centrality")

# Get edge colors based on centrality
ec = ox.plot.get_edge_colors_by_attr(Z, "edge_centrality", cmap="inferno")

# Plot the graph
fig, ax = ox.plot_graph(Z, edge_color=ec, edge_linewidth=2, node_size=0, bgcolor="w")
