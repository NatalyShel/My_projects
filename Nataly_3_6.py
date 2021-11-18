"""
Author: Nataly
Date: 17.11.2021
Task: program that takes as input a list of
numbers on one line and displays on one line the
values ??that appear more than once in it.
"""

# promt user data
print("Enter string of numbers separated by space: ")

#transform input string of numbers separated by space into list of integer values
numbers = [int(i) for i in input().split()]

# sort list of numbers
numbers.sort()

# define new temporary list and resulting list
temp = []
result =[]

for i in numbers:
    if i not in temp:
        temp.append(i)  # add number to temp if it is met for first time
    else:
        if i not in result:
            result.append(i) # otherwise add number to result if not in it already
            print(i, end=' ') # print result list in one line