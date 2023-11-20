a = 0
while (a<5):
    b = 0
    while (b<6):
        b += 1
        print(f"{a} multiplied with {b} is {a*b}.")
    a += 1


lst = ["Kimo", "Jen", "Moh", "Jane"]
lst.append("May")
print(lst[0:2])
print(lst[1:])

for xid, x in enumerate(lst):
    if (x != lst[-1]):
        #-1 is the last element of the list
        print(f"x is {x} and the lst index is {lst[xid+1]}.")

for x in lst:
    print(x)

for i in range(0, 7, 2):
    print(i)

str = "abcdefghijkl"
for i in range(0, len(str)):
    if (i != 0):
        print(str[i-1] + str[i])

nmb = ["4", "6", "7"]
nmb = [int(x) for x in nmb]
print(nmb)
