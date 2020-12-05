from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    
    url = "https://mars.nasa.gov/news/"
    
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    article = soup.find("div", class_="list_text")
    news_title = article.find("div", class_="content_title").text
    news_p = article.find("div", class_="article_teaser_body").text

    # Images
    # url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    base_url = 'https://www.jpl.nasa.gov'
    url = base_url + '/spaceimages/?search=&category=Mars'

    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    image_url = soup.find("a", class_= "button fancybox")["data-fancybox-href"]
    featured_image_url = base_url + image_url

    # Facts
    url = 'https://space-facts.com/mars/'
    mars_facts_df = tables[0]
    mars_facts_df.columns = ['Fact', 'Value']
    mars_facts_df['Fact'] = mars_facts_df['Fact'].str.replace(':', '')
    mars_facts_df