username = "python"
password = "rules"
attn = 0
while True:
    attu = input("What is your username?\n")
    attp = input("What is your password?\n")
    attn += 1
    if attu != username or attp != password:
        if attn < 5:
            print("The username of password is not correct, please try again.")
        else:
            print("Access denied.")
            break
    else:
        print("Welcome!")
        break

