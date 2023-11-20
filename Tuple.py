student = {
    "name" : "Timo",
    "age" : 20,
    "grade" : "A",
    "Courses" : ["Math", "Physics", "Programming"]
}

#accessing dictionary values:
print("Name: ", student["name"])
print("age: ", student["age"])
print("grade: ", student["grade"])
print("Courses: ", student["Courses"])

student['age'] = 25
student["Courses"].append("Language")

print(student)

student["city"] = "Espoo"
print(student)

#Iterating through the dic
for key, value in student.items():
    print(key + ":", value)

del student["grade"]
#check if a key exist
if "age" in student:
    print("Age: ", student["age"])
else:
    print("Age not found in the dictionary.")