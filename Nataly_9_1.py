##########################################################################
#Author: Nataly
#Date: 30.11.2021
#Task: implement the Queue class with  two basic operations:
# • put(element), which puts an element at end of the queue;
# • get(), which takes an element from the front of the queue 
# and returns it as the result (the queue cannot be empty to 
# successfully perform it.)
# Follow the hints:
# • use a list as your storage (just like we did in stack)
# • put() should append elements to the beginning of the list, 
# while get() should remove the elements from the list's end;
# • define a new exception named QueueError (choose an exception to 
# derive it from) and raise it when get() tries to operate on an empty list.
##########################################################################

class QueueError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class Queue:
    def __init__(self):
        self.__que = []     # init list variable for queue by empty list

    def put(self, val):     # put new element into queue
        self.__que.insert(0, val)
    
    def get(self):          # get element from queue
        if len(self.__que) == 0:
            raise QueueError("queue is empty!")
        else:
            val = self.__que[-1]
            del self.__que[-1]
            return val
        

# run test to check code above
que = Queue()   # create object of class Queue
# put 3 elements in queue
que.put(1)
que.put("Dog")
que.put(False)

# try to get and print 4 elements from queue
try:
    for i in range(4):
        print(que.get())
except QueueError as er:
    print("Queue error:", er)