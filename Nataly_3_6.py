""" program to make user guess magician's secret number
"""

# init secret number
secret_num = 777

# read user number
user_num = int(input("Enter an integer number: "))

# loop user attempts if he hasn't guessed the secret number
loop = True
while loop:
    if user_num != secret_num:
        print("Ha ha! You're stuck in my loop!")
        user_num = int(input("Enter an integer number: "))
    else:
        print("Well done, muggle! You are free now.") 
        loop = False        # finishing the loop