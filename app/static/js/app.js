function do_work() {
  // extract user input
  let state = d3.select("#state_dropdown").property("value");

  // We need to make a request to the API
  let url = `/api/v1.0/dashboard/${econ_data}`;
  d3.json(url).then(function (data) {

    // create the graphs
    make_bar(all_data);
    make_sunburst(unemployment_data);
    make_bubble(employment_data);
    make_map(all_data);
  });
}

function make_table(filtered_data) {
  // select table
  let table = d3.select("#data_table");
  let table_body = table.select("tbody");
  table_body.html(""); // destroy any existing rows

  // create table
  for (let i = 0; i < filtered_data.length; i++){
    // get data row
    let data_row = filtered_data[i];

    // creates new row in the table
    let row = table_body.append("tr");
    row.append("td").text(data_row.name);
    row.append("td").text(data_row.full_name);
    row.append("td").text(data_row.region);
    row.append("td").text(data_row.latitude);
    row.append("td").text(data_row.longitude);
    row.append("td").text(data_row.launch_attempts);
    row.append("td").text(data_row.launch_successes);
    row.append("td").text(data_row.launch_attempts - data_row.launch_successes);
  }
}

function make_bubble_chart(filtered_data) {
  // Extract the data for the bubble chart
  let bubble_x = filtered_data.map(d => d.employment_rate);
  let bubble_y = filtered_data.map(d => d.unemployment_rate);
  let bubble_size = filtered_data.map(d => d.employment_count);
  let bubble_text = filtered_data.map(d => d.state);
};
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

function make_bar(filtered_data) {
  // sort values
  filtered_data.sort((a, b) => (b.launch_attempts - a.launch_attempts));

  // extract the x & y values for our bar chart
  let bar_x = filtered_data.map(x => x.name);
  let bar_text = filtered_data.map(x => x.full_name);
  let bar_y1 = filtered_data.map(x => x.launch_attempts);
  let bar_y2 = filtered_data.map(x => x.launch_successes);

  // Trace1 for the Launch Attempts
  let trace1 = {
    x: bar_x,
    y: bar_y1,
    type: 'bar',
    marker: {
      color: "skyblue"
    },
    text: bar_text,
    name: "Attempts"
  };

  // Trace 2 for the Launch Successes
  let trace2 = {
    x: bar_x,
    y: bar_y2,
    type: 'bar',
    marker: {
      color: "firebrick"
    },
    text: bar_text,
    name: "Successes"
  };

  // Create data array
  let data = [trace1, trace2];

  // Apply a title to the layout
  let layout = {
    title: "SpaceX Launch Results",
    barmode: "group",
    // Include margins in the layout so the x-tick labels display correctly
    margin: {
      l: 50,
      r: 50,
      b: 200,
      t: 50,
      pad: 4
    }
  };

  // Render the plot to the div tag with id "plot"
  Plotly.newPlot("bar_chart", data, layout);

}

// event listener for CLICK on Button
d3.select("#filter").on("click", do_work);

// on page load, don't wait for the click to make the graph, use default
do_work();
