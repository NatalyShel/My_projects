from sys import path
path.append("C:\\Users\\tillo\\git_proj\\My_projects\\ToDo_proj")

import json

#from Packages.ToDo_Class import ToDoTask
import Packages.ToDo_Class as TD

class MyTaskEncoder(json.JSONEncoder):
    def default(self, task):
        if isinstance(task, TD.ToDoTask):
            return task.__dict__
        else:
            #raise TypeError(task.__class__.__name__ + " not JSON serializable.")
            return super().default(self, task)

class MyTaskDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_task)

    def decode_task(self, task):
        return (TD.ToDoTask(**task))