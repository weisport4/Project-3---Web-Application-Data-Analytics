// Main function to handle everything
function do_work() {
  // Extract user input
  let selectedYear = d3.select("#year_filter").property("value");
  let selectedState = d3.select("#state_filter").property("value");

  // Query the SQL database for each dataset
  Promise.all([
    queryDatabase(`SELECT * FROM employment WHERE year = ${selectedYear} AND state = '${selectedState}'`),
    queryDatabase(`SELECT * FROM unemployment WHERE year = ${selectedYear} AND state = '${selectedState}'`),
    queryDatabase(`SELECT * FROM jobs WHERE year = ${selectedYear} AND state = '${selectedState}'`),
    queryDatabase(`SELECT * FROM income WHERE year = ${selectedYear} AND state = '${selectedState}'`)
  ]).then(function (data) {
    let employmentData = data[0];
    let unemploymentData = data[1];
    let jobsData = data[2];
    let incomeData = data[3];

    // Create the graphs
    make_bar(jobsData);
    make_pie(incomeData);
    make_table(employmentData);
    make_sunburst(unemploymentData);
  });
}

// Function to query the SQL database
function queryDatabase(query) {
  return new Promise((resolve, reject) => {
    d3.json('/path_to_your_server_endpoint', {
      method: "POST",
      body: JSON.stringify({ sql: query }),
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(data => resolve(data))
    .catch(error => reject(error));
  });
}

// Function to create a table for employment data
function make_table(filtered_data) {
  // Select table
  let table = d3.select("#data_table");
  let table_body = table.select("tbody");
  table_body.html(""); // Destroy any existing rows

  // Create table
  filtered_data.forEach(data_row => {
    let row = table_body.append("tr");
    row.append("td").text(data_row.year);
    row.append("td").text(data_row.state);
    row.append("td").text(data_row.employment_rate);
    row.append("td").text(data_row.employment_count);
  });

  // Initialize DataTables after the table is populated
  $('#data_table').DataTable();
}

// Other functions for creating graphs (make_pie, make_bar, make_sunburst) remain the same

// Event listener for CLICK on Button
d3.select("#filter").on("click", do_work);

// On page load, don't wait for the click to make the graph, use default
do_work();