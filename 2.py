import math
formatPI = f"value of PI: {math.pi}"
print(formatPI)

pi: float = 3.141592656
formatPI = "value of PI: {:.2f}".format(math.pi)
# .2f decimals
print(formatPI)

radius = float(input("Enter the radius "))
areaCircle = math.pi * radius ** 2
# the same as radius * radius
print(f"Area of circle {areaCircle:.2f}")
print("hello world")