import osmnx as ox
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point, box
import matplotlib.pyplot as plt  # Ensure matplotlib is imported for plotting

def calculate_walkability_score(location, radius=1000):
    """
    Calculate walkability score for a location based on:
    - Number of amenities within walking distance
    - Street network density
    - Intersection density
    """
    # Download street network and amenities
    G = ox.graph_from_point(location, dist=radius, network_type='walk')
    
    # Get amenities from OSM
    amenities = ox.geometries_from_point(
        location, 
        tags={'amenity': True},
        dist=radius
    )
    
    # Calculate metrics
    area = radius * radius * 3.14159 / 1000000  # km²
    
    # Street density (km/km²)
    edge_lengths = ox.utils_graph.get_route_edge_attributes(G, 'length')
    street_density = sum(edge_lengths) / 1000 / area
    
    # Intersection density
    nodes, edges = ox.graph_to_gdfs(G)
    intersection_density = len(nodes[nodes.street_count > 1]) / area
    
    # Amenity score
    amenity_score = len(amenities) / area
    
    # Calculate final score (weighted average)
    walkability_score = (
        0.4 * normalize(street_density) +
        0.4 * normalize(intersection_density) +
        0.2 * normalize(amenity_score)
    )
    
    # Plot the street network
    fig, ax = ox.plot_graph(G, show=False, close=False)
    if not amenities.empty:
        amenities.plot(ax=ax, color='red', markersize=10, alpha=0.7, label='Amenities')
    ax.legend()
    plt.show()
    
    return walkability_score, {
        'street_density': street_density,
        'intersection_density': intersection_density,
        'amenities_per_sqkm': amenity_score
    }

def normalize(value, min_val=0, max_val=100):
    """Normalize value to 0–100 scale"""
    return min(100, max(0, (value - min_val) / (max_val - min_val) * 100))

def main():
    # Prompt the user to choose input method
    choice = input("Enter 1 for coordinates, 2 for address: ")
    if choice == "1":
        latitude = float(input("Enter latitude: "))
        longitude = float(input("Enter longitude: "))
        location = (latitude, longitude)
    elif choice == "2":
        address = input("Enter an address: ")
        location = ox.geocode(address)
    else:
        print("Invalid choice. Exiting.")
        return

    # Calculate walkability score
    score, metrics = calculate_walkability_score(location)
    print(f"Walkability Score: {score}")
    print(metrics)

if __name__ == "__main__":
    main()
