import multiprocessing as mp

import numpy as np
import osmnx as ox

# you can make query an unambiguous dict to help the geocoder find it
place = {"city": "San Francisco", "state": "California", "country": "USA"}
G = ox.graph_from_place(place, network_type="drive", truncate_by_edge=True)
fig, ax = ox.plot_graph(G, figsize=(10, 10), node_size=0, edge_color="r", bgcolor="white", edge_linewidth=0.2)

# you can make query an unambiguous dict to help the geocoder find it
place = {"city": "Seattle", "state": "Washington", "country": "USA"}
G = ox.graph_from_place(place, network_type="drive", truncate_by_edge=True)
fig, ax = ox.plot_graph(G, figsize=(10, 10), node_size=0, edge_color="r", bgcolor="white", edge_linewidth=0.2)
