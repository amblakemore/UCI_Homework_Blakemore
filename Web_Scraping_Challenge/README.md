# Mission to Mars

### Scraping
First we create a jupyter notebook and set up our chrome driver. We set up to scrape the NASA Mars News Site and collect the latest titles and paragraph text. 

Next, we scraped images from the jpl.nasa.gov site and use splinter to navigate the site and find the image url for the "Featured Mars Image." Once we have our image, we are able to visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet and use Pandas to convert the data to an HTML table string

![Alt text](/Web_Scraping_Challenge/table.png?raw=true "Optional Title")

We can then visit the USGS Astrogeology site to obtain high resolution images for each of the Mars hemispheres.

