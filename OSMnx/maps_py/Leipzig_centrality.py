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
edge_centrality = nx.closeness_centrality(nx.line_graph(O))
nx.set_edge_attributes(O, edge_centrality, "edge_centrality")
ec = ox.plot.get_edge_colors_by_attr(O, "edge_centrality", cmap="cividis")
fig, ax = ox.plot_graph(O, edge_color=ec, bgcolor="w", edge_linewidth=2, node_size=0)

SO = ox.graph_from_place("Suedost, Leipzig, Saxony, Germany", network_type="drive")
edge_centrality = nx.closeness_centrality(nx.line_graph(SO))
nx.set_edge_attributes(SO, edge_centrality, "edge_centrality")
ec = ox.plot.get_edge_colors_by_attr(SO, "edge_centrality", cmap="coolwarm")
fig, ax = ox.plot_graph(SO, edge_color=ec, bgcolor="w", edge_linewidth=2, node_size=0)

S = ox.graph_from_place("Sued, Leipzig, Saxony, Germany", network_type="drive")
edge_centrality = nx.closeness_centrality(nx.line_graph(S))
nx.set_edge_attributes(S, edge_centrality, "edge_centrality")
ec = ox.plot.get_edge_colors_by_attr(S, "edge_centrality", cmap="viridis")
fig, ax = ox.plot_graph(S, edge_color=ec, bgcolor="w", edge_linewidth=2, node_size=0)

SW = ox.graph_from_place("Suedwest, Leipzig, Saxony, Germany", network_type="drive")
edge_centrality = nx.closeness_centrality(nx.line_graph(SW))
nx.set_edge_attributes(SW, edge_centrality, "edge_centrality")
ec = ox.plot.get_edge_colors_by_attr(SW, "edge_centrality", cmap="seismic")
fig, ax = ox.plot_graph(SW, edge_color=ec, bgcolor="w", edge_linewidth=2, node_size=0)

W = ox.graph_from_place("West, Leipzig, Saxony, Germany", network_type="drive")
edge_centrality = nx.closeness_centrality(nx.line_graph(W))
nx.set_edge_attributes(W, edge_centrality, "edge_centrality")
ec = ox.plot.get_edge_colors_by_attr(W, "edge_centrality", cmap="tab10")
fig, ax = ox.plot_graph(W, edge_color=ec, bgcolor="w", edge_linewidth=2, node_size=0)

AW = ox.graph_from_place("Altwest, Leipzig, Saxony, Germany", network_type="drive")
edge_centrality = nx.closeness_centrality(nx.line_graph(AW))
nx.set_edge_attributes(AW, edge_centrality, "edge_centrality")
ec = ox.plot.get_edge_colors_by_attr(AW, "edge_centrality", cmap="Set1")
fig, ax = ox.plot_graph(AW, edge_color=ec, bgcolor="w", edge_linewidth=2, node_size=0)

NW = ox.graph_from_place("Nordwest, Leipzig, Saxony, Germany", network_type="drive")
edge_centrality = nx.closeness_centrality(nx.line_graph(NW))
nx.set_edge_attributes(NW, edge_centrality, "edge_centrality")
ec = ox.plot.get_edge_colors_by_attr(NW, "edge_centrality", cmap="jet")
fig, ax = ox.plot_graph(NW, edge_color=ec, bgcolor="w", edge_linewidth=2, node_size=0)

N = ox.graph_from_place("Nord, Leipzig, Saxony, Germany", network_type="drive")
edge_centrality = nx.closeness_centrality(nx.line_graph(N))
nx.set_edge_attributes(N, edge_centrality, "edge_centrality")
ec = ox.plot.get_edge_colors_by_attr(N, "edge_centrality", cmap="hsv")
fig, ax = ox.plot_graph(N, edge_color=ec, bgcolor="w", edge_linewidth=2, node_size=0)

# or hot
