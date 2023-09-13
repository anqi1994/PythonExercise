import random
def rolldice():
    num = random.randint(1,6)
    return num

#main program
lst = []
att = rolldice()
while att != 6:
    lst.append(att)
    att = rolldice()

print("This is the result:")
lst.append(6)
print(lst)


