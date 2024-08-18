function loadAndMergeData(callback) {
  let promises = [
    d3.csv('/path/to/employment_cleaned.csv'),
    d3.csv('/path/to/jobs_cleaned.csv'),
    d3.csv('/path/to/statelatlong.csv'),
    d3.csv('/path/to/unemployment_cleaned.csv')
  ];

  Promise.all(promises).then(function(datasets) {
    let employmentData = datasets[0];
    let jobsData = datasets[1];
    let stateLatLongData = datasets[2];
    let unemploymentData = datasets[3];

    // Merge datasets based on the 'state' column
    let mergedData = employmentData.map(empRow => {
      let state = empRow.state;
      let jobRow = jobsData.find(row => row.state === state);
      let latLongRow = stateLatLongData.find(row => row.state === state);
      let unemploymentRow = unemploymentData.find(row => row.state === state);

      return {
        ...empRow,
        jobs_available: jobRow ? jobRow.jobs_available : null,
        latitude: latLongRow ? latLongRow.latitude : null,
        longitude: latLongRow ? latLongRow.longitude : null,
        unemployment_rate: unemploymentRow ? unemploymentRow.unemployment_rate : null
      };
    });

    callback(mergedData);
  }).catch(function(error) {
    console.error("Error loading or merging data: ", error);
  });
}

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
    let latitude = parseFloat(row.latitude);
    let longitude = parseFloat(row.longitude);

    // Ensure latitude and longitude are valid
    if (latitude && longitude) {
      let point = [latitude, longitude];

      // make marker
      let marker = L.marker(point);
      let popup = `
        <h1>${row.state}</h1>
        <hr><h2>Employment Rate: ${row.employment_rate}%</h2>
        <hr><h3>Total Employment: ${row.total_employment}</h3>
        <hr><h4>Unemployment Rate: ${row.unemployment_rate}%</h4>
        <hr><h4>Jobs Available: ${row.jobs_available}</h4>`;
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
    center: [37.0902, -95.7129], // Centering on the USA by default
    zoom: 5,
    layers: [street, markers]
  });

  // Step 5: Add the Layer Control filter + legends as needed
  L.control.layers(baseLayers, overlayLayers).addTo(myMap);
}

function do_work() {
  loadAndMergeData(function(data) {
    if (data) {
      createMap(data);
    } else {
      console.error("No data found.");
    }
  });
}

// Event listener for CLICK on Button
d3.select("#filter").on("click", do_work);

// On page load, don't wait for the click to make the map, use default
do_work();