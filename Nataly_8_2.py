##########################################################################
#Author: Nataly
#Date: 30.11.2021
#Task: The class itself should provide the following facilities:
# • objects of the class should be "printable", i.e. they should 
# be able to implicitly convert themselves into strings of the 
# following form: "hh:mm:ss", with leading zeros added when any 
# of the values is less than 10;
# • the class should be equipped with parameterless methods 
# called next_second() and previous_second(), incrementing the
#  time stored inside objects by +1/-1 second respectively.
# Use the following hints:
# • all object's properties should be private;
# • consider writing a separate function (not method!) to
# format the time string.
##########################################################################

class Timer:
    def __init__(self, hours = 0, min = 0, sec = 0 ):
        self.__hours = hours
        self.__min = min
        self.__sec = sec


    def __str__(self):
        def two_digits(val):  # add '0' at the left if val contains only 1 digit
            s = str(val)
            if len(s) == 1:
                s = '0' + s
            return s

        s1 = two_digits(self.__hours) + ":"\
            + two_digits(self.__min) + ":"\
            + two_digits(self.__sec)
        return s1
    
    def next_second(self):
        if self.__sec == 59:
            self.__sec = 0
            if self.__min == 59:
                self.__min = 0
                if self.__hours == 23:
                    self.__hours = 0
                else:
                    self.__hours += 1
            else:
                self.__min += 1
        else:
            self.__sec += 1
    
    def prev_second(self):
        if self.__sec == 00:
            self.__sec = 59
            if self.__min == 00:
                self.__min = 59
                if self.__hours == 00:
                    self.__hours = 23
                else:
                    self.__hours -= 1
            else:
                self.__min -= 1
        else:
            self.__sec -= 1


# run test
timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)