students = []
students.append(("Amir", (30, 30, 89, 100)))
students.append(("Timo",(40, 500, 89, 90)))
students.append(("Outi", (10, 30, 89, 60)))

nametofind = input("Enter a name to search:")
found = False
for student in students:
    if student[0] == nametofind:
        print(f"The name {student[0]}.")
        print(f"The grade {student[1]}.")
        avg = sum(student[1])/(len(student[1]))
        print(f"The avg is {avg}.")
        found = True
        break
if not found:
    print("The student does not exist.")

