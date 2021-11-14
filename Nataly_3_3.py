""" program wants 'Spathiphyllum' to be entered"""

# get string by input
str = input("Enter name of the best home plant please: ")

# remove spaces by method 'strip' 
str1 = str.strip()

# perform  the concept of conditional execution
if str1 == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif str1 == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", str1, "!")