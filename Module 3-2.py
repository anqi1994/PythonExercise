cc = input("Please enter your cabin class as follows:\nLUX, A, B, or C\nCabin Class: ")
if cc == "LUX":
    print("Upper deck cabin with a balcony.")
elif cc == "A":
    print("Above the car deck, equipped with a window.")
elif cc == "B":
    print("Windowless cabin above the car deck.")
elif cc == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class, please enter LUX, A, B, or C.")