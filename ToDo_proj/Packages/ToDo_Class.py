from sys import path
path.append("C:\\Users\\tillo\\git_proj\\My_projects\\ToDo_proj")


import sqlite3

from Packages.ToDo_Exceptions import NameExc, PriorExc, IdExc
#from ToDo_Exceptions import NameExc, PriorExc, IdExc

class ToDo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()

        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    priority INTEGER NOT NULL
                    );''')

    def find_task(self, task_name = "", task_id = -1):
        if task_name == "" and task_id == -1:
            return None

        found = False

        que = '''SELECT id, name, priority FROM tasks;'''
        rows = self.c.execute(que)

        for row in rows:
            if row[0] == task_id or row[1] == task_name:
                found = True
                return row

        if not found:
            return None
    
    def add_task(self):
        name = input("Enter new task name: ")
        if len(name) == 0 or name.isspace():
            raise NameExc

        if self.find_task(task_name=name) != None:
            raise NameExc("task already exists in ToDo list")
        
        priority = int(input("Enter new task priority: "))
        if priority < 1:
            raise PriorExc
        
        self.c.execute('''INSERT INTO tasks (name, priority) VALUES (?,?)''',
                        (name, priority))
        self.conn.commit()

        print("Task added successfully!", end=' ')
    
    def delete_task(self):
        id = int(input("Enter task id to delete row: "))
        res = self.find_task(task_id=id)
        if id < 1 or res == None:
            raise IdExc
        
        self.c.execute('''DELETE FROM tasks WHERE id = ?;''', (id,))
        self.conn.commit()

        print("Task deleted successfully!", end=' ')
    
    def change_priority(self):
        priority = int(input("Enter new priority: "))
        if priority < 1:
            raise PriorExc

        id = int(input("Enter task id: "))
        if id < 1 or self.find_task(task_id=id) == None:
            raise IdExc
       
        self.c.execute('''UPDATE tasks SET priority = ? WHERE id = ?;''', 
                    (priority, id))
        self.conn.commit()

        print("Task priority changed successfully!", end=' ')
    
    def show_tasks(self):
        print("Current ToDo list:")
        print("Id     |     Task name     |    Priority")

        for row in self.c.execute('''SELECT * FROM tasks;'''):
            print(row[0], " \t", row[1], " \t", row[2])

    def exit(self):
        print("Exit from ToDo application. Good by!")
