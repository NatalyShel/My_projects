########################################################################## 
#Author: Nataly
#Date: 24.11.2021
#Task:
# program that, at the user's request:
# • Defines your python version
# • Determines the capacity of the system(32/64)
# • Defines the processor
# • And everything that interests you
# • In response, the program issues comments, for example,
#  if you have Linux - 'Wow, you makin' a hacker! ' Etc.
# • By entering the word exit - the program is interrupted.
##########################################################################

from platform import python_version_tuple, machine, processor, system, platform

# read input data in a loop, exit by 'exit' word
while True:
    print("Enter your choice:")
    print("1 - to define your python version")
    print("2 - to define the capacity of the system")
    print("3 - to define the processor")
    print("4 - to define the system")
    print("5 - to define the platform")
    print("'exit' - to stop the program")

    operation = input()
    
    if operation.isalpha():
        operation = operation.lower() # transform to lower case

    if operation not in ['1', '2', '3', '4', '5', 'exit']:
        print("Entered operation not defined in program. Try again!")
        continue

    if operation == 'exit': # leave the loop if 'exit' word entered
        print("Good bye!")
        break
    elif operation == '1':
        print("Python version --> ", end="")
        for atr in python_version_tuple():
            print(atr, end=".")
        print()
    elif operation == '2':
        print("The capacity of the system --> ", machine())
    elif operation == '3':
        print("The processor --> ", processor())
    elif operation == '4':
        print("The system --> ", system())
    elif operation == '5':
        print("The platform --> ", platform())