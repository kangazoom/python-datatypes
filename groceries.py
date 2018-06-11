# groceries.py
# MICHELLE CRONIN

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# PRODUCTS

print("--------------\n THERE ARE {0} PRODUCTS:\n--------------".format(len(products)))

# create function to use later for sort
# returns names of products
def sort_by_name(product):
  return product["name"]

# use names of products as key to alphabetically sort product names
products_alpha = sorted(products, key=sort_by_name)

# print alphabetized results, consistent with assignment formatting
for p in products_alpha:
  print(" + {0} (${1:.2f})".format(p["name"], p["price"]))

# DEPARTMENTS

# find out how many unique departments there are:
# add all department to a list
listy = []
for p in products:
  listy.append(p["department"])
# SET only includes unique values
listy = set(listy)

print("\n\n--------------\nTHERE ARE {0} DEPARTMENTS:\n--------------".format(len(listy)))


# # sort departments in alphabetical order
# listy_alpha = sorted(listy)
#
# # add all the department values, including repeats, to a list
# # listy_alpha has unique department names, arranged alphabetically
# dept_repeats = []
# for department in listy_alpha:
#   for key in products:
#     if key["department"] == department:
#       dept_repeats.append(key["department"])
#
# # create a dictionary with alphabetically listed departments (unique) as keys
# dict_counter = {}.fromkeys(listy_alpha)
#
# # make all values 0 since I need to use it as a counter later on
# for key in dict_counter:
#   dict_counter[key] = 0
#
# # whenever the dictionary key matches with the department names in the list of all department mentions, increase related dictionary value by 1
# # Note: Maybe I didn't need to create dept_repeats and could have just worked with the values from the original products hash
# for key in dict_counter:
#   for dept in dept_repeats:
#     if key == dept:
#       dict_counter[key] += 1
#
#
#
# # Format results as indicated in assignment and vary grammar depending on number of products
# for key in dict_counter:
#   if dict_counter[key] <= 1:
#     print("+ {0} ({1} product)".format(key.title(), dict_counter[key]))
#   else:
#      print("+ {0} ({1} products)".format(key.title(), dict_counter[key]))
