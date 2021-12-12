class NameExc(Exception):
    def __init__(self, head="TDTaskNameError", message="Invalid task name!"):
        super().__init__(message)
        self.head = head
        self.mess = message

class PriorExc(Exception):
    def __init__(self, head="TDTaskPriorityError", message="Invalid task priority!"):
        super().__init__(message)
        self.head = head
        self.mess = message

class IdExc(Exception):
    def __init__(self, head="TDTaskIdError", message="Invalid task id!"):
        super().__init__(message)
        self.head = head
        self.mess = message