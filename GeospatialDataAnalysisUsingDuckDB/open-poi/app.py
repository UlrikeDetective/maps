# Description: A simple Panel app that displays a map with H3 hexagons.
import json
import panel as pn
import duckdb
from panel.custom import JSComponent
import param
from pathlib import Path


db = duckdb.connect(database='data/poi.duckdb', read_only=True)
db.sql("""
    INSTALL spatial;
    INSTALL h3 FROM community;
    LOAD h3;
    LOAD spatial;
""")


def generate_geojson(z: int, bounds: dict = None):
    """
    Generates a GeoJSON FeatureCollection from database query results.
    Args:
        z (int): The zoom level for H3 hexagons.
        bounds (dict, optional): A dictionary containing the bounding box coordinates with keys 'minx', 'maxx', 'miny', and 'maxy'.
    Returns:
        dict: A GeoJSON FeatureCollection containing the H3 hexagons and their associated properties.
    """

    q = f"""
    SELECT h3_h3_to_string(h{z}) as h3, 
        COUNT(*) as count, 
        NTILE(10) OVER (ORDER BY count) as q10,
        ST_AsGeoJSON(ST_GeomFromText(h3_cell_to_boundary_wkt(h{z}))) as geojson
    FROM places
        WHERE bbox.xmin >= {bounds['minx']} AND bbox.xmax <= {bounds['maxx']}
            AND bbox.ymin >= {bounds['miny']} AND bbox.ymax <= {bounds['maxy']} 
            and h{z} is not null
    GROUP BY h{z}
    """

    result = db.sql(q).df().to_dict(orient='records')
    print(len(result))
    # Convert the list of JSON objects to a GeoJSON FeatureCollection
    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": json.loads(row["geojson"]),
                "properties": {
                    "h3": row["h3"],
                    "count": row["count"],
                    "q10": row["q10"]
                }
            }
            for row in result
        ]
    }


class Map(JSComponent):
    data_geo = param.Dict()
    _esm = Path("src/map.js")
    __css__ = [
        "https://cdn.jsdelivr.net/npm/maplibre-gl@4.7.1/dist/maplibre-gl.min.css"]

    def _handle_msg(self, data):
        print(dict(data))
        self.data_geo = generate_geojson(z=data["zoom"], bounds=data["bounds"])


geojson_result = generate_geojson(z=8, bounds={
                                  'minx': 28.417753942870576,
                                  'maxx': 29.539046057128076,
                                  'miny': 40.80035286716085,
                                  'maxy': 41.21539357234562})

m = Map(data_geo=geojson_result, sizing_mode='stretch_both')
pn.Column(m, sizing_mode='stretch_both').servable()
