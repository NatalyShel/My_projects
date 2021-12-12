from sys import path
path.append("C:\\Users\\tillo\\git_proj\\My_projects\\ToDo_proj")

# import package to deal with logger
import logging

class EventLogger:
    def __init__(self, class_name = ""):

        # define FORMAT to use in formatter
        FORMAT = '%(levelname)s - %(message)s'

        # create logger
        self.logger = logging.getLogger(class_name + '.events')
        self.logger.setLevel(logging.DEBUG)

        # create handler
        self.handler = logging.FileHandler(path[-1] +
            '\\Sources\\' + class_name + '_events.log', mode='w')
        self.handler.setLevel(logging.DEBUG)

        # create formatter
        self.formatter = logging.Formatter(FORMAT)
        self.handler.setFormatter(self.formatter)

        # set handler for created logger
        self.logger.addHandler(self.handler)
    
    def get_logger(self):
        return self.logger