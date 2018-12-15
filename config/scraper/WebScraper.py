
import json
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen


#Create Dictionarys for meals
fribleyMeals = {}
fribleyMealNames = {}
leutnerMeals = {}
leutnerMealNames = {}

# Set links for dining halls
fribleyUrl = urlopen("https://case.cafebonappetit.com/cafe/fribley-marche/")
leutnerUrl = urlopen("https://case.cafebonappetit.com/cafe/leutner-cafe/")

#other days used for testing
#fribleyUrl = urlopen("https://case.cafebonappetit.com/cafe/fribley-marche/2018-12-17/")
#leutnerUrl = urlopen("https://case.cafebonappetit.com/cafe/leutner-cafe/2018-12-17/")


#Create Soups
fribleySoup = BeautifulSoup(fribleyUrl, "html.parser")
leutnerSoup = BeautifulSoup(leutnerUrl, "html.parser")

#Get Breakfast
fribleyBreakfast = fribleySoup.find('section', id='breakfast') #Finds just breakfast section
if fribleyBreakfast is not None: #Checks if breakfast is served
    fribleyBreakfast = fribleyBreakfast.find('div', tabindex='0') #Selects just the first 'specials' tab
    fribleyBreakfastFood = fribleyBreakfast.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
    fribleyMeals[1] = fribleyBreakfastFood #Adds breakfast to list of meals
    fribleyMealNames[1] = "Breakfast" #Adds breakfast to list of meal names

leutnerBreakfast = leutnerSoup.find('section', id='breakfast') #Finds just breakfast section
if leutnerBreakfast is not None: #Checks if breakfast is served
    leutnerBreakfast = leutnerBreakfast.find('div', tabindex='0') #Selects just the first 'specials' tab
    leutnerBreakfastFood = leutnerBreakfast.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
    leutnerMeals[1] = leutnerBreakfastFood #Adds breakfast to list of meals
    leutnerMealNames[1] = "Breakfast" #Adds breakfast to list of meal names

#Get Brunch
fribleyBrunch = fribleySoup.find('section', id='brunch') #Finds just brunch section
if fribleyBrunch is not None: #Checks if brunch is served
    fribleyBrunch = fribleyBrunch.find('div', tabindex='0') #Selects just the first 'specials' tab
    fribleyBrunchFood = fribleyBrunch.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
    fribleyMeals[1] = fribleyBrunchFood  #Adds Brunch to list of meals
    fribleyMealNames[1] = "Brunch" #Adds brunch to list of meal names

leutnerBrunch = leutnerSoup.find('section', id='brunch') #Finds just brunch section
if leutnerBrunch is not None: #Checks if brunch is served
    leutnerBrunch = leutnerBrunch.find('div', tabindex='0') #Selects just the first 'specials' tab
    leutnerBrunchFood = leutnerBrunch.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
    leutnerMeals[1] = leutnerBrunchFood  #Adds Brunch to list of meals
    leutnerMealNames[1] = "Brunch" #Adds brunch to list of meal names

#Get Lunch
fribleyLunch = fribleySoup.find('section', id='lunch') #Finds just lunch section
if fribleyLunch is not None: #Checks if Lunch is served
    fribleyLunch = fribleyLunch.find('div', tabindex='0') #Selects just the first 'specials' tab
    fribleyLunchFood = fribleyLunch.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
    fribleyMeals[2] = fribleyLunchFood  #Adds Lunch to list of meals
    fribleyMealNames[2] = "Lunch" #Adds Lunch to list of meal names

leutnerLunch = leutnerSoup.find('section', id='lunch') #Finds just lunch section
if leutnerLunch is not None: #Checks if Lunch is served
    leutnerLunch = leutnerLunch.find('div', tabindex='0') #Selects just the first 'specials' tab
    leutnerLunchFood = leutnerLunch.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
    leutnerMeals[2] = leutnerLunchFood  #Adds Lunch to list of meals
    leutnerMealNames[2] = "Lunch" #Adds Lunch to list of meal names

#Get Dinner
fribleyDinner = fribleySoup.find('section', id='dinner') #Finds just dinner section
fribleyDinner = fribleyDinner.find('div', tabindex='0') #Selects just the first 'specials' tab
fribleyDinnerFood = fribleyDinner.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
if len(fribleyMeals) == 2:  #Adds Dinner to list of meals, but also checks to see if there was brunch or not
    fribleyMeals[3] = fribleyDinnerFood
    fribleyMealNames[3] = "Dinner"
else:
    fribleyMeals[2] = fribleyDinnerFood
    fribleyMealNames[2] = "Dinner"

leutnerDinner = leutnerSoup.find('section', id='dinner') #Finds just dinner section
leutnerDinner = leutnerDinner.find('div', tabindex='0') #Selects just the first 'specials' tab
leutnerDinnerFood = leutnerDinner.find_all('button',class_='h4 site-panel__daypart-item-title') #Selects all food items
if len(leutnerMeals) == 2:  #Adds Dinner to list of meals, but also checks to see if there was brunch or not
    leutnerMeals[3] = leutnerDinnerFood
    leutnerMealNames[3] = "Dinner"
else:
    leutnerMeals[2] = leutnerDinnerFood
    leutnerMealNames[2] = "Dinner"

if fribleyBreakfast is None and fribleyLunch is None and leutnerBreakfast is None and leutnerLunch is None:
    print ("brunch")
else:
    print("normal")

#Create A Json file for all of the meals at fribley
for mealIndex, meal in fribleyMeals.items():

    #Create list of foods
    fribleyList = list()

    #Move and format food items to list
    for x in range(len(meal)):
        food = meal[x].text.strip() #formats and removes white space
        food = re.sub('\[.*?\]', '', food) #removes farm information
        food = food.replace("\u00f1", "n") #fixes Nne character
        fribleyList.append(food) #add item to list

    #Dump list to json files
    with open('fribley'+fribleyMealNames[mealIndex]+'.json', 'w') as fp:
        json.dump(fribleyList, fp, indent=4)

#Create A Json file for all of the meals at leutner
for mealIndex, meal in leutnerMeals.items():

    #Create list of foods
    leutnerList = list()

    #Move and format food items to list
    for x in range(len(meal)):
        food = meal[x].text.strip() #formats and removes white space
        food = re.sub('\[.*?\]', '', food) #removes farm information
        food = food.replace("\u00f1", "n") #fixes Nne character
        leutnerList.append(food) #add item to list

    #Dump list to json files
    with open('leutner'+leutnerMealNames[mealIndex]+'.json', 'w') as fp:
        json.dump(leutnerList, fp, indent=4)
