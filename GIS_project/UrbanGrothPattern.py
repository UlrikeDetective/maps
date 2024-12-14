import rasterio
import geopandas as gpd
from sklearn.cluster import DBSCAN
import numpy as np
from datetime import datetime
def analyze_urban_growth(building_footprints, years_range):
 """
 Analyze urban growth patterns using building construction dates
 """
 # Load and prepare data
 gdf = gpd.read_file(building_footprints)
 
 # Create time periods for analysis
 gdf['period'] = pd.cut(gdf['year_built'], 
 bins=years_range,
 labels=[f'{y}-{y+10}' for y in years_range[:-1]])
 
 # Analyze growth patterns
 results = []
 for period in gdf['period'].unique():
 period_buildings = gdf[gdf['period'] == period]
 
 # Calculate density clusters
 coords = np.vstack(period_buildings.geometry.apply(
 lambda x: [x.centroid.x, x.centroid.y]
 ))
 
 clustering = DBSCAN(eps=0.003, min_samples=5).fit(coords)
 
 # Calculate metrics
 results.append({
 'period': period,
 'new_buildings': len(period_buildings),
 'total_area': period_buildings.geometry.area.sum(),
 'growth_clusters': len(set(clustering.labels_)) - 1, # Exclude noise
 'avg_density': len(period_buildings) / period_buildings.unary_union.area
 })
 
 return pd.DataFrame(results)
def visualize_growth_patterns(analysis_results, city_boundary):
 """Create temporal visualization of urban growth"""
 fig, ax = plt.subplots(figsize=(15, 10))
 
 for idx, period in enumerate(analysis_results['period']):
 period_buildings = gdf[gdf['period'] == period]
 period_buildings.plot(
 ax=ax,
 color=plt.cm.viridis(idx / len(analysis_results)),
 alpha=0.5,
 label=period
 )
 
 plt.legend(title='Construction Period')
 plt.title('Urban Growth Patterns Over Time')
 return fig