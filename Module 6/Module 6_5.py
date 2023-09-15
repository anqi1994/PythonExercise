def even_number_lst(lst):
    evenlst = []
    for item in lst:
        if item % 2 == 0:
            evenlst.append(item)
    return evenlst

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("The original list is:")
print(lst)

print("The cut_down list is:")
print(even_number_lst(lst))