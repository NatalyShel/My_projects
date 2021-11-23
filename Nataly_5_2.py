##########################################################################
#Author: Nataly
#Date: 23.11.2021
#Task:
# implement program to calculate Fibonacci numbers:
# Fib_1 = 1
# Fib_2 = 1
# Fib_3 = Fib_1 + Fib_2
# ...
# (return None if argument < 1)
##########################################################################

def fib(n):
    ''' Calculate Fibonacci numbers

One argument: integer and >=1'''

    if n < 1:
        return None     # not proper argument
    elif n < 3:
        return 1
    else:
        fib_1 = fib_2 = 1   # init 2 first Fibinacci nubmers
        f_sum = 0
        for i in range(3,n+1):
            f_sum = fib_1 + fib_2
            fib_1, fib_2 = fib_2, f_sum
        return f_sum


# init run vairable for asking user input in loop until it is integer
run = True

while run:
    # ask user to enter end number of sequence
    str = input("Enter end number of sequence: ")

    try:
        n = int(str)
    except:
        print("Input value not integer. Try again!")
        continue

    run = False

# calculate and print Fibonacci numbers from -1 to n (including)
for i in range(-1, n+1):
    print(i, "->", fib(i))