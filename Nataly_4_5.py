##########################################################################
#Author: Nataly
#Date: 21.11.2021
#Task:
# write and test a function called is_prime which takes one argument
# and returns True if the argument is a prime number, and False otherwise.
# (Prime numbers are divisible only by the number 1 or itself)
##########################################################################

def is_prime(num):
    ''' Define if number is Prime

Argument >1, integer (returns None if not int or <=1)
Returns True if number is Prime, otherwise - False.'''

    if num <=1 or type(num) != int:
        print("Argument of function must be integer and >1 !")
        return None
    else:
        for i in range(2,num):
            if num % i  == 0:   # number is divisible not only by 1 and itself
                return False
        return True             # number is Prime


# run test: print Prime numbers in range 1:19
for i in range (1, 20):
    if is_prime(i+1):
        print(i+1, end=" ")
print()