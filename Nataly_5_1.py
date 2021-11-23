##########################################################################
#Author: Nataly
#Date: 21.11.2021
#Task:
# implement program to calculate factorial without recursion
# (return None if argument < 0)
##########################################################################

def factorial(n):
    ''' Calculate factorial

One argument: integer and >=0'''

    if n <0 or type(n) is not int:
        return None     # not proper argument
    elif n < 2:
        return 1
    else:
        factor_val = 1
        for i in range(2,n+1):
            factor_val *= i
        return factor_val


# run test: print factorial of numbers in range -1:9
for j in range(-1, 9):
    print(factorial(j))