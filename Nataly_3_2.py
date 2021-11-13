""" program finds maximum and minimum of 10 numbers
"""
# read 10 numbers
print("Enter 10 numbers")
num1 = int(input("number1: "))
num2 = int(input("number2: "))
num3 = int(input("number3: "))
num4 = int(input("number4: "))
num5 = int(input("number5: "))
num6 = int(input("number6: "))
num7 = int(input("number7: "))
num8 = int(input("number8: "))
num9 = int(input("number9: "))
num10 = int(input("number10: "))

# find max of 10 numbers
max_num = max(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10)
print("Maximum of 10 numbers:", max_num)

# find min of 10 numbers
min_num = min(num1,num2,num3,num4,num5,num6,num7,num8,num9,num10)
print("Minimum of 10 numbers:", min_num)