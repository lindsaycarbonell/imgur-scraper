# Imgur Scraper
In which I try to scrape Steven Universe background photos for my laptop. Because I'm extra.

## Progress
- managed to figure out how to scrape the first viewable images at [this link](http://imgur.com/a/risg9).
- the issue was that the page lazy loads so not all the images are loaded when the page is being scraped
- tried scraping [this](http://imgur.com/a/risg9?grid) summary grid page, but had the same problem.
- found [an example](https://github.com/Rapptz/Reddit-Imgur-Scraper/blob/master/imguralbum.py) but it also has the same problem.

## To do
- Gotta figure out how to scrape this lazy-load page
- https://blog.scrapinghub.com/2016/06/22/scrapy-tips-from-the-pros-june-2016/

## What I've learned so far
- BeautifulSoup
  - `from bs4 import BeautifulSoup`
  - use the requests package to get the page:
    - `response = requests.get(url)`
  - remember to define a parser when creating the soup object
    - `soup = BeautifulSoup(html, "html.parser")`
  - `.find` is for getting a single object. `.find_all` is for multiple objects
  -  `a_tags = soup.find_all('a', attrs={'class': 'zoom'})`
- Regular expressions!
  - use re.compile to create a pattern to search for
  - use re.search to create a match object
  - .start() and .end() on the match will return the first and last indices of the matched string inside the searched string
    - ex:  `str(image)[match.start():match.end()]`
- Python lists
  - list[firstnum:lastnum] will return a range of items in the list


## Links used
- [Pythex](http://pythex.org/) for checking regular expressions in Python
