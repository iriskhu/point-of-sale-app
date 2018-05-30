# shopping_cart.py

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
]
#based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#~~~~~~~~~~~~~~~~~~~~CHECK POINT 1~~~~~~~~~~~~~~~~~~~~~~~
                #CAPTURE USER INPUTS

product_ids = []

while True:
    product_id = input("Hey please input a product identifer, or 'DONE' if there are no more items: ")
    #to capture user input and store in variable
    if product_id == "DONE":
        break
    else:
        product_ids.append(int(product_id))

# "while True" is an infinite loop---it's always gonna be true. Never gonna stop. So we need to exit from this infinite loopself.
# "break" will stop your loop
# "int" is to convert to integer because user inputs are treated as strings.

                #CAPTURE EVERYTHING (the whole receipt) AFTER CAPTURING USER INPUTS

print ("---------------------------------")
print ("Iris Kunyang Hu's Grocery Store")
print ("---------------------------------")
print ("Phone: 1(612)-777-0924")
print ("Website: www.iriskhu.grocery.com")


import datetime
#(why "import", not "define"? b/c datetime is a module)

Checkout_time = datetime.datetime.now()
print (str(Checkout_time.strftime("%A, %B, %d, %Y at %I:%M, %p")))

print ("---------------------------------")


#~~~~~~~~~~~~~~~~~~~~~~~~CHECK POINT 2~~~~~~~~~~~~~~~~~~~~~~~~
#some commented-out loop
#...representing the result of the first checkpoint
#...which accepts user inputs and prints the results

#product_ids = [3, 6, 9, 12] #temporary list of valid ids for testing purpose


raw_total = 0

print ("SHOPPING CART ITEMS:")
for product_id in product_ids:
    matching_products = [product for product in products if product["id"] == product_id]
    matching_product = matching_products[0]
    raw_total = raw_total + matching_product["price"]
    print(" + " + matching_product["name"] + " (" + str("${0:.2f}".format(matching_product["price"])) + ")")

print ("---------------------------------")
print ("RUNNING TOTAL: " + str("${0:.2f}".format(raw_total)))


#~~~~~~~~~~~~~~~~~~~~~~~~CHECKPOINT 3~~~~~~~~~~~~~~~~~~~~~~~~~~
tax_owed = raw_total * 0.08875
print ("PLUS NYC SALES TAX: " + str("${0:.2f}".format(tax_owed)))

total_owed = raw_total + tax_owed
print ("TOTAL: " + str("${0:.2f}".format(total_owed)))

print ("---------------------------------")
print ("Thanks for your business! Please come again.")
print ("---------------------------------")
