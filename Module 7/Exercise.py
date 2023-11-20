my_list = {
    "milk" : 2,
    "juice" : 3,
    "oat" : 4
}
while True:
    def additem(item, value):
    if item in my_list:
      my_list[item] += value
        else:
            my_list[item] = value
        print(f"The item {item} added in the shopping list.")

    def display():
        for item, value in my_list.items():
            print(item, ": ", value)


   display())

   eys = my_list.keys()
   print(eys)


