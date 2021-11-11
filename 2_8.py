""" simple calculator
    Operations: + - / * ** // %
"""
type_oper = input("Enter type of opertion (+ - / * ** // %): ")
x = int(input("Enter integer value for first value: x = "))

if type_oper == '/':
    y = int(input("Enter integer value for second value but not 0: y = "))
    while y == 0:
        y = int(input("Division by 0 not possible! Try again: y = "))
else:
    y = int(input("Enter integer value for second value: y = "))

if type_oper == '+':
    z = x + y
    print("x + y =", z)
elif type_oper == '-':
    z = x - y
    print("x - y =", z)
elif type_oper == '/':
    z = float(x / y)
    print("x / y =", round(z,2))
elif type_oper == '*':
    z = x * y
    print("x * y =", z)
elif type_oper == '**':
    z = x ** y
    print("x ** y =", z)
elif type_oper == '//':
    z = x // y
    print("x // y =", z)
elif type_oper == '%':
    z = x % y
    print("x %* y =", z)
