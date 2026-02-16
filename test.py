import json

with open("menu.json") as menu:
    rawMenu = json.load(menu)

cookedMenu = []
for i in rawMenu["menu"]:
    cookedMenu.append(i["item"])

pricedMenu = {}
for i in rawMenu["menu"]:
    pricedMenu[i["item"]] = i["price"]

print(pricedMenu)