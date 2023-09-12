num= input("Please enter an integer:")
lst = []
try:
    num= int(num)
    if num > 0:
        for n in range(2, num):
            if num % n == 0:
                lst.append(n)
            else:
                continue
        if lst != [] or n == 1 or n == 0:
            print("This is not a prime number.")
        else:
            print("This is a prime number.")
    else:
        print("The prime number cannot be negative.")
except:
    print("Invalid input.")
