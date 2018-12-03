
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://case.cafebonappetit.com/cafe/fribley-marche/")
print(html)


# specify the url
#quote_page = 'https://case.cafebonappetit.com/cafe/fribley-marche/'

# query the website and return the html to the variable ‘page’
#page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(html)


# Take out the <div> of name and get its value
#name_box = soup.find('h1', attrs={'class': 'name'})

#name = name_box.text.strip() # strip() is used to remove starting and trailing
print (soup.title.string)