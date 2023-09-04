year = int(input("Please enter the year: "))
if year / 4 - int(year / 4) == 0:
    if year / 100 - int(year / 100) == 0:
        if year / 400 - int(year / 400) == 0:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

#simplified version
year = int(input("Please enter the year: "))
if (year % 4 == 0 and year % 4 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")