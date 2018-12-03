
from bs4 import BeautifulSoup
from urllib.request import urlopen

#fooditems = []

html = urlopen("https://case.cafebonappetit.com/cafe/fribley-marche/")

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(html, "html.parser")


fooditems = soup.find_all('button',class_='h4 site-panel__daypart-item-title')

for x in fooditems:
    print (x.text.strip())



