import json
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

#Create Dictionarys for meals
friblyMeals = {}
friblyMealNames = {}
luetnerMeals = {}
luetnerMealNames = {}

# Set links for dining halls
friblyUrl = urlopen("https://case.cafebonappetit.com/cafe/fribley-marche/")
#friblyUrl = urlopen("https://case.cafebonappetit.com/cafe/fribley-marche/2018-12-02/") #sunday website
luetnerUrl = urlopen("https://case.cafebonappetit.com/cafe/leutner-cafe/")

#Create Soups
friblySoup = BeautifulSoup(friblyUrl, "html.parser")
luetnerSoup = BeautifulSoup(luetnerUrl, "html.parser")

#Get Breakfast
friblyBreakfast = friblySoup.find('section', id='breakfast') #Finds just breakfast section
if friblyBreakfast is None: #Checks if breakfast is served
    print ("No Breakfast")
else:
    friblyBreakfastFood = friblyBreakfast.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
    friblyMeals[1] = friblyBreakfastFood #Adds breakfast to list of meals
    friblyMealNames[1] = "Breakfast" #Adds breakfast to list of meal names

luetnerBreakfast = luetnerSoup.find('section', id='breakfast') #Finds just breakfast section
if luetnerBreakfast is None: #Checks if breakfast is served
    print ("No Breakfast")
else:
    luetnerBreakfastFood = luetnerBreakfast.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
    luetnerMeals[1] = luetnerBreakfastFood #Adds breakfast to list of meals
    luetnerMealNames[1] = "Breakfast" #Adds breakfast to list of meal names

#Get Brunch
friblyBrunch = friblySoup.find('section', id='brunch') #Finds just brunch section
if friblyBrunch is None: #Checks if brunch is served
    print ("No Brunch")
else:
    friblyBrunchFood = friblyBrunch.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
    friblyMeals[1] = friblyBrunchFood  #Adds Brunch to list of meals
    friblyMealNames[1] = "Brunch" #Adds brunch to list of meal names

luetnerBrunch = luetnerSoup.find('section', id='brunch') #Finds just brunch section
if luetnerBrunch is None: #Checks if brunch is served
    print ("No Brunch")
else:
    luetnerBrunchFood = luetnerBrunch.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
    luetnerMeals[1] = luetnerBrunchFood  #Adds Brunch to list of meals
    luetnerMealNames[1] = "Brunch" #Adds brunch to list of meal names

#Get Lunch
friblyLunch = friblySoup.find('section', id='lunch') #Finds just lunch section
if friblyLunch is None: #Checks if Lunch is served
    print ("No Lunch")
else:
    friblyLunchFood = friblyLunch.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
    friblyMeals[2] = friblyLunchFood  #Adds Lunch to list of meals
    friblyMealNames[2] = "Lunch" #Adds Lunch to list of meal names

luetnerLunch = luetnerSoup.find('section', id='lunch') #Finds just lunch section
if luetnerLunch is None: #Checks if Lunch is served
    print ("No Lunch")
else:
    luetnerLunchFood = luetnerLunch.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
    luetnerMeals[2] = luetnerLunchFood  #Adds Lunch to list of meals
    luetnerMealNames[2] = "Lunch" #Adds Lunch to list of meal names

#Get Dinner
friblyDinner = friblySoup.find('section', id='dinner') #Finds just dinner section
friblyDinnerFood = friblyDinner.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
if len(friblyMeals) == 2:  #Adds Dinner to list of meals, but also checks to see if there was brunch or not
    friblyMeals[3] = friblyDinnerFood
    friblyMealNames[3] = "Dinner"
else:
    friblyMeals[2] = friblyDinnerFood
    friblyMealNames[2] = "Dinner"

luetnerDinner = luetnerSoup.find('section', id='dinner') #Finds just dinner section
luetnerDinnerFood = luetnerDinner.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
if len(luetnerMeals) == 2:  #Adds Dinner to list of meals, but also checks to see if there was brunch or not
    luetnerMeals[3] = luetnerDinnerFood
    luetnerMealNames[3] = "Dinner"
else:
    luetnerMeals[2] = luetnerDinnerFood
    luetnerMealNames[2] = "Dinner"

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
    
#Create A Json file for all of the meals at luetner
for mealIndex, meal in luetnerMeals.items():

    #Create Dictionary of foods
    luetnerDict = {}

    #Move and format food items to dictionarys
    for x in range(len(meal)):
        food = meal[x].text.strip() #formats and removes white space
        food = re.sub('\[.*?\]', '', food) #removes farm information
        food = food.replace("\u00f1", "n") #fixes Nne character
        luetnerDict[x] = food #add item to dictionary

    #Dump dictionaries to json files
    with open('luetner'+luetnerMealNames[mealIndex]+'.json', 'w') as fp:
        json.dump(luetnerDict, fp, indent=4)
