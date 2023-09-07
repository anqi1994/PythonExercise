smallest = None
largest = None

a = input("Please enter a number, if you want to end the program, press enter:\n")
while a != "":
    a = float(a)
    if smallest == None:
        smallest = a
    elif a < smallest:
        smallest = a
    if largest == None:
        largest = a
    elif a > largest:
       largest = a
    a = input("Please enter a number, if you want to end the program, press enter:\n")
print("The smallest number is {}, and the largest number is {}".format(smallest, largest))


#improved version
a = input("Please enter a number, if you want to end the program, press enter:\n")
while a != "":
    a = float(a)
    if smallest == None or a < smallest:
        smallest = a
    if largest == None or a > largest:
        largest = a
    a = input("Please enter a number, if you want to end the program, press enter:\n")
if smallest != None and largest != None:
    print("The smallest number is {}, and the largest number is {}".format(smallest, largest))
else:
    print("No valid number is entered.")