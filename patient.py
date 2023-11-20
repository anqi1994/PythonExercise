first = ("Qi", "An", 28, "Flu")
def information(patient):
    first_name, last_name, age, symptoms = patient
    formatted_info = f"Name: {first_name} {last_name}, Age: {age}, Symptoms: {symptoms}"
    return formatted_info

patientinfo = information(first)
print(patientinfo)

second = ("Harry", "Potter", 2, "Flu")
third = ("Ron", "Wesley", 3, "Flu")
forth = ("Jack", "White", 4, "Flu")
fifth = ("Rose", "Green", 5, "Flu")
patient = []
patient.append(first)
patient.append(second)
patient.append(third)
patient.append(forth)
patient.append(fifth)
for index, item in enumerate(patient[:3]):
    a = information(item)
    #a = a.split()
    print(index+1, a)


def checkpatient(name):
    for individual in patient:
        if individual[0] == name:
            print(information(individual))
            return
    print('not exist')
    return

checkpatient(input("Enter the first name of the patient:\n"))

doctor = {"Title": "jr.",
          "Name":"John Watson",
          "EmploymentYear": "1900"
}

print(doctor)
doctor["Gender"] = "Male"

print(doctor)

def docdetail(doctor):
    title = doctor["Title"]
    name = doctor["Name"]
    year = doctor["EmploymentYear"]
    Gender = doctor["Gender"]
    formatted_doc = f"Title: {title}, Name: {name}, EmploymentYear: {year}, Gender:{Gender}"
    return formatted_doc

print(docdetail(doctor))