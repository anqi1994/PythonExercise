talents = float(input("Enter talents: \n"))
pounds = float(input("Enter pounds: \n"))
lots = float(input("Enter lots: \n"))
lots = talents * 20 * 32 + pounds * 32 + lots
gram = lots * 13.3
kilo = int(gram / 1000)
gram = round(gram - kilo*1000, 2)
print("The weight in modern units: \n{} kilograms and {} grams.".format(kilo, gram))
