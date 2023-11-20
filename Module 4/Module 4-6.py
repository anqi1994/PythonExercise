import random
randf1 = random.uniform(0, 1)
randf2 = random.uniform(0,1)
n = 0
n_all = 0
ran1 = []
ran2 = []
while True:
    if n_all < 1000000:
        if randf1 ** 2 + randf2 ** 2 < 1:
            n = n + 1
            n_all = n_all + 1
        else:
            n_all = n_all + 1
        randf1 = random.uniform(0, 1)
        randf2 = random.uniform(0,1)
    else:
        break
pie = 4 * n / n_all
print(f"The value of pi is about {pie}.")
