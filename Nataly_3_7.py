""" program that uses a
    for loop to "count mississippily" to five
"""
import time

# show a message of starting
print("I'm starting counting...")

# count 5 seconds ('Mississippi') in a loop
for i in range(5):
    print(i+1, " Mississippi")
    time.sleep(1)

# show a final message
print("Ready or not, here I come!")