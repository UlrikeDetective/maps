import networkx as nx
import osmnx as ox
import partridge as ptg
import shapely.ops as ops
def analyze_transit_coverage(city_boundary, gtfs_path):
 """
 Analyze public transit coverage and service gaps
 """
 # Load GTFS data
 feed = ptg.load_feed(gtfs_path)
 
 # Create transit network
 stops = feed.stops
 stops_gdf = gpd.GeoDataFrame(
 stops,
 geometry=gpd.points_from_xy(stops.stop_lon, stops.stop_lat)
 )
 
 # Calculate service areas (500m walking distance)
 stop_buffers = stops_gdf.geometry.buffer(500)
 service_area = ops.unary_union(stop_buffers)
 
 # Identify areas without coverage
 city_area = gpd.read_file(city_boundary)
 gaps = city_area.geometry.difference(service_area)
 
 # Calculate accessibility metrics
 population_data = gpd.read_file('population_data.geojson')
 
 results = {
 'total_stops': len(stops),
 'coverage_area_percent': (service_area.area / city_area.geometry.area) * 100,
 'population_served': calculate_population_served(
 population_data, 
 service_area
 ),
 'gap_areas': gpd.GeoDataFrame(geometry=[gaps])
 }
 
 return results
def calculate_service_frequency(feed, stop_id):
 """Calculate average service frequency per stop"""
 stop_times = feed.stop_times[feed.stop_times.stop_id == stop_id]
 trips_per_day = len(stop_times.trip_id.unique())
 return trips_per_day