
from bs4 import BeautifulSoup
from urllib.request import urlopen

from array import array
stringarray = array('i')

html = urlopen("https://case.cafebonappetit.com/cafe/fribley-marche/")
print(html)


# specify the url
#quote_page = 'https://case.cafebonappetit.com/cafe/fribley-marche/'

# query the website and return the html to the variable ‘page’
#page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(html, "html.parser")


# Take out the <div> of name and get its value
#name_box = soup.find('h1', attrs={'class': 'name'})

#name = name_box.text.strip() # strip() is used to remove starting and trailing
print (soup.title.string)
#print (soup.find_all(id='daypart-modal_title--3'))
food_names = soup.findNext('button',attrs={"class":"h4 site-panel__daypart-item-title"})
name = food_names.text.strip()
print (name)

#print(*i, sep='\n')
#print (soup.findAll('h2',attrs={"class":"daypart-modal__title"}))