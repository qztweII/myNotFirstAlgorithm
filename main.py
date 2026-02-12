name = input("Hi! What is your name?")
doneOrdering = False
order = []
while not doneOrdering: #Taking Order
    itemToOrder = input("What would you like to order? Type \"done\" when finished ordering. ")
    if itemToOrder == "done":
        doneOrdering = True
    else:
        order.append(itemToOrder)

price = 0
discount = 0
for item in order: #Discount mechanism
    price += 5
if price >= 20:
    price = price * 0.8
    discount = 20
elif price >= 10:
    price = price * 0.9
    discount = 10

#Open a new receipt file
openedFile = False
attempts = 0
while not openedFile:
    try:
        fileName = f"Orders{attempts}.txt"
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