##########################################################################
#Author: Nataly
#Date: 19.11.2021
#Task:
# write and test a function which takes one argument (a year) and
# returns True if year is a leap year, or False otherwise.

# The code uses two lists - one with the
# test data, and the other containing the
# expected results. The code will tell you if
# any of your results are invalid.
##########################################################################

def is_leap_year(year):
    ''' Define if year is Leap or Common

Argument >=1582, integer
Returns True if year is Leap, otherwise - False.'''

    if year < 1582:     # not Gregorian calendar
        print("Not within the Gregorian calendar period")
        return None
    elif (year % 4) != 0:   # year is Leap    
        return False        # Common year
    elif (year % 100) != 0:
        return True
    elif (year % 400) != 0:      
        return False        # Common year
    else:
        return True         # year is Leap

# define input data for testing
test_data = [1900, 2000, 2016, 1987]

# define data of results
test_results = [False, True, True, False]

# run test
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "-> ", end="")
    result = is_leap_year(yr)
    if result == test_results[i]:
        print("Ok")
    else:
        print("Failed")