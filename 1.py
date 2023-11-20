a = range(3,0,-1)
b = [2,0,2,3]
n = 0
for i in a:
    m = 0
    for c in b:
        if i == c:
            m += 1
        n += 1
    print(m)
print(n)


(a, b) = (2, 3)
color = (a, b)
print(color[1])
print(color)
