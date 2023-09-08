import random
num = int(input("How many dices do you want to roll?\n"))
dice = []
while num > 0:
    dice.append(random.randint(1,9))
    num = num - 1
ans = 0
#print(dice)
for x in dice:
    ans += x
print("The sum the numbers is", ans)
