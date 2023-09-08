lst = []
a = input("Enter a number, press Enter to stop: ")
while a != "":
    if a.isdigit():
        a = float(a)
        lst.append(a)
    else:
        print("Invalid input, please enter a number.")
    a = input("Enter a number, press Enter to stop: ")
if len(lst) >= 5:
    sorted_lst = sorted(lst, reverse=True)
    print("The largest five numbers are:",sorted_lst[0: 5])
else:
    print("We need at least five numbers, please enter again. ")



