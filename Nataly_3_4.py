"""
Author: Nataly
Date: 17.11.2021
Task: program to use commands: in / not in
Imagine a list -not very long, not very complicated, just a simple
list containing some integer numbers. Some of these numbers may
be repeated, and this is the clue. We don't want any repetitions.
We want them to be removed.
Your task is to write a program which removes all the number
repetitions from the list. The goal is to have a list in which all the
numbers appear not more than once.
"""

# define initial list
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# print initial list
print("Initial list:\n", my_list)

# define resulting list as empty
new_list = []

# add elements from initial list to new list if they not in it yet
for i in my_list:
    if i not in new_list:
        new_list.append(i)

# print resulting list
print("List with unique elements only:\n", new_list)