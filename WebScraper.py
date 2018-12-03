import json
import re
#import str

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

#Move and format food items to dictionarys
for x in range(len(friblyFoodItems)):
    food = friblyFoodItems[x].text.strip() #formats and removes white space
    food = re.sub('\[.*?\]', '', food) #removes farm information
    food = food.replace("\u00f1", "n") #fixes n character
    friblyDict[x] = food #add item to dictionary

for x in range(len(luitnerFoodItems)):
    food = luitnerFoodItems[x].text.strip() #formats and removes white space
    food = re.sub('\[.*?\]', '', food) #removes farm information
    food = food.replace("\u00f1", "n") #fixes n character
    luitnerDict[x] = food #add item to dictionary

#Dump dictionaries to json files
with open('friblyItems.json', 'w') as fp:
    json.dump(friblyDict, fp, indent=4)

with open('luitnerItems.json', 'w') as fp:
    json.dump(luitnerDict, fp, indent=4)

test = "This pizza is 6\""
#test = test.replace("\"","-in")
print (test)
