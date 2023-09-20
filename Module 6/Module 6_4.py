def sum_of_numbers(lst):
    total = 0
    for item in lst:
        total += item
    return total

lst = [1, 2, 3, 4, 5, 6]
print("The sum of these integers is:")
print(sum_of_numbers(lst))
