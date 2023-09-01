import math
str_num = input("Enter three integers divided by space: \n")
single = str_num.split()
nums = [int(num) for num in single]
sum = sum(nums)
pro = math.prod(nums)
avg = sum / 3
print("Their sum is {}, their product is {}, and their average is {}.".format(sum, pro, avg))

first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))
third = int(input("Enter the third integer: "))
sum = first + second + third
pro = first * second * third
avg = sum / 3
print("Their sum is {}, their product is {}, and their average is {}.".format(sum, pro, avg))