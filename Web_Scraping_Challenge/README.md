# Mission to Mars

### Scraping
First we create a jupyter notebook and set up our chrome driver. We set up to scrape the NASA Mars News Site and collect the latest titles and paragraph text. 

Next, we scraped images from the jpl.nasa.gov site and use splinter to navigate the site and find the image url for the "Featured Mars Image." Once we have our image, we are able to visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet and use Pandas to convert the data to an HTML table string

![Alt text](/Web_Scraping_Challenge/table.png?raw=true "Optional Title")

We can then visit the USGS Astrogeology site to obtain high resolution images for each of the Mars hemispheres. Using a Python dictonary to store the data using keys "img_url" and "title." We append the dictionart with the image url string and the hemisphere title to a list and the list contains one dictionary for each hemisphere.

![Alt text](/Web_Scraping_Challenge/images.png?raw=true "Optional Title")

### MongoDB and Flask
After we have scraped and collected the information from the first part, we will create a HTML page that displays all of the information. We start by converting our notebook into a Python script with a function that will execite all of our scraping code from the first part and return one dictionary containing all of the scraped data.

We create a route that will import our script and calls upon on script function. We then created a HTML file that will take our Mars dictionary data and displays all of the data using the correct HTML elements.

![Alt text](/Web_Scraping_Challenge/app.png?raw=true "Optional Title")

