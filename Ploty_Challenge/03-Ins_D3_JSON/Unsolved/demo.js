const url = "https://api.spacexdata.com/v2/launchpads";

// JavaScript Promise
d3.json(url).then(function(data) {
    console.log(data)
});

const dataPromise = d3.json(url);
console.log("Data Promise:", dataPromise);