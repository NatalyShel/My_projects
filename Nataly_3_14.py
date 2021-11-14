""" program to reset the 2d and 3d bits if they are 1
"""
# read binary data
a = input("Enter binary number: ")

# define mask for setting the second bit to 1
mask = int('00000110',2)

# apply mask to entered number
print("Result = ", bin(int(a,2) ^ mask))