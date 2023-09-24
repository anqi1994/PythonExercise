airportdata = {}
choice = input("If you want to enter a new airport, enter'1',\n"
               "If you want to fetch the information of an existing airport,"
               "enter'2';\n"
               "If you want to quit, press enter.\n")
while choice != "":
    if choice == "1":
        code = input("Please enter the ICAO code of the airport:\n")
        if code in airportdata:
            print("This airport already exist.")
        else:
            name = input("Please enter the name of the airport:\n")
            airportdata[code] = name
            print(f"{name} has been saved.")
    elif choice == "2":
        code = input("Please enter the ICAO code of the airport:\n")
        if code in airportdata:
            print(f"The name of this airport is {airportdata[code]}.")
        else:
            print("Cannot find information about this airport.")
    else:
        print("Please enter 1 or 2, or press enter.")
    choice = input("If you want to enter a new airport, enter'1',\n"
                   "If you want to fetch the information of an existing airport,"
                   "enter'2';\n"
                   "If you want to quit, press enter.\n")
print("Goodbye.")

