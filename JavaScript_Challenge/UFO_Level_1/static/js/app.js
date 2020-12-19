// from data.js
var tableData = data;

// YOUR CODE HERE!
function ufoTable(data){
    var dataTable = d3.select("tbody");
    // d3.select("#datetime").property("value") = " ";
    dataTable.html(" ");
    data.forEach((rowData)=> {
        var row = dataTable.append("tr");
        Object.values(rowData).forEach((value) => {
            var dataCell = row.append("td");
            dataCell.text (value);
        })
    })
}
ufoTable(tableData);

function filterData(){
    var date = d3.select("#datetime").property("value");
    var filterDate = tableData.filter(rowData => rowData.datetime === date);
    console.log(filterDate);
    ufoTable(filterDate)
}

d3.selectAll("#filter-btn").on("click", filterData)