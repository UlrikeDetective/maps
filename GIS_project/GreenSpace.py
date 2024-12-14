import geopandas as gpd
import folium
from shapely.ops import unary_union
import pandas as pd
import osmnx as ox


def analyze_green_spaces(city_boundary, population_data):
    """
    Analyze green space distribution and accessibility
    """
    # Load green spaces from OSM
    green_spaces = ox.geometries_from_place(
        city_boundary,
        tags={'leisure': ['park', 'garden'], 'landuse': ['grass', 'forest']}
    )
    
    # Calculate metrics per neighborhood
    results = []
    for idx, neighborhood in population_data.iterrows():
        # Calculate green space area
        neighborhood_green = gpd.clip(green_spaces, neighborhood.geometry)
        green_area = neighborhood_green.area.sum()
        
        # Calculate access (% population within 400m of green space)
        buffer = neighborhood_green.geometry.buffer(400)
        accessible_area = unary_union(buffer)
        accessibility = (
            neighborhood.geometry.intersection(accessible_area).area /
            neighborhood.geometry.area
        ) * 100
        
        results.append({
            'neighborhood': neighborhood['name'],  # Use 'name' or appropriate column
            'green_space_area': green_area,
            'green_space_per_capita': green_area / neighborhood['population'],  # Check column name
            'accessibility_score': accessibility
        })
    
    return pd.DataFrame(results)


def create_green_space_map(analysis_results, city_geometry):
    """
    Create an interactive map of green space analysis
    """
    m = folium.Map(location=city_geometry.centroid.coords[0][::-1], zoom_start=12)
    
    # Add choropleth layer
    folium.Choropleth(
        data=analysis_results,
        columns=['neighborhood', 'green_space_per_capita'],
        key_on='feature.properties.neighborhood',
        fill_color='YlOrRd',
        legend_name='Green Space per Capita (sq m)'
    ).add_to(m)
    
    return m
