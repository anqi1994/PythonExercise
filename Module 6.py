def sum(a, b):
    total = a + b
    return total
import random
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
print("here is the result ", sum(a, b))



def substract(a, b):
    ans = a - b
    return ans
print(substract(a, b))

def multiply(a, b):
    mult = a * b
    return mult
print(multiply(a,b))

def division(a,b):
    if b != 0:
        divis = a / b
    else:
        print("Invalid number")
    return divis
print(division(a,b))
