"""
Author: Nataly
Date: 16.11.2021
Task: To sort list using "buble" method (in increased or reversed way)
"""
# read length of list for sorting
n = int(input("Enter length of list for sorting -> "))

# define empty list
my_list = []

# read numbers to add into list
print("Enter", n, "integer values to add into list.")
for i in range(n):
    my_list.append(int(input("--> ")))

# read type of sorting
while True:
    print("Enter 'i' to sort list in increased way or 'r' to sort in reversed way")
    sort_type = input()
    if sort_type == 'i' or sort_type == 'r':
        break
    else:
        print("Wrong entered data, try again!")

# print original list
print("Original list: ", my_list)

# define variable to use in sorting loop
swapped = True

# sort list according to selected type of sort
while swapped:
    swapped = False # no swap so far
    for i in range(len(my_list)-1):
        if ((sort_type == 'i' and my_list[i] > my_list[i+1]) or # increased sorting
            (sort_type == 'r' and my_list[i] < my_list[i+1])):  # reversed sorting
                swapped = True # swap occured!
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

# print resulted list
print("Sorted list: ", my_list)