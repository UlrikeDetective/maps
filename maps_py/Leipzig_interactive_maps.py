import networkx as nx
import osmnx as ox

# download a street network then solve a shortest-path route on it
weight = "length"
M = ox.graph_from_place("Mitte, Leipzig, Germany", network_type="drive")
orig = list(M.nodes)[0]
dest = list(M.nodes)[-1]
route = ox.shortest_path(M, orig, dest, weight=weight)

# explore graph edges interactively, with a simple one-liner
ox.graph_to_gdfs(M, nodes=False).explore()
