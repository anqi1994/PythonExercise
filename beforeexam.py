#distance = input("How many kilometers do you want to travel?")

def fuel(distances):
    fuel = (distances / 100 * 5)
    return fuel

def price(fuel):
    price = fuel * 1.95
    price = round(price,2)
    return price

n=0
while True:

    distances = input("How many kilometers do you want to travel?");
    if len(distances) > 0:
        fuels = fuel(float(distances))
        prices = price(float(fuels))
        print(f"If you want to travel {distances} kilometers, you need {fuel} litre of fuel.")
        print(f"For this amount of the fuel, you need to pay {price} euros.")
        n += 1
    else:
        break
    ans = input("If you want to continue traveling, enter yes; otherwise, press enter.")
    if ans =='':
        break


print(n)
print("Goodbye!")

