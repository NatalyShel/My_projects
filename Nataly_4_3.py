##########################################################################
#Author: Nataly
#Date: 20.11.2021
#Task:
# write and test a function which takes two arguments (a year and a
# month) and returns the number of days for the given month/year
# pair (while only February is sensitive to the year value, 
# function should be universal).
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

def days_in_month(year, month):
    ''' Returns number of days in given month of given year

year >=1582, 1 <= month <= 12, integer
Returns None if arguments don't have sense.'''

    is_leap = is_leap_year(year) # call funtion to define if year is Leap

    # list with number of days in every month of Common year 
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap == None or month > 12 or month < 1: # arguments don't have sense
        return None
    elif month ==2 and is_leap == True:   # February in Leap year    
        return 29
    else:
        return days[month-1]


# define input data for testing
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]

# define data of results
test_results = [28, 29, 31, 30]

# run test
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "-> ", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("Ok")
    else:
        print("Failed")