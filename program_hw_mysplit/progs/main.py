##########################################################################
#Author: Nataly
#Date: 26.11.2021
#Task: write and test own function similar to 'split()'
##########################################################################

from sys import path
path.append("C:\\Users\\tillo\\git_proj\\My_projects\\program_hw_mysplit")

# import my function
from packages.mysplit.mysplit1 import mysplit
 

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))