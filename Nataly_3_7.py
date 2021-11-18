"""
Author: Nataly
Date: 18.11.2021
Task: program to calculate average.
"""

# promt user data
print("Enter string of numbers separated by space: ")

#transform input string of numbers separated by space into list of integer values
numbers = [int(i) for i in input().split()]

# define resulting variable
result =0

# calculate average of all nubmers
result = sum(numbers) / len(numbers)

# print result
print("Average of entered numbers =", result)