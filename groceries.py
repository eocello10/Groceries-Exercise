
# groceries.py

#from pprint import pprint

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

#print(products)
# pprint(products)

# TODO: write some Python code here to produce the desired output

#conda create -n groceries-env python=3.7 # (first time only) - create environmentw we will use
#conda activate groceries-env - activate that environemnt 

products_count  = len(products) # len helps us count certain parameter

#print ("THERE ARE " + str(products_count) + " PRODUCTS") # to print how many products there are

def sort_by_name(any_product): # the p's are seperate for each other if I were to use p
    return any_product ["name"]
sorted_products = sorted(products, key=sort_by_name)


for p in sorted_products: 
    #print (p["name"])
    #price_usd = p["price"] #$4.99
    price_usd = " (${0:.2f})".format(p["price"])
    #print (" ... " + p["name"] + price_usd) # string concatentation allows us to combine items - Removed string was similar to(look at 30/35 VS text of video for exercise) " + str(price_usd) +"
# TypeError: can only concatenate str (not "float") to str - when this error coems up we have to use str as seen above

    #"id":1, 
    #"name": "Chocolate Sandwich Cookies", 
    #"department": "snacks",
    # "aisle": "cookies cakes",
    #"price": 3.50}
     # if we add or subtract products don't want this to be hard coded
# if products = ID ("1")
 #   print("Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes")


#Print the number of products. - this is the string concatentation with a more dyanic approach
#Print the first product.
#Print the name of the first product.
#Print the name of each product.
#Print in alphabetical order the name of each product.
#Print in alphabetical order the name and price of each product. - this is string concatentation of nam + price with the sort above
#Print in alphabetical order the name and price of each product, where the price is rounded to two decimal places. - this is the 0:2f item
#--------------")
#THERE ARE 20 PRODUCTS:
#--------------
# + All-Seasons Salt ($4.99)
# + Chocolate Fudge Layer Cake ($18.50)
# + Chocolate Sandwich Cookies ($3.50)
# + Cut Russet Potatoes Steam N' Mash ($4.25)
# + Dry Nose Oil ($21.99)
# + Fresh Scent Dishwasher Cleaner ($4.99)
# + Gluten Free Quinoa Three Cheese & Mushroom Blend ($3.99)
# + Green Chile Anytime Sauce ($7.99)
# + Light Strawberry Blueberry Yogurt ($6.50)
# + Mint Chocolate Flavored Syrup ($4.50)
# + Overnight Diapers Size 6 ($25.50)
# + Peach Mango Juice ($1.99)
# + Pizza For One Suprema Frozen Pizza ($12.50)
# + Pomegranate Cranberry & Aloe Vera Enrich Drink ($4.25)
# + Pure Coconut Water With Orange ($3.50)
# + Rendered Duck Fat ($9.99)
# + Robust Golden Unsweetened Oolong Tea ($2.49)
# + Saline Nasal Mist ($16.00)
# + Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce ($6.99)
# + Sparkling Orange Juice & Prickly Pear Beverage ($2.99)


#Department Work


Departments = []
for p in products:
    #print(p["department"])
    
    #Question regarding this don't quite understand it
    #if p["department"] not in Departments:
        Departments.append(p["department"])
        # convert list to set remove du[licates vs. using the append function

unique_departments = list(set(Departments)) # see note above. Can use list, set or append to remove duplicates

Departments_count = len(unique_departments)
print("There are " + str(Departments_count) + " Departments")


unique_departments.sort()

for d in unique_departments:
    matching_products = [p for p in products if p["department"] == d] # where does d get defined or p for tht matter
    matching_products_count = len(matching_products)
    print(d.title() + " (" + str(matching_products_count) + " products)" )

# filtering to perform a count


