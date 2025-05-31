# How to Make a Firefly Map with QGIS

💡 **New to QGIS?** Download it for free: [QGIS Official Site](https://qgis.org/). QGIS is a powerful, open-source GIS software—completely free!

---

## Step 1: Set the Scene

A great firefly map starts with a beautiful, dark basemap.

### Option 1: Use QuickMapServices Plugin
1. **Open QGIS**
2. Go to **Plugins > Manage and Install Plugins**
3. Search for **QuickMapServices** and install it
4. Go to **Web > QuickMapServices > Settings > More Settings**
5. Enable **Get contributed pack**
6. Return to **Web > QuickMapServices** to access a wide range of webmaps (including dark basemaps)
   - *Note: Some maps require licenses—check before use!*
7. You can also adjust any basemap’s color, brightness, and contrast in the layer’s symbology

### Option 2: Download Natural Earth Data Manually
1. Visit [Natural Earth Downloads](https://www.naturalearthdata.com/downloads/)
2. For country boundaries: **Cultural > Admin 0 – Countries**
3. Download the **Shapefile (SHP)** version (choose 1:110m for simplicity)
4. Unzip the folder
5. In QGIS: **Layer > Add Layer > Add Vector Layer...**
6. Browse to the `.shp` file and add it

### Option 3: Use QGIS Built-in Data Sources
- Open **Browser Panel** (View > Panels > Browser)
- Scroll to **XYZ Tiles** or **Open Data Sources**
- Or use QuickMapServices for raster basemaps

---

## 🔧 Pro Tip: Styling for Firefly Maps
- **Right-click layer > Properties > Symbology**
- Set **fill color** to transparent
- Set **border color** to a bright, glowing color (e.g. neon green `#39FF14`, cyan, yellow)
- Use **Draw Effects** to add an outer glow for the firefly effect

---

## Step 2: Add Your Firefly Layer

Let’s add the layer you want to “glow.” Example: UK pub locations from OpenStreetMap.

### Option 1: Use the QuickOSM Plugin *(Recommended)*
1. **Install QuickOSM Plugin**
   - Plugins > Manage and Install Plugins…
   - Search for **QuickOSM** and install
2. **Download UK Pubs Data**
   - Vector > QuickOSM > QuickOSM
   - Set **Key:** `amenity`, **Value:** `pub`, **In:** United Kingdom
   - Click **Run Query**
3. **Save the Layer (Optional)**
   - Right-click the new layer > Export > Save Features As... (e.g. Shapefile or GeoPackage)

### Option 2: Use Geofabrik Downloads (Manual)
1. Go to [Geofabrik Downloads](https://download.geofabrik.de/)
   - Navigate to Europe > Great Britain
2. Download the `.osm.pbf` file
3. Use a tool like `osmconvert` or `osmfilter` to extract pubs, or open in QGIS:
   - Vector > OpenStreetMap > Import Topology from XML
   - Use OSM Feature to filter for `amenity=pub`

### Option 3: Use Overpass Turbo (For Small Regions)
1. Go to [Overpass Turbo](https://overpass-turbo.eu/)
2. Paste this query:
   ```overpassql
   [out:json][timeout:25];
   area["name"="United Kingdom"]->.searchArea;
   node["amenity"="pub"](area.searchArea);
   out body;
   >;
   out skel qt;
   ```
3. Click **Run**, then **Export > GeoJSON** or **QGIS**
4. Open the exported file in QGIS

---

Enjoy making your firefly map! ✨
