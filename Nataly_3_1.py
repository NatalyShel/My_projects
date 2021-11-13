""" program finds the largest of four
    numbers
"""
# read 4 numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

# find the largest number

# init larger_num by the first number for beginning (in case they are equal)
larger_num = num1
if (num1 > num2) & (num1 > num3) & (num1 > num4):
    larger_num = num1
elif (num2 > num3) & (num2 > num4):
    larger_num = num2
elif num3 > num4:
    larger_num = num3
elif num4 > num1:
    larger_num = num4
else:
    print("all numbers are equal")
    exit()

print("Larger number =", larger_num)