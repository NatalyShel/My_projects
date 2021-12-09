# import package to work with xml format
import xml.etree.ElementTree as ET

class TemperatureConverter:
    # convert temperature from Celsius to Fahrenheit
    def convert_celsius_to_fahrenheit(self, temperature_in_celsius):
        return 9.0/5.0 * temperature_in_celsius +32

class ForecastXmlParser:
    def __init__(self, temperature_converter):
        self.temperature_converter = temperature_converter
    
    def parse(self, file):
        tree = ET.parse(file)   # get data from file and put it to tree
        root = tree.getroot()   # get root element from data tree
        # get child elements in loop
        for child in root:
            day = child.find('day').text
            temperature_in_celsius = int(child.find(
                'temperature_in_celsius').text)
            # calculate temperature in Fahrenheit
            temperature_in_fahrenheit = round(
                self.temperature_converter.convert_celsius_to_fahrenheit(
                    temperature_in_celsius),1)
            print('{0}: {1} Celsius, {2} Fahrenheit'.format(
                day, temperature_in_celsius, temperature_in_fahrenheit))