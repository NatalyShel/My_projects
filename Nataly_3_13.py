""" program to set the 2d bit if not 1
"""
# read binary data
a = input("Enter binary number: ")

# define mask for setting the second bit to 1
mask = int('00000010',2)

# apply mask to entered number
print("Result = ", bin(int(a,2) | mask))