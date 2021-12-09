##########################################################################
#Author: Nataly
#Date: 09.12.2021
#Task: Write a program that will simulate the recording of
# battery temperatures with an interval of one minute. 
# The simulation should contain 60 logs (the last hour).
# To simulate temperatures, use one of the available random
# functions in Python. Temperatures should be drawn in the 
# range of 20–40 degrees Celsius, and then saved in
# the following format:
# LEVEL_NAME - TEMPERATURE_IN_CELSIUS UNIT => DEBUG - 20 C
# The drawn temperatures should be assigned to the appropriate 
# level depending on their value
##########################################################################

# import package to deal with logger
import logging

# import BatterySimulation from Packages
import Packages.BatterySimulation as BS

# define FORMAT to use in formatter
FORMAT = '%(levelname)s - %(message)s'

# create logger
logger = logging.getLogger('battery.temperature')
logger.setLevel(logging.DEBUG)

# create handler
handler = logging.FileHandler('battery_temperature.log', mode='w')
handler.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

# set handler for created logger
logger.addHandler(handler)

# create object of class BatterySimulation
battery_simulation = BS.BatterySimulation(logger)

# call function to simulate battery temperature  changes 
# and add loggs to logger (which authomatically writes data into file)
battery_simulation.simulate_last_hour()