import random
def rolldice(num):
    ranint = random.randint(1, num)
    return ranint

lst = []
num = input("input the maximum number of the dice, make sure it is a positive integer: \n")
try:
    num = int(num)
    if num > 0:
        ranint = None
        while ranint != num:
            ranint = rolldice(num)
            lst.append(ranint)
    else:
        print("Invalid input. It must be a positive integer.")
except ValueError:
   print("Invalid input. It must be an integer.")

print("Here is your result:")
print(lst)