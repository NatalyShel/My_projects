""" program works with a list
"""
# define original list
hat_list = [1, 2, 3, 4, 5]

# print all elements of the list
print("Original list: ", hat_list)

# print list length
print("Original list length = ", len(hat_list))

# prompt user to enter data
new_value = int(input("Enter an integer number: "))

# replace the middle number in the list with entered data
hat_list[len(hat_list)//2] = new_value

# remove the last element from the list
del hat_list[-1]

# print all elements of the updated list
print("Updated list: ", hat_list)

# print  updated list length
print("Updated list length = ", len(hat_list))