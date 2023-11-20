num= input("Please enter an integer:")
n = 2
lst = []
try:
    num= int(num)
    if num >= 0:
        while n < num:
            if num % n == 0:
                lst.append(n)
                n = n + 1
            else:
                n = n + 1
        if lst != [] or num == 1 or num == 0:
            print("It is not a prime number.")
        else:
            print("It is a prime number.")
    else:
        print("Prime number cannot be a negative number.")
except:
    print("value error")


pro([1,2,3,4])