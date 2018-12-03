import json
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Set link for dining halls
friblyUrl = urlopen("https://case.cafebonappetit.com/cafe/fribley-marche/")
luitnerUrl = urlopen("https://case.cafebonappetit.com/cafe/leutner-cafe/")

# parse the html using beautiful soup and store in variable
friblySoup = BeautifulSoup(friblyUrl, "html.parser")
luitnerSoup = BeautifulSoup(luitnerUrl, "html.parser")

#Parse through page for food items
friblyFoodItems = friblySoup.find_all('button',class_='h4 site-panel__daypart-item-title')
luitnerFoodItems = luitnerSoup.find_all('button',class_='h4 site-panel__daypart-item-title')

#Create Dictionarys to store formated food items
friblyDict = {}
luitnerDict = {}

#Move food items to dictionarys
for x in range(len(friblyFoodItems)):
    friblyDict[x]=friblyFoodItems[x].text.strip()

for x in range(len(luitnerFoodItems)):
    luitnerDict[x]=luitnerFoodItems[x].text.strip()

#Dump dictionaries to json files
with open('friblyItems.json', 'w') as fp:
    json.dump(friblyDict, fp, indent=4)

with open('luitnerItems.json', 'w') as fp:
    json.dump(luitnerDict, fp, indent=4)




