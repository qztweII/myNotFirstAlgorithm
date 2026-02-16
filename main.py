import json

with open("menu.json") as menu: #Loading menu from a json file
    rawMenu = json.load(menu)

def studentOrder(): #Takes the order
    order = []
    doneOrdering = False
    global rawMenu
    
    cookedMenu = []
    for i in rawMenu["menu"]:
        cookedMenu.append(i["item"])

    while not doneOrdering: #Taking Order, each item is assigned a numerical id
        for i in range(len(cookedMenu)): #Interface
            print(f"[{i}] {cookedMenu[i]}")
        print("[E] Finish Ordering")

        try: #Taking order, make sure input is a number corresponding to a numerical id
            itemToOrder = input("Please use number to select a food: ")
            if itemToOrder.upper() == "E":
                doneOrdering = True
                if len(order) == 0: #Nothing ordered safeguard
                    print("You cannot have a none order!")
            else:
                itemToOrder = int(itemToOrder)
                cookedMenu[itemToOrder] #Check if itemToOrder is out of range
        except:
            print("Invalid input. Please enter a number to select your item")
        else:
            if itemToOrder != "E":
                order.append(cookedMenu[itemToOrder])
    return order #Returns a list

def calculateTotal(order): #Calculates the total price of order
    global rawMenu
    price = 0
    pricedMenu = {} #make the function's menu
    for i in rawMenu["menu"]:
        pricedMenu[i["item"]] = i["price"]
    
    for item in order: #For now, literally everything is five
        price += pricedMenu[item]
    
    return round(price, 2) #Returns a float

def applyDiscount(price): #Applies a discount above certain prices
    if price >= 20: #Discount mechanism
        price = price * 0.8
        discount = 20
    elif price >= 10:
        price = price * 0.9
        discount = 10
    else:
        discount = 0
    
    return [round(price, 2), discount]
def priceCheck(price): #Safeguard for if somehow, just somehow the price is below zero
    if price <= 0: #Exit if the price is somehow below zero
            print("Oh no! Why is the price zero??")
            exit()

def receipt(name, order, price, discount): #Save order to system and display receipt
    global f
    openedFile = False
    attempts = 0
    while not openedFile:
        try:
            fileName = f"orders/Orders{attempts}.txt"
            f = open(fileName, "x")
        except:
            attempts += 1
        else:
            openedFile = True

    #Save order to system
    f.write(name + "\n")
    for i in order:
        f.write(i + "\n")
    f.write(str(price) + "\n")
    if discount > 0:
        f.write(f"Discount applied: {discount}%")
    f.close()

    f = open(fileName) #Display receipt
    print(f.read())

#Main Application runner thing I forgot the terminology
name = input("Hi! What is your name?")
order = studentOrder()
price = calculateTotal(order)
priceAndDiscount = applyDiscount(price)
priceCheck(price)
receipt(name, order, priceAndDiscount[0], priceAndDiscount[1])