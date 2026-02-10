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
for item in order: #Discount mechanism
    price += 5
if price >= 20:
    price = price * 0.8
elif price >= 10:
    price = price * 0.9

f = open("Orders.txt", "x") #Save order to system
for i in order:
    f.write(i + "\n")
f.write(str(price) + "\n")
f.close()

f = open("Orders.txt") #Display receipt
print(f.read())