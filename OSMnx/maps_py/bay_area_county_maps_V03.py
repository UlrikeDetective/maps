# using osmnx and matplotlib to plot maps in the San Francisco Bay Area

import osmnx as ox
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties, fontManager

# List of places (cities) you want to visualize
places = [
    "Alameda County, California, USA",
    "Contra Costa County, California, USA",
    "Marin County, California, USA",
    "San Francisco, California, USA",
    "San Mateo County, California, USA",
    "Santa Clara County, California, USA",
    "Solano County, California, USA",
    "Santa Cruz County, California, USA",
    "Monterey County, California, USA",
]

# Define color palette pairs
color_palette_actual = [
    ('#9bafd9', '#103783'),  # LightSteelBlue, NavyBlue
    ('#07f49e', '#42047e'),  # MintGreen, DarkPurple
    ('#45caff', '#ff1b6b'),  # LightBlue, VividPink
    ('#faf0ca', '#0d3b66')   # LightCream, DarkBlue
]

# Extend with additional colors if necessary
additional_colors = [
    ('#95f9c3', '#0b3866'),  # LightGreen, DarkTeal
    ('#613232', '#ffc8c8'),  # DarkBrown, LightPink
    ('#e07a5f', '#f4f1de'),  # TerraCotta, Cream
    ('#6ff7e8', '#1f7ea1'),  # Aquamarine, Teal
    ('#B1624EFF', '#5CC8D7FF'),  # CopperRed, LightCyan
    ('#f8acff', '#696eff'),  # PalePink, Periwinkle
    ('#9bafd9', '#103783'),  # LightSteelBlue, NavyBlue
    ('#00f59b', '#7014f2'),  # ElectricGreen, ElectricPurple
    ('#A2A2A1FF', '#195190FF'),  # LightGray, DeepBlue
    ('#ff0f7b', '#f89b29'),  # DeepPink, Coral
    ('#60efff', '#0061ff'),  # SkyBlue, RoyalBlue
    ('#EA738DFF', '#CBCE91FF')   # DeepPink, PaleOlive
]

# Combine the colors to make 12 pairs
color_palette_actual.extend(additional_colors[:len(places) - len(color_palette_actual)])

# Check available fonts
available_fonts = sorted([f.name for f in fontManager.ttflist])
print("Available fonts: ", available_fonts)

# Set the font properties (use a different font if Nanum Gothic is not available)
font_properties_city = FontProperties(family='Geneva', size=50)  # Font for city name
font_properties_country = FontProperties(family='Geneva', size=20)  # Font for country name

for i, place_name in enumerate(places):
    # Split the place name into city and country
    city, state, country = place_name.split(', ')
    title_text = f"{city}\n{country}"

    # Download the geometries data for the place
    gdf = ox.geocode_to_gdf(place_name)
    
    # Download the street network data for the place
    graph = ox.graph_from_place(place_name, network_type='all')

    # Select a color pair (cycling through the list)
    shape_color, edge_color = color_palette_actual[i % len(color_palette_actual)]

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(10, 10))
    plt.subplots_adjust(top=0.92)  # Adjust to create space at the top

    # Plot the geometries on the axis with the shape color
    ax.set_facecolor('white')
    gdf.plot(ax=ax, facecolor=shape_color, edgecolor=edge_color, linewidth=1.5)
    
    # Plot the street network on the axis with the edge color
    ox.plot_graph(graph, ax=ax, node_size=0, edge_color=edge_color, edge_linewidth=0.5, show=False, close=False)

    # Add the city and country name above the visualization
    fig.suptitle(city, fontsize=30, fontproperties=font_properties_city, color=edge_color, ha='center', y=1.02)
    fig.text(0.5, 0.94, country, fontsize=20, fontproperties=font_properties_country, color=edge_color, ha='center')

    # Save the plot to a file
    filename = f'urban_shapes_{place_name.replace(", ", "_").replace(" ", "_")}_V01.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.show()
