import osmnx as ox
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties, fontManager

# List of places (cities) you want to visualize
places = [
    "Usedom, Germany",
    "Rügen, Germany",
    "Sylt, Germany",
    "Borkum, Germany",
    "Mallorca, Spain",
    "Ibiza, Spain",
    "Formentera, Spain",
    "La Gomera, Spain",
    "Fuerteventura, Spain",
    "Ilha Terceira, Portugal",
    "Ilha do Pico, Portugal",
    "Ilha do Faial, Portugal",
    "Ilha de Sao Miguel, Portugal",
    "Madeira, Portugal",
    "Sicily, Italy",
    "Sardegna, Italy",
    "Isola di Lipari, Lipari, Italy",
    "Isola di Vulcano, Lipari, Italy",
    "Isola di Panarea, Italy",
    "Stromboli, Italy",
    "Corfu, Greece",
    "Santorini, Greece",
    "Naxos, Greece",
    "Mikonos, Greece",
    "Rathlin Island, United Kingdom",
    "Inishmore, Ireland",
    "Mainland, Orkney, United Kingdom",
    "North Ronaldsay, United Kingdom",
    "Papa Westray, United Kingdom",
    "Small Isles, Scotland, United Kingdom",
    "Staffa, Scotland, United Kingdom",
    "Iona, Scotland, United Kingdom",
    "Isle of Portland, England, United Kingdom",
]

# Define color palette pairs
color_palette_actual = [
    ('#f4f1de', '#e07a5f'),  # Cream and TerraCotta
    ('#ff0f7b', '#f89b29'),  # DeepPink and Coral
    ('#60efff', '#0061ff')   # SkyBlue and RoyalBlue
]

# Extend with additional colors if necessary
additional_colors = [
    ('#45caff', '#ff1b6b'),  # LightBlue and VividPink
    ('#07f49e', '#42047e'),  # MintGreen and DarkPurple
    ('#9bafd9', '#103783'),  # LightSteelBlue and NavyBlue
    ('#95f9c3', '#0b3866'),  # LightGreen and DarkTeal
    ('#613232', '#ffc8c8'),  # DarkBrown and LightPink
    ('#f8acff', '#696eff'),  # PalePink and Periwinkle
    ('#6ff7e8', '#1f7ea1'),  # Aquamarine and Teal
    ('#00f59b', '#7014f2'),  # ElectricGreen and ElectricPurple
    ('#faf0ca', '#0d3b66'),  # LightCream and DarkBlue
    ('#B1624E', '#5CC8D7'),  # CopperRed and LightCyan
    ('#A2A2A1', '#195190'),  # LightGray and DeepBlue
    ('#EA738D', '#CBCE91'),  # DeepPink and PaleOlive
    ('#87CEEB', '#4682B4'),  # SkyBlue and SteelBlue
    ('#000080', '#FFA500'),  # Navy and Orange
    ('#32CD32', '#006400'),  # LimeGreen and DarkGreen
    ('#FF69B4', '#8B008B'),  # HotPink and DarkMagenta
    ('#8A2BE2', '#FFD700'),  # BlueViolet and Gold
    ('#D8BFD8', '#4B0082'),  # Thistle and Indigo
    ('#40E0D0', '#00008B'),  # Turquoise and DarkBlue
    ('#FF6347', '#008080'),  # Tomato and Teal
    ('#7B68EE', '#FFD700'),  # MediumSlateBlue and Gold
    ('#8B0000', '#FFA07A'),  # DarkRed and LightSalmon
    ('#FFC0CB', '#800080'),  # Pink and Purple
    ('#00CED1', '#DC143C'),  # DarkTurquoise and Crimson
    ('#FFDAB9', '#8B4513'),  # PeachPuff and SaddleBrown
    ('#7FFF00', '#8B0000'),  # Chartreuse and DarkRed
    ('#ADFF2F', '#FF8C00'),  # GreenYellow and DarkOrange
    ('#FFDEAD', '#8B0000'),  # NavajoWhite and DarkRed
    ('#BC8F8F', '#FFD700'),  # RosyBrown and MediumSlateBlue
    ('#FFD700', '#00008B'),  # Gold and DarkBlue
    ('#2F4F4F', '#FFD700')   # DarkSlateGray and Gold
]

# Combine the colors to make 12 pairs
color_palette_actual.extend(additional_colors[:len(places) - len(color_palette_actual)])

# Check available fonts
available_fonts = sorted([f.name for f in fontManager.ttflist])
print("Available fonts: ", available_fonts)

# Set the font properties (use a different font if Nanum Gothic is not available)
font_properties_city = FontProperties(family='Geneva', size=80)  # Font for city name
font_properties_country = FontProperties(family='Geneva', size=20)  # Font for country name

for i, place_name in enumerate(places):
    try:
        # Split the place name into components
        parts = place_name.split(', ')
        if len(parts) == 3:
            city, state, country = parts
        elif len(parts) == 2:
            city, country = parts
            state = ""
        else:
            raise ValueError(f"Invalid place format: {place_name}")

        title_text = f"{city}\n{country}"

        # Use the `geometries_from_place` function to get the geometries of the island
        tags = {'place': ['island', 'islet']}
        gdf = ox.geometries_from_place(place_name, tags=tags)

        # Download the street network data for the place
        graph = ox.graph_from_place(place_name, network_type='all')

        # Select a color pair (cycling through the list)
        background_color, edge_color = color_palette_actual[i % len(color_palette_actual)]

        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(10, 10))
        plt.subplots_adjust(top=0.92)  # Adjust to create space at the top

        # Plot the geometries on the axis with the background color
        ax.set_facecolor(background_color)
        gdf.plot(ax=ax, facecolor=edge_color, edgecolor='k', linewidth=0.5)

        # Plot the street network on the same axis
        ox.plot_graph(graph, ax=ax, node_size=0, edge_color='black', edge_linewidth=0.8, show=False, close=False)

        # Add the city and country name above the visualization
        fig.suptitle(city, fontsize=50, fontproperties=font_properties_city, color=edge_color, ha='center', y=1.02)
        fig.text(0.5, 0.93, country, fontsize=20, fontproperties=font_properties_country, color=edge_color, ha='center')

        # Save the plot to a file
        filename = f'europeanIsland_shapes_{place_name.replace(", ", "_").replace(" ", "_")}_V04.png'
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.show()

    except Exception as e:
        print(f"Error processing {place_name}: {e}")

