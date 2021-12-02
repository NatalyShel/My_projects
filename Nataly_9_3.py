##########################################################################
#Author: Nataly
#Date: 02.12.2021
#Task: implement a class called Weeker. objects of that class will be 
# able to store and to manipulate days of a week.
# The class constructor accepts one argument - a string. The string
#  represents the name of the day of the week and the only acceptable
# values must come from the following set: Mon Tue Wed Thu Fri Sat Sun
# Invoking the constructor with an argument from outside this set 
# should raise the WeekDayError exception. The class should provide 
# the following facilities:
# • objects of the class should be "printable", i.e. they should be
#  able to implicitly convert themselves into strings of the same
#  form as the constructor arguments;
# • the class should be equipped with one-parameter methods called
#  add_days(n) and subtract_days(n), with n being an integer number
#  and updating the day of week stored inside the object in the way
# reflecting the change of date by the indicated number of days, 
# forward or backward.
# • all object's properties should be private;
##########################################################################

class WeekDayError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class Weeker:
    def __init__(self, day = "Mon"):
        # init list of Days (acceptable values)
        self.__days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        # check if argument is acceplable
        if day not in self.__days:
            raise WeekDayError("Value of day not acceptable!")
        else:
            for i in range(len(self.__days)):
                if day == self.__days[i]:
                    self.__day_index = i    # save index of day in week list

    def __str__(self):     # convert object into string (to be printable)
        return self.__days[self.__day_index]
    
    def add_days(self, n):  # change day forward by n number of days
        if n <= 0 or type(n) is not int:
            raise ValueError("Argument must be integer and > 0!")
        else:
            self.__day_index = (self.__day_index + n) % 7
    
    def subtract_days(self, n):  # change day backward by n number of days
        if n <= 0 or type(n) is not int:
            raise ValueError("Argument must be integer and > 0!")
        else:
            self.__day_index = (self.__day_index - n) % 7


# run test
try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print("Add 15 days ->", weekday)
    weekday.subtract_days(23)
    print("Subtract 23 days ->", weekday)
    weekday = Weeker('Monday')
except WeekDayError as wde:
    print(wde)
except ValueError as ve:
    print(ve)

