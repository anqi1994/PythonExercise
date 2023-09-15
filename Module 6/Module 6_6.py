import math
def pizza(dia, price):
    area = (dia / 2) ** 2 * math.pi
    unitprice = price /area
    return unitprice

dia1 = float(input("What is the diameter of the pizza in centimeters?\n"))
price1 = float(input("What is the price of the pizza?\n"))
res1 = pizza(dia1, price1)

dia2 = float(input("What is the diameter of the pizza in centimeters?\n"))
price2 = float(input("What is the price of the pizza?\n"))
res2 = pizza(dia2, price2)

if res1 > res2:
    print("The second pizza provides a better value.")
elif res1 == res2:
    print("The two pizzas have the same unit price")
else:
    print("The first pizza provides a better value.")