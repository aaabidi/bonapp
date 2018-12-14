import json
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

#Create Dictionarys for meals
friblyMeals = {}
friblyMealNames = {}
luitnerMeals = {}
luitnerMealNames = {}

# Set links for dining halls
friblyUrl = urlopen("https://case.cafebonappetit.com/cafe/fribley-marche/")
#friblyUrl = urlopen("https://case.cafebonappetit.com/cafe/fribley-marche/2018-12-02/") #sunday website
luitnerUrl = urlopen("https://case.cafebonappetit.com/cafe/leutner-cafe/")

#Create Soups
friblySoup = BeautifulSoup(friblyUrl, "html.parser")
luitnerSoup = BeautifulSoup(luitnerUrl, "html.parser")

#Get Breakfast
friblyBreakfast = friblySoup.find('section', id='breakfast') #Finds just breakfast section
if friblyBreakfast is None: #Checks if breakfast is served
    print ("No Breakfast")
else:
    friblyBreakfast = friblyBreakfast.find('div', tabindex='0') #Selects just the first 'specials' tab
    friblyBreakfastFood = friblyBreakfast.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
    friblyMeals[1] = friblyBreakfastFood #Adds breakfast to list of meals
    friblyMealNames[1] = "Breakfast" #Adds breakfast to list of meal names

luitnerBreakfast = luitnerSoup.find('section', id='breakfast') #Finds just breakfast section
if luitnerBreakfast is None: #Checks if breakfast is served
    print ("No Breakfast")
else:
    luitnerBreakfast = luitnerBreakfast.find('div', tabindex='0') #Selects just the first 'specials' tab
    luitnerBreakfastFood = luitnerBreakfast.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
    luitnerMeals[1] = luitnerBreakfastFood #Adds breakfast to list of meals
    luitnerMealNames[1] = "Breakfast" #Adds breakfast to list of meal names

#Get Brunch
friblyBrunch = friblySoup.find('section', id='brunch') #Finds just brunch section
if friblyBrunch is None: #Checks if brunch is served
    print ("No Brunch")
else:
    friblyBrunch = friblyBrunch.find('div', tabindex='0') #Selects just the first 'specials' tab
    friblyBrunchFood = friblyBrunch.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
    friblyMeals[1] = friblyBrunchFood  #Adds Brunch to list of meals
    friblyMealNames[1] = "Brunch" #Adds brunch to list of meal names

luitnerBrunch = luitnerSoup.find('section', id='brunch') #Finds just brunch section
if luitnerBrunch is None: #Checks if brunch is served
    print ("No Brunch")
else:
    luitnerBrunch = luitnerBrunch.find('div', tabindex='0') #Selects just the first 'specials' tab
    luitnerBrunchFood = luitnerBrunch.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
    luitnerMeals[1] = luitnerBrunchFood  #Adds Brunch to list of meals
    luitnerMealNames[1] = "Brunch" #Adds brunch to list of meal names

#Get Lunch
friblyLunch = friblySoup.find('section', id='lunch') #Finds just lunch section
if friblyLunch is None: #Checks if Lunch is served
    print ("No Lunch")
else:
    friblyLunch = friblyLunch.find('div', tabindex='0') #Selects just the first 'specials' tab
    friblyLunchFood = friblyLunch.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
    friblyMeals[2] = friblyLunchFood  #Adds Lunch to list of meals
    friblyMealNames[2] = "Lunch" #Adds Lunch to list of meal names

luitnerLunch = luitnerSoup.find('section', id='lunch') #Finds just lunch section
if luitnerLunch is None: #Checks if Lunch is served
    print ("No Lunch")
else:
    luitnerLunch = luitnerLunch.find('div', tabindex='0') #Selects just the first 'specials' tab
    luitnerLunchFood = luitnerLunch.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
    luitnerMeals[2] = luitnerLunchFood  #Adds Lunch to list of meals
    luitnerMealNames[2] = "Lunch" #Adds Lunch to list of meal names

#Get Dinner
friblyDinner = friblySoup.find('section', id='dinner') #Finds just dinner section
friblyDinner = friblyDinner.find('div', tabindex='0') #Selects just the first 'specials' tab
friblyDinnerFood = friblyDinner.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
if len(friblyMeals) == 2:  #Adds Dinner to list of meals, but also checks to see if there was brunch or not
    friblyMeals[3] = friblyDinnerFood
    friblyMealNames[3] = "Dinner" 
else:
    friblyMeals[2] = friblyDinnerFood
    friblyMealNames[2] = "Dinner" 

luitnerDinner = luitnerSoup.find('section', id='dinner') #Finds just dinner section
luitnerDinner = luitnerDinner.find('div', tabindex='0') #Selects just the first 'specials' tab
luitnerDinnerFood = luitnerDinner.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
if len(luitnerMeals) == 2:  #Adds Dinner to list of meals, but also checks to see if there was brunch or not
    luitnerMeals[3] = luitnerDinnerFood
    luitnerMealNames[3] = "Dinner" 
else:
    luitnerMeals[2] = luitnerDinnerFood
    luitnerMealNames[2] = "Dinner" 

#Create A Json file for all of the meals at fribly 
for mealIndex, meal in friblyMeals.items():

    #Create Dictionary of foods
    friblyDict = {}

    #Move and format food items to dictionarys
    for x in range(len(meal)):
        food = meal[x].text.strip() #formats and removes white space
        food = re.sub('\[.*?\]', '', food) #removes farm information
        food = food.replace("\u00f1", "n") #fixes Nne character
        friblyDict[x] = food #add item to dictionary

    #Dump dictionaries to json files
    with open('fribly'+friblyMealNames[mealIndex]+'.json', 'w') as fp:
        json.dump(friblyDict, fp, indent=4)
    
#Create A Json file for all of the meals at luitner 
for mealIndex, meal in luitnerMeals.items():

    #Create Dictionary of foods
    luitnerDict = {}

    #Move and format food items to dictionarys
    for x in range(len(meal)):
        food = meal[x].text.strip() #formats and removes white space
        food = re.sub('\[.*?\]', '', food) #removes farm information
        food = food.replace("\u00f1", "n") #fixes Nne character
        luitnerDict[x] = food #add item to dictionary

    #Dump dictionaries to json files
    with open('luitner'+luitnerMealNames[mealIndex]+'.json', 'w') as fp:
        json.dump(luitnerDict, fp, indent=4)


