"""
Author: Nataly
Date: 18.11.2021
Task: Write a program that reads two numbers aa and bb
from the keyboard, calculates and displays the arithmetic
mean of all numbers from the segment [a; b], which are
multiples of 3.
In the example below, the arithmetic mean is
calculated for numbers on the segment [-5; 12]. The total
number of numbers divisible by 3on this segment is 6: -
3, 0, 3, 6, 9, 12. Their arithmetic mean is 4.5
The program receives input to the intervals, within
which there is always at least one number that is divisible by 3.
"""

# promt user data
print("Enter interval (2 boundary numbers separated by space)", end=' ')
print("contains at least one number that is divisible by 3:")

while True:
    #transform input string of numbers separated by space into list of integer values
    numbers = [int(i) for i in input().split()]

    if len(numbers) < 2 or numbers[0] >= numbers[1]:
        print("Wrong input data. Try again!")
        continue
    else:
        break

# define list for numbers divisible by 3
div_by_3 = []

for i in range(numbers[0], numbers[1]+1):
    if i % 3 == 0:
        div_by_3.append(i)  # add number to list if it is divisible by 3

# print result
if len(div_by_3) == 0:
    print("There is no numbers divisible by 3!")
else:
    print("List of numbers divisible by 3 -->", div_by_3)
    # calculate arithmetic mean and print it
    print("Arithmetic mean of them:", sum(div_by_3) / len(div_by_3))    