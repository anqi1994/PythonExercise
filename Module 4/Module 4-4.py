import random

ans = random.randint(1, 10)
guess = input("Guess an integer between 1 and 10:\n")
while True:
    guess = int(guess)
    print(ans)
    while guess != ans:
        if guess < ans:
           print("Too low.")
        else:
           print("Too high")
        guess = int(input("Guess another integer between 1 and 10:\n"))
    if guess == ans:
        break
print("You are correct.")

#improved version

while True:
    guess = int(guess)
    ans = random.randint(1, 10)
    while True:
        if guess == ans:
            print("You are correct!")
            break
        elif guess > ans:(
            print("Too high."))
        else:
            print("Too low.")
        guess = int(input("Guess another integer between 1 and 10:\n"))
    time = input("Do you want to play again? (Enter yes or no)\n").lower()
    if time != "yes":
        break