1️⃣ Changing the Style of an OSM Base Layer

There are a few ways to have an OSM layer in QGIS:

A) Using XYZ Tiles (common for OSM base maps)

In Browser Panel → XYZ Tiles → New Connection:

Name: OSM Standard

URL: https://tile.openstreetmap.org/{z}/{x}/{y}.png

Add the layer to your project.

Right-click → Properties → Symbology:

For XYZ raster tiles, you cannot change the style directly in QGIS because it’s just an image from the OSM server.

To change appearance, you must use a different tile server that provides an alternative style.

B) Alternative OSM Tile Styles (XYZ Tiles)

You can swap the URL to get different pre-made styles. Examples:

Style Name	URL
OSM Standard	https://tile.openstreetmap.org/{z}/{x}/{y}.png
OSM Humanitarian	https://tile.openstreetmap.fr/hot/{z}/{x}/{y}.png
Carto Light	https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png
Carto Dark	https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png
Stamen Toner	http://tile.stamen.com/toner/{z}/{x}/{y}.png
Stamen Watercolor	http://tile.stamen.com/watercolor/{z}/{x}/{y}.png

Just create a new XYZ tile layer in QGIS for each URL. This effectively “changes the style.”

C) Using Vector Tiles

If you want more flexibility (change road colors, building colors, parks, etc.):

Use Vector Tiles instead of raster XYZ tiles. Examples:

OpenMapTiles

MapTiler

Load them in QGIS using Vector Tiles Reader plugin.

You can now:

Change colors of roads, buildings, water, parks.

Show/hide layers.

Customize the style with a QML or Mapbox style JSON.

D) Styling OSM Features Locally

If you have a local .osm.pbf file and imported it into QGIS as vector layers (points, lines, polygons):

Right-click the layer → Properties → Symbology.

You can style features by tags, e.g.:

leisure=park → green fill

highway=primary → thick red lines

building=yes → gray fill

This gives full control over colors, line widths, labels, and transparency.

2️⃣ Summary of Options
Method	Can you change style?	Notes
XYZ Tile Raster	❌ Limited	Must use a different tile server for style
Vector Tiles	✅ Full	Change layer colors, visibility, labels
Local OSM Vector Layers	✅ Full	Style by OSM tags with QGIS symbology

💡 Tip:
If your goal is visual analysis (e.g., highlighting parks, streets, buildings), I recommend importing OSM as vector layers or using Vector Tiles, because XYZ tiles are “frozen images” — you can’t recolor roads or parks individually.