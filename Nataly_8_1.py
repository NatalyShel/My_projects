##########################################################################
#Author: Nataly
#Date: 29.11.2021
#Task: extend the Stack class behavior in such a way so that
#  the class is able to count all the elements that are pushed
#  and popped (I assume that counting pops is enough). 
# Follow the hints:
# • introduce a property designed to count pop operations and 
# name it in a way which guarantees hiding it;
# • initialize it to zero inside the constructor;
# • provide a method which returns the value currently assigned
#  to the counter (name it get_counter()).
##########################################################################

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)
    
    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)    # call init for superclass
        self.__counter = 0  # defint private variable and init it by 0

    def get_counter(self):  # method to get value of private variable
        return self.__counter
    
    def pop(self):
        val = Stack.pop(self)
        self.__counter += 1     # increment counter
        return val


# run test to check code above
stk = CountingStack()   # create object of class CountingStack

for i in range(100):
    stk.push(i)     # add (push) new value into stack
    stk.pop()       # delete last added value

# print counter which calculated how many pops occured in stack object
print(stk.get_counter())