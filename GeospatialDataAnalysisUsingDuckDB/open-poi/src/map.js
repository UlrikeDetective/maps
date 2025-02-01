import maplibregl from 'https://cdn.jsdelivr.net/npm/maplibre-gl@4.7.1/+esm';

export function render({ model, el }) {
  const map = new maplibregl.Map({
    container: el, // container id
    style: "https://tiles.openfreemap.org/styles/positron", // style URL
    center: [28.9784, 41.0082], // starting position [lng, lat] (Istanbul)
    zoom: 10, 
  });

  map.addControl(
    new maplibregl.NavigationControl({
      visualizePitch: true,
      visualizeRoll: true,
      showZoom: true,
      showCompass: true,
    }),
    "top-left"
  );

  map.addControl(new maplibregl.FullscreenControl(), "top-left");
  model.on("after_render", () => {
    console.log(model.data_geo);
    map.on("load", () => {
      map.addSource("geojson", {
        type: "geojson",
        data: model.data_geo,
      });

      map.addLayer({
        id: "geojson",
        type: "fill-extrusion",
        source: "geojson",
        paint: {
          'fill-extrusion-color': [
            'interpolate',
            ['linear'],
            ['get', 'q10'],
            1, '#ffffb2', 
            5, '#fd8d3c', 
            10, '#bd0026' 
          ],
          'fill-extrusion-height': [
            'interpolate',
            ['linear'],
            ['get', 'q10'],
            1, 100, 
            10, 1000 
          ],
          'fill-extrusion-opacity': 0.8 
        },
      });
    });
    map.on("click", "geojson", (e) => {
      new maplibregl.Popup()
        .setLngLat(e.lngLat)
        .setHTML(e.features[0].properties.q10)
        .addTo(map);
    });

    model.on("change:data_geo", () => {
      const source = map.getSource("geojson");
      if (source) {
        source.setData(model.data_geo);
      }
    });
  });

  function handleMoveChange() {
    const currentZoom = Math.floor(map.getZoom()); 
    console.log("Zoom Level: ", currentZoom);
    const bounds = map.getBounds();
    const boundsJson = {
      minx: bounds.getWest(), 
      maxx: bounds.getEast(), 
      miny: bounds.getSouth(), 
      maxy: bounds.getNorth(), 
    };

    if (currentZoom >= 12) {
      model.send_msg({ zoom: 10, bounds: boundsJson });
    } else if (currentZoom >= 5 && currentZoom < 12) {
      model.send_msg({ zoom: 6, bounds: boundsJson });
    }
  }

  map.on("moveend", () => {
    handleMoveChange();
  });
}
