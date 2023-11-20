lst = []
def addtask(task):
    lst.append(task)
    print(f"Task '{task}' added!")

def removetask(task):
    if task in lst:
        lst.remove(task)
        print(f"Task '{task}' deleted!")
    else:
        print(f"Task '{task}' is not in the list.")

def displaylist():
    if not lst:
        print("Your list is empty.")
    else:
        print("Your list is: ")
        for index, item in enumerate(lst):
            print(index, item)

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Display the list.")
    print("4.quit.")
    choice = input("Enter your choice ")
    if choice == "1":
        task = input("Enter the task you want to add:")
        addtask(task)
    elif choice == "2":
        task = input("Enter the task you want to remove:")
        removetask(task)
    elif choice == "3":
        displaylist()
    elif choice == "4":
        print("Goodbye!")
    else:
        print("Invalid input.")




myTuples = (1, 2, 3)
print(myTuples)
print(myTuples[1:])

myTuples2 = (1,)
print(myTuples2)

point = (2, 3)
x, y = point
print(x)

grades = (1, 2, 3, 4, 5, 6)
total = 0
for grade in grades:
    total += grade
    print(f"grade are {grade}.")
print(f"The total is {total}.")

avg = total /len(grades)
print(f"This is the average:{avg}.")
