##########################################################################
#Author: Nataly
#Date: 08.12.2021
#Task: Create a class named TemperatureConverter and its
# convert_celsius_to_fahrenheitmethod which should convert temperature
# from Celsius to Fahrenheit. Use the following formula:
# F = 9/5 * C + 32
# Create a class named ForecastXmlParser and its parse method 
# responsible for reading data from forecast.xml.
# Use the TemperatureConverter class to convert temperature from
# Celsius to Fahrenheit (rounded to one decimal place). 
##########################################################################

# import Converter classes from Packages
import Packages.Converter_Classes as CL

# create object of class TemperatureConverter
temperature_converter = CL.TemperatureConverter()

# create object of class ForecastXmlParser and encapsulate
#  object temperature_converter into it
forecast_xml_parser = CL.ForecastXmlParser(temperature_converter)

# call method parse to read data from file and perform 
#  converting temperature
forecast_xml_parser.parse('forecast.xml')