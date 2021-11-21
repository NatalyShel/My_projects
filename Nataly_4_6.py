##########################################################################
#Author: Nataly
#Date: 21.11.2021
#Task:
# write a pair of functions converting liters/100km into 
# miles/gallons, and vice versa.
# 1 American mile = 1609.344 metres;
# 1 American gallon = 3.785411784 litres.
##########################################################################

def liters_100km_to_miles_gallone(liters):
    ''' Convert liters/100km into miles/gallons

One argument: integer or float (returns None if not number or <0)'''

    # define converting constants
    American_mile = 1609.344
    American_gallon = 3.785411784

    if liters < 0 or type(liters) not in [int, float]:
        return None     # argument doesn't have sense
    else:
        gall = liters / American_gallon
        miles = 100 * 1000 / American_mile
        return miles / gall

def miles_gallon_to_liters_100km(miles):
    ''' Convert miles/gallons into liters/100km 

One argument: integer or float (returns None if not number or <0)'''

    # define converting constants
    American_mile = 1609.344
    American_gallon = 3.785411784

    if miles < 0 or type(miles) not in [int, float]:
        return None     # argument doesn't have sense
    else:
        return 100*1000 * American_gallon / (miles * American_mile)


# run test
print(liters_100km_to_miles_gallone(3.9))
print(liters_100km_to_miles_gallone(7.5))
print(liters_100km_to_miles_gallone(10))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))