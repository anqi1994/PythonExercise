import random
combination3a = str(random.randint(0,9))
combination3b = str(random.randint(0,9))
combination3c = str(random.randint(0,9))
combination3 = combination3a + combination3b + combination3c
com4a = str(random.randint(1,6))
com4b = str(random.randint(1,6))
com4c = str(random.randint(1,6))
com4d = str(random.randint(1,6))
com4 = com4a + com4b + com4c + com4d
print("The combination is:", combination3 + com4)

#something harder
int3 = [random.randint(0,9) for a in range(3)]
int4 = [random.randint(1,6) for a in range(4)]
com3 = "".join(map(str, int3))
com4 = "".join(map(str, int4))
print("The combination is:", com3 + com4)