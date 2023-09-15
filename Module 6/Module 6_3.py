def gallontolitre(quantity):
    quantity = 3.78541 * quantity
    return quantity

while True:
    quantity = input("What is the quantity in gasoline?")
    try:
        quantity = float(quantity)
        if quantity >= 0:
            litre = gallontolitre(quantity)
            litre = round(litre, 3)
            print("The quantity is litre is", litre)
        else:
            break
    except ValueError:
        print("Please enter a number.")
print("Goodbye!")