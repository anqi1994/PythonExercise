lst = []
n = 0
while n < 5:
    city = input("Enter the name of a city:\n")
    lst.append(city)
    n = n + 1
for i in lst:
    print(i)

#use range
lst = []
for city in range(5):
    city = input(f"Enter the name of a city {city + 1}")
    lst.append(city)
print("List of cities:")
for city in lst:
    print(city)