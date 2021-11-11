"""
calculating y = 1/(x + 1/(x + 1/(x + 1/x)))
"""
x = int(input("Enter integer value: x = "))
while x == 0:
        x = int(input("Division by 0 not possible! Enter another value: x = "))
y = 1/(x + 1/(x + 1/(x + 1/x)))
print("y = 1/(x + 1/(x + 1/(x + 1/x))) =", y)