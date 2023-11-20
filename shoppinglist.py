item = input("What do you want to purchase?\n")
lis = []
while item != "":
    lis.append(item)
    item = input("What do you want to purchase?\n")
else:
    print("This is your shopping list:")
    for x in lis:

        print(x)