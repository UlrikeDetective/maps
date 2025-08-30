# Getting Started with QGIS

💡 **New to QGIS?** Download it for free: [QGIS Official Site](https://qgis.org/). QGIS is a powerful, open-source GIS software—completely free!

---

## Step 1: Install QGIS
1. Visit the [QGIS Download Page](https://qgis.org/en/site/forusers/download.html).
2. Choose the version suitable for your operating system (Windows, macOS, Linux).
3. Follow the installation instructions provided on the website.

---

## Step 2: Explore the Interface
Once QGIS is installed, open the application and familiarize yourself with the interface:

- **Menu Bar**: Access tools and settings.
- **Toolbars**: Quick access to frequently used tools.
- **Layers Panel**: Manage your map layers.
- **Map Canvas**: The main area where your map is displayed.
- **Browser Panel**: Quickly access files and data sources.

---

## Step 3: Add Your First Layer
1. **Download Sample Data**:
   - Visit [Natural Earth Downloads](https://www.naturalearthdata.com/downloads/).
   - Download a dataset (e.g., country boundaries).
2. **Add the Layer**:
   - Go to **Layer > Add Layer > Add Vector Layer...**
   - Browse to the downloaded file and click **Add**.

---

## Step 4: Styling Your Map
1. **Open Layer Properties**:
   - Right-click the layer in the **Layers Panel** and select **Properties**.
2. **Adjust Symbology**:
   - Set fill color, border color, and other visual properties.
3. **Apply Effects**:
   - Use the **Draw Effects** option to add shadows, glows, or other effects.

---

## Step 5: Save and Export
1. **Save Your Project**:
   - Go to **Project > Save As...** and choose a location to save your work.
2. **Export Your Map**:
   - Go to **Project > Import/Export > Export Map to Image...**
   - Choose the desired format (e.g., PNG, JPEG).

---

Enjoy exploring the world of GIS with QGIS! 🌍

---

# Changing the Style of an OSM Base Layer

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

| Style Name         | URL                                                       |
|--------------------|-----------------------------------------------------------|
| OSM Standard       | https://tile.openstreetmap.org/{z}/{x}/{y}.png           |
| OSM Humanitarian   | https://tile.openstreetmap.fr/hot/{z}/{x}/{y}.png       |
| Carto Light        | https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png |
| Carto Dark         | https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png  |
| Stamen Toner       | http://tile.stamen.com/toner/{z}/{x}/{y}.png            |
| Stamen Watercolor  | http://tile.stamen.com/watercolor/{z}/{x}/{y}.png       |

Just create a new XYZ tile layer in QGIS for each URL. This effectively “changes the style.”

C) Using Vector Tiles

If you want more flexibility (change road colors, building colors, parks, etc.):

Use Vector Tiles instead of raster XYZ tiles. Examples:

- OpenMapTiles
- MapTiler

Load them in QGIS using Vector Tiles Reader plugin.

You can now:

- Change colors of roads, buildings, water, parks.
- Show/hide layers.
- Customize the style with a QML or Mapbox style JSON.

D) Styling OSM Features Locally

If you have a local .osm.pbf file and imported it into QGIS as vector layers (points, lines, polygons):

Right-click the layer → Properties → Symbology.

You can style features by tags, e.g.:

- leisure=park → green fill
- highway=primary → thick red lines
- building=yes → gray fill

This gives full control over colors, line widths, labels, and transparency.

---

## Summary of Options

| Method                     | Can you change style? | Notes                                           |
|----------------------------|-----------------------|-------------------------------------------------|
| XYZ Tile Raster            | ❌ Limited            | Must use a different tile server for style      |
| Vector Tiles               | ✅ Full               | Change layer colors, visibility, labels         |
| Local OSM Vector Layers    | ✅ Full               | Style by OSM tags with QGIS symbology         |

💡 Tip:
If your goal is visual analysis (e.g., highlighting parks, streets, buildings), I recommend importing OSM as vector layers or using Vector Tiles, because XYZ tiles are “frozen images” — you can’t recolor roads or parks individually.

---

# Example

Perfect! Let’s set up a ready-to-use QGIS workflow for San Francisco using OpenStreetMap data. This workflow will:

- Add a base map layer (OSM).
- Import vector layers (parks, buildings, streets) from OSM.
- Apply a simple, clear style.

## Step 1: Add OSM Base Map

Open QGIS.

In the Browser Panel → XYZ Tiles → New Connection:

Name: OSM Standard

URL: https://tile.openstreetmap.org/{z}/{x}/{y}.png

Click OK and drag the layer into your map canvas.

💡 You can also use alternative styles:

- Humanitarian: https://tile.openstreetmap.fr/hot/{z}/{x}/{y}.png
- Stamen Toner: http://tile.stamen.com/toner/{z}/{x}/{y}.png

## Step 2: Download OSM Data for San Francisco

Go to Geofabrik: California
 → download san-francisco.osm.pbf.

## Step 3: Load OSM Data into QGIS

In QGIS: Vector → OpenStreetMap → Import Topology from XML/PBF → select san-francisco.osm.pbf.

Use Vector → OpenStreetMap → Export Topology to Spatialite to convert it to layers.

Choose layers like points, lines, multilinestrings, multipolygons.

## Step 4: Filter Layers by Feature Type
A) Parks

In your polygon layer, open Layer → Filter… and use:

"leisure" = 'park' OR "landuse" = 'recreation_ground'


This gives all parks in San Francisco.

B) Buildings

Filter polygon layer:

"building" IS NOT NULL

C) Streets

In your lines layer, filter with:

"highway" IS NOT NULL

## Step 5: Apply Styling

Right-click layer → Properties → Symbology.

Example styles:

- Parks: Green fill, 30% transparency
- Buildings: Gray fill, no outline
- Streets: Thin black or colored lines

You can also label streets: Label → Field → name

## Step 6: Optional – Save Styles

Right-click each layer → Styles → Save Style… → .qml file

Reuse on other cities easily.

## Step 7: Zoom to San Francisco

Use Canvas → Zoom to Layer or set CRS to EPSG:4326 (WGS 84).

✅ Result:

- Base map: OSM tiles
- Parks: green polygons
- Buildings: gray polygons
- Streets: black or colored lines