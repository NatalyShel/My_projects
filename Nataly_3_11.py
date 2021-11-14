""" program to implement Lothar Collatz hypothesis
"""
# read number
while True:
    c0 = int(input("Enter any non-negative and non-zero integer number: "))
    if c0 > 0:
        break

# define counter of steps
steps = 0 

while c0 != 1:
    steps +=1           # increment counter
    if c0 % 2 == 0:     # if c0 is even
        c0 /= 2
    else:               # if c0 is odd
        c0 = 3 * c0 +1
    print(int(c0))

# print value of counter        
print("steps = ", steps)