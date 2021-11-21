##########################################################################
#Author: Nataly
#Date: 20.11.2021
#Task:
# write and test a function which takes three arguments (a year, a
# month, and a day of the month) and returns the corresponding day of the
# year, or returns None if any of the arguments is invalid.
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

def day_in_year(year, month, day):
    ''' Returns order number of day in year

Returns None if arguments don't have sense.'''

    days = days_in_month(year, month) # define number of days in month of year

    # init variable for sum of days in monthes by given day (argument of function)
    sum = day

    if days == None: # arguments don't have sense
        return None
    elif day < 1 or day > days:   # day number doesn't have sense   
        return None
    else:
        for i in range(1, month):
            sum += days_in_month(year, i)
        return sum


# define input data for testing
test_years = [2000, 2007, 2013]
test_months = [12, 11, 5]
test_days = [31, 12, 6]

# define data of results
test_results = [366, 316, 126]

# run test
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    d = test_days[i]
    print(yr, mo, d, "-> ", end="")
    result = day_in_year(yr, mo, d)
    print("result =", result)
    if result == test_results[i]:
        print("Ok")
    else:
        print("Failed")