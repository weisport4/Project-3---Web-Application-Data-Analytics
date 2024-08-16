function createMap(data) {
  // STEP 1: Init the Base Layers

  // Define variables for our tile layers.
  let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  });

  let topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
  });

  // Step 2: Create the Overlay layers
  let markers = L.markerClusterGroup();
  let heatArray = [];

  data.forEach(row => {
    let latitude = row.latitude;
    let longitude = row.longitude;

    // Ensure latitude and longitude are valid
    if (latitude && longitude) {
      let point = [latitude, longitude];

      // make marker
      let marker = L.marker(point);
      let popup = `<h1>${row.state}</h1><hr><h2>Employment Rate: ${row.employment_rate}%</h2><hr><h3>Total Employment: ${row.total_employment}</h3>`;
      marker.bindPopup(popup);
      markers.addLayer(marker);

      // add to heatmap
      heatArray.push(point);
    }
  });

  // create heat layer
  let heatLayer = L.heatLayer(heatArray, {
    radius: 25,
    blur: 20
  });

  // Step 3: BUILD the Layer Controls

  // Only one base layer can be shown at a time.
  let baseLayers = {
    Street: street,
    Topography: topo
  };

  let overlayLayers = {
    Markers: markers,
    Heatmap: heatLayer
  };

  // Step 4: INIT the Map

  // Destroy the old map
  d3.select("#map-container").html("");

  // rebuild the map
  d3.select("#map-container").html("<div id='map'></div>");

  let myMap = L.map("map", {
    center: [40.7128, -74.0059], // Centering on New York by default
    zoom: 5,
    layers: [street, markers]
  });

  // Step 5: Add the Layer Control filter + legends as needed
  L.control.layers(baseLayers, overlayLayers).addTo(myMap);
}

function do_work() {
  // Extract user input
  let state = d3.select("#state_dropdown").property("value");

  // We need to make a request to the API
  let url = `/api/v1.0/allData/${state}`;

  // Fetch the data and create the map
  d3.json(url).then(function (data) {
    if (data) {
      createMap(data);
    } else {
      console.error("No data found for the selected state.");
    }
  }).catch(function (error) {
    console.error("Error fetching data: ", error);
  });
}

// Event listener for CLICK on Button
d3.select("#filter").on("click", do_work);

// On page load, don't wait for the click to make the map, use default
do_work();