########################################################################## 
#Author: Nataly
#Date: 19.11.2021
#Task:
# Implement the calculator using your own functions.
# while, exit by put "exit"
# Set of operations:
# +, -, /, *, %, //, **, odd/even, type(), max/min, avg
##########################################################################

# define calculating functions

def plus(a,b):
    print(a, "+", b, "=", a + b)

def minus(a,b):
    print(a, "-", b, "=", a - b)

# show message if argument = 0
def zero_div(x):
    if x == 0:
        print("Division by zero not allowed!")
        return True
    else:
        return False

def div(a,b):
    if not zero_div(b):
        print(a, "/", b, "=", a / b)

def mult(a,b):
    print(a, "*", b, "=", a * b)

def int_div(a,b):
    if not zero_div(b):
        print(a, "//", b, "=", a // b)

def rest_of_div(a,b):
    if not zero_div(b):
        print(a, "%", b, "=", a % b)

def exp(a,b):
    print(a, "**", b, "=", a ** b)

def odd(a):
    if a % 2 == 1:      # if argument is odd
        print(a, "is odd")
    else:
        print(a, "is not odd")

def even(a):
    if a % 2 == 0:      # if argument is even
        print(a, "is even")
    else:
        print(a, "is not even")

def type_fun(a):
    print("type(a)=", type(a))

# find maximum in list of nubmers
def max_fun(lst = []):
    m = -99999999999999
    for i in lst:
        if i > m:
            m = i
    print("max(", lst, ") =", m)

# find minimum in list of nubmers
def min_fun(lst = []):
    m = 99999999999999
    for i in lst:
        if i < m:
            m = i
    print("min(", lst, ") =", m)

# calculate average of list of nubmers
def avg(lst = []):
    print("avg(", lst, ") =", sum(lst) / len(lst))


# read input data and calculate in a loop, exit by 'exit' word
while True:
    print("Enter type of operation: + - / * // % **")
    print("                         odd even type max min avg ")
    print("Or enter 'exit' to leave the loop")

    operation = input()

    if operation not in ['exit', '+', '-', '/', '*', '%', '//', '**', 
                        'odd', 'even', 'type', 'max', 'min', 'avg']:
        print("entered operator not defined in program")
        continue

    if operation == 'exit': # leave the loop if 'exit' word entered
        print("Good bye!")
        break
    elif operation in ['max','min','avg']:
        print("Enter string of numbers separated by space: ")
        numbers = [float(i) for i in input().split()]
        if operation == 'max':
            max_fun(numbers)
        elif operation == 'min':
            min_fun(numbers)
        elif operation == 'avg':
            avg(numbers)
    else:
        x = input("Enter argument: a = ")
        if operation == 'type':
            type_fun(x)
        elif operation == 'odd':
            odd(int(x))
        elif operation == 'even':
            even(int(x))
        else:
            a = float(x)
            b = float(input("Enter second argument: b = "))
            
            if operation == '+':
                plus(a,b)
            elif operation == '-':
                minus(a,b)
            elif operation == '/':
                div(a,b)
            elif operation == '*':
                mult(a,b)
            elif operation == '//':
                int_div(a,b)
            elif operation == '%':
                rest_of_div(a,b)
            elif operation == '**':
                exp(a,b)