function dropdownName(){
    var display = d3.select("#selDataset");
    d3.json("samples.json").then((dataset) => {
        var sampleIDs = dataset.names;
        sampleIDs.forEach((samples) => {
            display.append("option")
            .text(samples)
            .property("value", samples);
        })
        var sample = sampleIDs[0];
        dropdownMetadata(sample);
        createCharts(sample);
    })
}
dropdownName();

function dropdownMetadata(metaSample){
    d3.json("samples.json").then((dataset) => {
        var metaIDs = dataset.metadata;
        console.log(metaIDs);
        var filterMetadata = metaIDs.filter(rowdata => rowdata.id == metaSample);
        var result = filterMetadata[0];
        var displayPanel = d3.select("#sample-metadata");
        displayPanel.html("");
        Object.entries(result).forEach(([key, value]) => {
            displayPanel.append("h6").text(`${key} : ${value}`);
        })
    })
}

function optionChanged(newSampleID){
    dropdownMetadata(newSampleID);
    createCharts(newSampleID);
}

function createCharts(sampleCharts){
    d3.json("samples.json").then((dataset) => {
        var sampleData = dataset.samples;
        var filterSamples = sampleData.filter(rowdata => rowdata.id == sampleCharts);
        var result = filterSamples[0];
        var otuID = result.otu_ids;
        var sampleValues = result.sample_values;
        var otuLables = result.otu_labels;
        var data = [{
            x: sampleValues.slice(0, 10).reverse(),
            y: otuID.slice(0, 10).map(otuID => `otuID ${otuID}`).reverse(),
            text: otuLables.slice(0, 10).reverse(),
            type: "bar",
            orientation: "h"
        }];
        var barLayout = {
            title: "Bacterial Sample"
        }
        Plotly.newPlot("bar", data, barLayout);
        var bubbleData = [{
            x: otuID,
            y: sampleValues,
            text: otuLables,
            mode: "markers",
            marker: {
                size: sampleValues,
                color: otuID,
                colorscale: "Earth"
            }
        }];
        var bubbleLayout = {
            title: "Bacterial Culture per Sample"
        }
        Plotly.newPlot("bubble", bubbleData, bubbleLayout);
})}

