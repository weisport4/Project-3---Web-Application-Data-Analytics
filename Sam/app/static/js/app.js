function do_work() {
  // Extract user input
  let state = d3.select("#state_dropdown").property("value");

  // Request to the API for all relevant data
  let allDataUrl = `/api/v1.0/allData/${state}`;
  let unemploymentDataUrl = `/api/v1.0/unemploymentData/${state}`;
  let employmentDataUrl = `/api/v1.0/employmentData/${state}`;

  Promise.all([
    d3.json(allDataUrl),
    d3.json(unemploymentDataUrl),
    d3.json(employmentDataUrl)
  ]).then(function (data) {
    let all_data = data[0];
    let unemployment_data = data[1];
    let employment_data = data[2];

    // Check if data is valid
    if (all_data && unemployment_data && employment_data) {
      // Create the graphs
      make_bar_chart(all_data);
      make_sunburst_chart(unemployment_data); // Assuming a function make_sunburst_chart exists
      make_bubble_chart(employment_data);
      make_map(all_data); // Assuming a function make_map exists
    } else {
      console.error("No data found for the selected state.");
    }
  }).catch(function (error) {
    console.error("Error fetching data: ", error);
  });
}

function make_table(filtered_data) {
  // Select table
  let table = d3.select("#data_table");
  let table_body = table.select("tbody");
  table_body.html(""); // Clear existing rows

  // Create table
  filtered_data.forEach(data_row => {
    let row = table_body.append("tr");
    row.append("td").text(data_row.employment_rate);
    row.append("td").text(data_row.unemployment_rate);
    row.append("td").text(data_row.state);
    row.append("td").text(data_row.latitude);
    row.append("td").text(data_row.longitude);
    row.append("td").text(data_row.total_employment); // Adjusted to match data structure
  });
}

function make_bubble_chart(filtered_data) {
  // Extract data for the bubble chart
  let bubble_x = filtered_data.map(d => d.employment_rate);
  let bubble_y = filtered_data.map(d => d.unemployment_rate);
  let bubble_size = filtered_data.map(d => d.total_employment);
  let bubble_text = filtered_data.map(d => d.state);

  // Create the trace for the bubble chart
  let trace1 = {
    x: bubble_x,
    y: bubble_y,
    text: bubble_text,
    mode: 'markers',
    marker: {
      size: bubble_size,
      sizemode: 'area',
      sizeref: 2.0 * Math.max(...bubble_size) / (100**2),
      color: bubble_size,
      colorscale: 'Viridis',
      showscale: true
    }
  };

  // Define the layout for the bubble chart
  let layout = {
    title: 'Employment Rate vs Unemployment Rate',
    xaxis: { title: 'Employment Rate (%)' },
    yaxis: { title: 'Unemployment Rate (%)' },
    showlegend: false,
    height: 600,
    width: 1000
  };

  // Render the plot to the div tag with id "bubble_chart"
  Plotly.newPlot("bubble_chart", [trace1], layout);
}

function make_bar_chart(filtered_data) {
  // Sort values by employment rate
  filtered_data.sort((a, b) => b.employment_rate - a.employment_rate);

  // Extract the x & y values for our bar chart
  let bar_x = filtered_data.map(x => x.state);
  let bar_y = filtered_data.map(x => x.employment_rate);

  // Trace for the bar chart
  let trace1 = {
    x: bar_x,
    y: bar_y,
    type: 'bar',
    marker: {
      color: "skyblue"
    },
    name: "Employment Rate"
  };

  // Create data array
  let data = [trace1];

  // Apply a title to the layout
  let layout = {
    title: "Employment Rate by State",
    xaxis: { title: "State" },
    yaxis: { title: "Employment Rate (%)" },
    margin: {
      l: 50,
      r: 50,
      b: 150,
      t: 50,
      pad: 4
    }
  };

  // Render the plot to the div tag with id "bar_chart"
  Plotly.newPlot("bar_chart", data, layout);
}

function make_sunburst_chart(filtered_data) {
  // Assume filtered_data has hierarchical data with levels like sector, state, and employment count
  let labels = filtered_data.map(d => d.sector + " - " + d.state);
  let parents = filtered_data.map(d => d.sector);
  let values = filtered_data.map(d => d.employment_count);

  // Create trace for sunburst chart
  let trace1 = {
    type: "sunburst",
    labels: labels,
    parents: parents,
    values: values,
    branchvalues: 'total',
    outsidetextfont: { size: 20, color: "#377eb8"},
    leaf: { opacity: 0.6 },
    marker: { line: { width: 2 }},
  };

  // Apply a title to the layout
  let layout = {
    title: "Employment Distribution by Sector and State",
    margin: { l: 10, r: 10, b: 10, t: 40 },
    sunburstcolorway: ["#636efa", "#ef553b", "#00cc96", "#ab63fa", "#19d3f3"],
    extendsunburstcolorway: true,
  };

  // Render the plot to the div tag with id "sunburst_chart"
  Plotly.newPlot("sunburst_chart", [trace1], layout);
}

// Event listener for CLICK on Button
d3.select("#filter").on("click", do_work);

// On page load, don't wait for the click to make the graph, use default
do_work();