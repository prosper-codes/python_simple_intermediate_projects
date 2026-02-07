import  requests
import selectorlib


URl = ""

def scrape(url):
    """ Scrape the page source from URl"""
    response = requests.get(url)
    source = response.text
    return source


if __name__ =="__main__":
    scrape(URl)