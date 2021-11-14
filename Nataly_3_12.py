""" Calculator
    Operations: + - / * ** // % and or not
                type() round() max() min()
    ***!?! operations 'and','or','not' work incoreclty for now
"""

# read input data and calculate in a loop, exit by 'exit' word

while True:
    print("Enter type of operation: + - / * ** // %")
    print("                         and or not type round max min ")
    print("Or enter 'exit' word to leave the loop")

    operation = input()

    if operation == 'exit': # leave the loop if 'exit' word entered
        print("Good bye!")
        break

    x1 = input("Enter value: x1 = ")

    if operation == 'type':
        print("type(x1) = ", type(x1))
    elif operation == 'not':
        print("not x1 = ", not bool(x1))
    elif operation in ['+','-','/','*','**','//','%','and','or','max','min','round']:
        x2 = input("Enter second value: x2 = ")
        if operation == '+':
            print("x1 + x2 = ", float(x1) + float(x2))
        elif operation == '-':
            print("x1 - x2 = ", float(x1) - float(x2))
        elif operation in ['/','//','%']:
            while float(x2) == float(0):
                x2 = input("Enter second value but not 0: x2 = ")
            if operation == '/':
                print("x1 / x2 = ", float(x1) / float(x2))
            elif operation == '//':
                print("x1 // x2 = ", float(x1) // float(x2))
            elif operation == '%':
                print("x1 % " + "x2 = ", float(x1) % float(x2))
        elif operation == '*':
            print("x1 * x2 = ", float(x1) * float(x2))
        elif operation == '**':
            print("x1 ** x2 = ", float(x1) ** float(x2))
        elif operation == 'max':
            print("max(x1, x2) = ", max(float(x1), float(x2)))
        elif operation == 'min':
            print("min(x1, x2) = ", min(float(x1), float(x2)))
        elif operation == 'and':
            print("x1 and x2 = ", bool(x1) and bool(x2))
        elif operation == 'or':
            print("x1 or x2 = ", bool(x1) or bool(x2))        
        elif operation == 'round':
            print("round(x1, x2) = ", round(float(x1),int(x2)))
        else:
            print("entered operator not defined in program")
    else:
        print("Operation not defined!")