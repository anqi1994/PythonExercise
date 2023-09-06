gen = input("Please enter your biological gender (female or male):\n")
hemva = float(input("Please enter your hemoglobin value (g/l):\n"))
if gen == "female":
    if hemva < 117:
        print("Your hemoglobin value is low.")
    elif hemva >= 117 and hemva <= 155:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
elif gen == "male":
    if hemva < 134:
        print("Your hemoglobin value is low.")
    elif hemva >= 134 and hemva <= 167:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
else:
    print("Invalid Value")
