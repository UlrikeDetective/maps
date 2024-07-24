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


# download a street network then solve a shortest-path route on it
weight = "length"
NO = ox.graph_from_place("Nordost, Leipzig, Germany", network_type="drive")
orig = list(NO.nodes)[0]
dest = list(NO.nodes)[-1]
route = ox.shortest_path(NO, orig, dest, weight=weight)
# explore graph edges interactively, with a simple one-liner
ox.graph_to_gdfs(NO, nodes=False).explore()

# download a street network then solve a shortest-path route on it
weight = "length"
O = ox.graph_from_place("Ost, Leipzig, Germany", network_type="drive")
orig = list(O.nodes)[0]
dest = list(O.nodes)[-1]
route = ox.shortest_path(O, orig, dest, weight=weight)
# explore graph edges interactively, with a simple one-liner
ox.graph_to_gdfs(O, nodes=False).explore()

# download a street network then solve a shortest-path route on it
weight = "length"
SO = ox.graph_from_place("Suedost, Leipzig, Germany", network_type="drive")
orig = list(SO.nodes)[0]
dest = list(SO.nodes)[-1]
route = ox.shortest_path(SO, orig, dest, weight=weight)
# explore graph edges interactively, with a simple one-liner
ox.graph_to_gdfs(SO, nodes=False).explore()

# download a street network then solve a shortest-path route on it
weight = "length"
S = ox.graph_from_place("Sued, Leipzig, Germany", network_type="drive")
orig = list(S.nodes)[0]
dest = list(S.nodes)[-1]
route = ox.shortest_path(S, orig, dest, weight=weight)
# explore graph edges interactively, with a simple one-liner
ox.graph_to_gdfs(S, nodes=False).explore()

# download a street network then solve a shortest-path route on it
weight = "length"
SW = ox.graph_from_place("Suedwest, Leipzig, Germany", network_type="drive")
orig = list(SW.nodes)[0]
dest = list(SW.nodes)[-1]
route = ox.shortest_path(SW, orig, dest, weight=weight)
# explore graph edges interactively, with a simple one-liner
ox.graph_to_gdfs(SW, nodes=False).explore()

# download a street network then solve a shortest-path route on it
weight = "length"
W = ox.graph_from_place("West, Leipzig, Germany", network_type="drive")
orig = list(W.nodes)[0]
dest = list(W.nodes)[-1]
route = ox.shortest_path(W, orig, dest, weight=weight)
# explore graph edges interactively, with a simple one-liner
ox.graph_to_gdfs(W, nodes=False).explore()

# download a street network then solve a shortest-path route on it
weight = "length"
AW = ox.graph_from_place("Altwest, Leipzig, Germany", network_type="drive")
orig = list(AW.nodes)[0]
dest = list(AW.nodes)[-1]
route = ox.shortest_path(AW, orig, dest, weight=weight)
# explore graph edges interactively, with a simple one-liner
ox.graph_to_gdfs(AW, nodes=False).explore()

# download a street network then solve a shortest-path route on it
weight = "length"
NW = ox.graph_from_place("Nordwest, Leipzig, Germany", network_type="drive")
orig = list(NW.nodes)[0]
dest = list(NW.nodes)[-1]
route = ox.shortest_path(NW, orig, dest, weight=weight)
# explore graph edges interactively, with a simple one-liner
ox.graph_to_gdfs(NW, nodes=False).explore()

# download a street network then solve a shortest-path route on it
weight = "length"
N = ox.graph_from_place("Nord, Leipzig, Germany", network_type="drive")
orig = list(N.nodes)[0]
dest = list(N.nodes)[-1]
route = ox.shortest_path(N, orig, dest, weight=weight)
# explore graph edges interactively, with a simple one-liner
ox.graph_to_gdfs(N, nodes=False).explore()
