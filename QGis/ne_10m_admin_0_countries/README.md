* How to make a firefly map with QGIS
💡 If you haven’t used QGIS before, run — don’t walk! You can download it for free here! QGIS is a community-built, open source GIS software which is totally free!

Step 1: set the scene
The foundation of a great firefly map is a beautiful, dark basemap. Otherwise, you can find a wide range of pre-built basemaps by:

Open QGIS and head to the Plugins drop-down menu (top of the screen) and open Manage and Install Plugins.
Search for QuickMapServices and install this plugin.
Leave the plugin menu, and open the Web drop-down menu.
Via QuickMapServices, go through Settings > More Settings > and enable Get contributed pack.
If you head back to this menu, you’ll now see there’s a host of webmaps available for you to use, including a number of really nice dark options. Some of these require licenses so be mindful of that when using them.
You can also adapt any basemap’s coloration, brightness and contrast in the layer’s symbology (although again, be mindful of the license terms).

If you have the time — and patience — you can build you own! I’m just going to use country boundaries from Natural Earth to keep things nice and simple (see below).

Option 1: Download Natural Earth data manually
Go to the official Natural Earth website:
https://www.naturalearthdata.com/downloads/

Choose a dataset:

For country boundaries:
Go to Cultural > Admin 0 – Countries
(direct link)

Download the Shapefile (SHP) version — usually available in 1:110m, 1:50m, and 1:10m scales:

Smaller scale = less detail = faster to render.

Start with 1:110m to keep it simple and fast.

Unzip the downloaded folder.

In QGIS:

Go to Layer > Add Layer > Add Vector Layer...

Browse to the .shp file you unzipped (e.g. ne_110m_admin_0_countries.shp) and add it.

✅ Option 2: Use Natural Earth from QGIS’s built-in data sources
If you prefer not to download manually:

Open Browser Panel in QGIS (View > Panels > Browser).

Scroll down to XYZ Tiles or Open Data Sources.

Alternatively, use the QuickMapServices plugin (already installed from your guide), but this usually gives raster basemaps, not vector layers like country boundaries.

🔧 Pro Tip: Styling for Firefly Maps
Once you have the country borders loaded:

Right-click the layer > Properties > Symbology.

Set fill color to transparent.

Set border color to a bright, glowing color (e.g. neon green #39FF14, cyan, or yellow).

Use “Draw Effects” to add an outer glow for that firefly effect.

Step 2: your firefly layer
Next, add the layer to your map that you want to “glow!” I’m using UK pub locations from OpenStreetMap because… I don’t have to justify myself. (© OpenStreetMap contributors)

So this is what we’re dealing with… there are so many pubs (what a great problem to have) that it’s difficult to make out any spatial patterns. Let’s firefly this up!


Option 1: Use the QuickOSM Plugin (Best Option)
1. Install the QuickOSM Plugin:
Go to Plugins > Manage and Install Plugins…

Search for QuickOSM and click Install Plugin

2. Download UK Pubs Data:
Go to Vector > QuickOSM > QuickOSM

In the dialog:

Key: amenity

Value: pub

In: Select United Kingdom (or a specific region if you like)

Click Run Query

This will download all features tagged as amenity=pub in the selected area from OpenStreetMap.

3. Save the Layer (optional):
Once it appears on the map, you can right-click the new layer > Export > Save Features As... to save it as a shapefile or GeoPackage for later use.

✅ Option 2: Use Geofabrik Downloads (Manual Way)
If you want a large dataset and prefer working offline:

1. Go to Geofabrik Downloads
Navigate to Europe > Great Britain

2. Download the .osm.pbf file
3. Use a tool like osmconvert or osmfilter to extract pubs, or open it in QGIS using:
Vector > OpenStreetMap > Import Topology from XML

(Then use OSM Feature to filter and extract amenity=pub)

✅ Option 3: Use Overpass Turbo (for smaller datasets)
If you only want pub data for a smaller region like London or Manchester:

1. Go to Overpass Turbo
2. Paste this query:
overpassql
Copy
Edit
[out:json][timeout:25];
area["name"="United Kingdom"]->.searchArea;
node["amenity"="pub"](area.searchArea);
out body;
>;
out skel qt;
3. Click Run, then Export > GeoJSON or QGIS
Then open that file in QGIS.
