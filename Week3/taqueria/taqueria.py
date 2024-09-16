menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

x = menu.items()
menu_list = []
for item in x:
    temp = item[0].lower()
    menu_list.append(temp)

total = 0.0
while True:
    try:
        inp = input("Item: ").lower()
        if inp in menu_list:
            inp = inp.title()
            total += menu[inp]
            print("Total: $%.2f" % total)
    except EOFError:
        break
