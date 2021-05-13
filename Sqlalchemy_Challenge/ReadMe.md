# Surfs Up!

### Climate Analysis and Exploration
We connect our sqlite database and then organize them into classes for "Stations" and "Measurements." Using the data, we design a query to retrieve that last year's worth of preciptiation data

![Alt text](/Sqalchemy_Challenge/precipitation.png?raw=true "Optional Title")

We can also design a query to find the most activate stations (highest number of observations) and retrived the last 12 months of temperature obersation data (TOBS)

### Climate App
Using the queries that were developed in the first portion, we then use flask to create routes where were can convert the query results to a dictonary for the values that were extracted.

![Alt text](/Sqlalchemy_Challenge/app.png?raw=true "Optional Title")

