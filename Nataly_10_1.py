##########################################################################
#Author: Nataly
#Date: 03.12.2021
#Task: write a program which:
# • asks user for input file name;
# • reads the file (if possible) and counts all the Latin letters
# (lower-and upper-case letters are treated as equal)
# • prints a simple histogram in alphabetical order (only non-zero
# counts should be presented)
# Create a test file for the code, and check if your histogram
# contains valid results.
##########################################################################

from os import strerror

srcname = input("Enter input file name: ")

# try to open and read file. if error -> print error number
try:
    src = open(srcname, 'rt')

    content = src.read()    # read all content from imput file into variable

    content = content.lower() # set all letters to lower case

    # init dictionary of latin leter counters
    counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

    # get one char from content
    for ch in content:
        # if char is latin letter -> increment its counter
        if ch.isalpha() and (ch in counters.keys()):
            counters[ch] +=1

    # print counters of letter from 'a' to 'z' excluding counters == 0
    for key in counters:
        if counters[key] != 0:
            print(key, "->", counters[key])

    # close input file
    src.close()
except IOError as e:
    print("I/O error occured", strerror(e.errno))