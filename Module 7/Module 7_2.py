nameset = set()
name = input("Please enter a name, if you want to quit, press enter.\n")

while name != "":
    if name not in nameset:
        nameset.add(name)
        print("New name")
    else:
        print("Existing name")
    name = input("Please enter a name, if you want to quit, press enter.\n")
print("Namelist:")
for name in nameset:
    print(name)