"""
Author: Nataly
Date: 17.11.2021
Task: program that accepts one line(string) of integers as input.  
Output -> sum of these numbers.
"""

# read user data
s = input("Enter string of numbers separated by space: ")

# split nubmers into list
li1 = s.split(" ")
print("input data after split:",li1)

# define new empty list
numbers = []

# modify elements from characters into integer and add in new list
for ch in li1:
    numbers.append(int(ch))

# print list of numbers
print("integer values after append in list:",numbers)

# calculate sum of numbers
print("Sum of numbers =",sum(numbers))