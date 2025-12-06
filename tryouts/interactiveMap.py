import re
import folium
import networkx as nx
import geopandas as gpd
from shapely.geometry import LineString, Point
from pyproj import CRS
import pandas as pd

class PlotGraphMap:
    def __init__(self, excel_file_path):
        print("✅ PlotGraphMap Initialized")
        self.excel_file_path = excel_file_path
        self.CRS_UTM = CRS.from_epsg(32633)  # Change based on your region
        self.CRS_WGS84 = CRS.from_epsg(4326)

    def parse_point(self, x):
        coords = x.replace("POINT (", "").replace(")", "").split()
        return float(coords[0]), float(coords[1])

    def parse_linestring(self, coords_string):
        matches = re.findall(r'(-?\d+\.\d+)\s(-?\d+\.\d+)', coords_string)
        return [(float(lon), float(lat)) for lon, lat in matches]

    def get_graph(self):
        G = nx.Graph()
        routes_df = pd.read_excel(self.excel_file_path, sheet_name='Route')
        houses_df = pd.read_excel(self.excel_file_path, sheet_name='House')
        pits_df = pd.read_excel(self.excel_file_path, sheet_name='Pit-structurePoint')

        houses_df[["house_x", "house_y"]] = houses_df["House_Coordinates"].apply(lambda x: pd.Series(self.parse_point(x)))
        pits_df[["pit_x", "pit_y"]] = pits_df["Pit_geocoordinates"].apply(lambda x: pd.Series(self.parse_point(x)))

        for _, row in houses_df.iterrows():
            G.add_node(row.house_id, geometry=Point(row.house_x, row.house_y), type='house')

        for _, row in pits_df.iterrows():
            G.add_node(row.Pit_Id, geometry=Point(row.pit_x, row.pit_y), type='pit')

        for _, row in routes_df.iterrows():
            if not G.has_node(row.start_structure_id) or not G.has_node(row.end_structure_id):
                continue
            coords = self.parse_linestring(row.geocoordinates)
            if coords:
                line_geometry = LineString(coords)
                G.add_edge(
                    row.start_structure_id,
                    row.end_structure_id,
                    geometry=line_geometry,
                    length=row.get('length_of_the_trench', line_geometry.length),
                    trench_id=row.get('trench_id', 'Unknown')
                )
        return G

    def plot_trench_graph_interactive(self, output_html="trench_graph_map.html"):
        G = self.get_graph()
        if G is None:
            print("⚠️ Graph not initialized.")
            return

        trench_lines = []
        trench_ids = []
        for u, v, data in G.edges(data=True):
            geom = data.get("geometry")
            if isinstance(geom, LineString):
                trench_lines.append(geom)
                trench_ids.append(data.get("trench_id", "Unknown"))

        trench_gdf = gpd.GeoDataFrame({'trench_id': trench_ids, 'geometry': trench_lines}, crs=self.CRS_UTM).to_crs(self.CRS_WGS84)
        map_center = trench_gdf.geometry.unary_union.centroid
        m = folium.Map(location=[map_center.y, map_center.x], zoom_start=16)

        for _, row in trench_gdf.iterrows():
            coords = [(y, x) for (x, y) in row.geometry.coords]
            folium.PolyLine(coords, color="black", weight=3, tooltip=row.trench_id).add_to(m)

        for node, data in G.nodes(data=True):
            geom = data.get("geometry")
            if isinstance(geom, Point):
                gdf = gpd.GeoSeries([geom], crs=self.CRS_UTM).to_crs(self.CRS_WGS84)
                pt = gdf.iloc[0]
                color = "grey" if data["type"] == "pit" else "#ff69b4"
                folium.CircleMarker(
                    location=(pt.y, pt.x),
                    radius=5,
                    color=color,
                    fill=True,
                    fill_color=color,
                    tooltip=f"{node}"
                ).add_to(m)

        m.save(output_html)
        print(f"✅ Interactive map saved to {output_html}")