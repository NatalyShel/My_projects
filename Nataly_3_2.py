"""
Author: Nataly
Date: 15.11.2021
Task:
Write a program that reflects these changes and lets you practice with
the concept of lists. Your task is to:
step 1: create an empty list named beatles;
step 2: use the append()method to add the following members of the
band to the list: John Lennon, Paul McCartney, and George Harrison;
step 3: use the forloop and the append()method to prompt the user to
addthe following members of the band to the list: Stu Sutcliffe, and Pete
Best; input()
step 4: use thedelinstruction to remove Stu Sutcliffeand Pete Bestfrom
the list;
step 5: use the insert()method to addRingo Starr to the beginningof the
list.
"""
# create an empty list
beatles = []

# show inotial staff of the group
print("initial beatles = ", beatles)

# add some members to the group
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')

# show current staff of the group
print("added 3 people to beatles = ", beatles)

#  prompt user to add 2 more members (Stu Sutcliffe and Pete Best)
new_members = ['Stu Sutcliffe',  'Pete Best']
for member in new_members:
    print("Enter next member name: (", member, ") -->")
    beatles.append(input())

# show current staff of the group
print("added 2 people to beatles = ", beatles)

# use the del instruction to remove Stu Sutcliffe and Pete Best from the list
del beatles[-1]
del beatles[-1]

# show current staff of the group
print("removed 2 latest people from beatles = ", beatles)

# use the insert()method to add Ringo Starr to the beginning of the list
beatles.insert(0,'Ringo Starr')

# show current staff of the group
print("added new member into first place of beatles = ", beatles)