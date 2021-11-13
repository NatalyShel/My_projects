""" program defines if entered year is leap or common
    * of the Gregorian calendar (since 1582)
"""

# read year
year = int(input("Enter year: "))

# define if year is Leap or Common
if year < 1582:     # not Gregorian calendar
    print("Not within the Gregorian calendar period")
elif (year % 4) != 0:      
    print("Common year")
elif (year % 100) != 0:
    print("Leap year")
elif (year % 400) != 0:      
    print("Common year")
else:
    print("Leap year")