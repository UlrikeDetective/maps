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



M = ox.graph_from_place("Mitte, Leipzig, Saxony, Germany", network_type="drive")
edge_centrality = nx.closeness_centrality(nx.line_graph(M))
nx.set_edge_attributes(M, edge_centrality, "edge_centrality")
ec = ox.plot.get_edge_colors_by_attr(M, "edge_centrality", cmap="plasma")
fig, ax = ox.plot_graph(M, edge_color=ec, bgcolor="w", edge_linewidth=2, node_size=0)

NO = ox.graph_from_place("Nordost, Leipzig, Saxony, Germany", network_type="drive")
edge_centrality = nx.closeness_centrality(nx.line_graph(NO))
nx.set_edge_attributes(NO, edge_centrality, "edge_centrality")
ec = ox.plot.get_edge_colors_by_attr(NO, "edge_centrality", cmap="magma")
fig, ax = ox.plot_graph(NO, edge_color=ec, bgcolor="w", edge_linewidth=2, node_size=0)

O = ox.graph_from_place("Ost, Leipzig, Saxony, Germany", network_type="drive")
fig, ax = ox.plot_graph(O, node_size=0.7, bgcolor="w", edge_color="b")

SO = ox.graph_from_place("Suedost, Leipzig, Saxony, Germany", network_type="drive")
fig, ax = ox.plot_graph(SO, node_size=0.7, bgcolor="w", edge_color="b")

S = ox.graph_from_place("Sued, Leipzig, Saxony, Germany", network_type="drive")
edge_centrality = nx.closeness_centrality(nx.line_graph(S))
nx.set_edge_attributes(S, edge_centrality, "edge_centrality")
ec = ox.plot.get_edge_colors_by_attr(S, "edge_centrality", cmap="viridis")
fig, ax = ox.plot_graph(S, edge_color=ec, bgcolor="w", edge_linewidth=2, node_size=0)

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
