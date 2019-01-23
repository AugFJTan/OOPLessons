###########################################################################################
# File       : recipe.py
# Date       : 23/01/2019
# Description: Program to show how classes are used as templates, how objects are created
#              and simple inheritance
###########################################################################################

# Use python library to generate random numbers
import random

# Class to use as template for our object
class RecipeSelector:
	# Class constructor method
	def __init__(self, recipes): # recipes is a list of strings
		self.recipes = recipes   # self denotes field of this class
	
	# Normal method
	# Displays recipes for one week with no same recipe for two consecutive days
	def WhatToCook(self):
		day_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
		
		yesterday = ""
		
		for dow in day_of_week:
			today = yesterday
		
			while yesterday == today:
				today = self.recipes[random.randrange(len(self.recipes))] # select a random recipe
			
			print(dow + ": " + today)
			
			yesterday = today
		
		print()

# New Drinks class that inherits from RecipeSelector class
class Drinks(RecipeSelector):
	# Class constructor method
	def __init__(self, recipes, prices): # prices is a list of numbers
		super().__init__(recipes)        # Call constructor of base class (RecipeSelector)
		self.prices = prices
	
	# Method to extend functionality of Drinks
	def ShowPrices(self): 
		for i in range(len(self.recipes)):
			print("{0} = {1}".format(self.recipes[i], self.prices[i]))
			
my_recipes = ["Chicken soup", "Steamed fish", "Boiled vege", "Spaghetti", "Fried chicken"]
my_other_recipes = ["Pizza", "Sushi", "Steak", "Burger", "Roast chicken", "Barbeque ribs"]

my_drinks = ["Coffee", "Tea", "Barley", "Orange juice", "Lemonade"]
prices = [1.5, 1.0, 0.8, 2.5, 3.0]

# Create object using RecipeSelector class
rs = RecipeSelector(my_recipes)
rs.WhatToCook()

# Create difference object using RecipeSelector class
rs2 = RecipeSelector(my_other_recipes)
rs2.WhatToCook()

# Drinks class can use WhatToCook() method from RecipeSelector class as well as new method ShowPrices()
drinks = Drinks(my_drinks, prices)
drinks.WhatToCook()
drinks.ShowPrices()
