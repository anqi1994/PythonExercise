month = input("Enter the month:\n")
spring = ("March", "April", "May")
summer = ("June", "July", "August")
autumn = ("September", "October", "November")
winter = ("December", "January", "February")

if month in spring:
    print("It is spring.")
elif month in summer:
    print("It is summer.")
elif month in autumn:
    print("It is autumn.")
elif month in winter:
    print("It is winter.")
else:
    print("Invalid input, please enter the month from January to December.")

