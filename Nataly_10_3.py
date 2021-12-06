##########################################################################
#Author: Nataly
#Date: 04.12.2021
#Task: write a program which:
# • asks user for input file name;
# • reads the file (if possible) and counts the sum of the received
#  points for each student;
# • prints a simple (but sorted) report
# Note:
# • your program must be fully protected against all possible
#  failures: the file's non-existence, the file's emptiness, or
#  any input data failures;
# encountering any data error should cause immediate program
#  termination, and the erroneous should be presented to the user;
# • implement and use your own exceptions hierarchy - we've presented
#  it in the editor; the second exception should be raised when
# a bad line is detect, and the third when the source file exists but is empty.
# Tip: Use a dictionary to store the students' data.
##########################################################################

class StudetsDataException(Exception):
    #def __init__(self, student = "unknown", message = ''):
    def __init__(self, message = ''):
        Exception.__init__(self, message)
        #self.student = student

class BadLine(StudetsDataException):
    def __init__(self, line_number = 0):
        message = "Line with number " + str(line_number) + " not valid."
        StudetsDataException.__init__(self, message)

class FileEmpty(StudetsDataException):
    def __init__(self, file_name):
        message = "File \'" + file_name + "\' is empty."
        StudetsDataException.__init__(self, message)

from os import strerror

srcname = input("Enter input file name: ")

# try to open file. if error -> print error number and exit
try:
    src = open(srcname, 'rt')

    line = src.readline()   # read line from imput file
    dict_students = {}
    line_count = 0
    if line == '':
        raise FileEmpty(srcname)
    else:
        while line != '':
            line_count += 1
            line = line.strip()
            lst = line.split()
            if len(lst) != 3:
                raise BadLine(line_count)
            try:
                mark = float(lst[2])
            except:
                raise BadLine(line_count)
            stu_name = lst[0] + ' ' + lst [1]
            if stu_name not in dict_students.keys():
                dict_students[stu_name] = mark
            else:
                dict_students[stu_name] += mark
            line = src.readline()   # read line from imput file
    
    for key in dict_students.keys():
        print(key, '\t', dict_students[key])

    src.close()    
except FileEmpty as fe:
    print(fe)
except BadLine as bl:
    print(bl)
except IOError as e:
    print("I/O error occured", strerror(e.errno))