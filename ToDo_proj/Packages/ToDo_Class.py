from sys import path
path.append("C:\\Users\\tillo\\git_proj\\My_projects\\ToDo_proj")


import sqlite3
import json
from os import strerror

from Packages.ToDo_Exceptions import NameExc, PriorExc, IdExc
from Packages.JSON_coders import MyTaskEncoder, MyTaskDecoder
from Packages.EventLoger_Class import EventLogger
# import package to deal with logger
import logging


class ToDoTask:
    def __init__(self, id, name, priority):
        self.id = id
        self.name = name
        self.priority = priority


class ToDo:
    def __init__(self):
        self.logger = (EventLogger('todo')).get_logger()

        self.conn = sqlite3.connect(path[-1] + '\\Sources\\todo.db')
        self.logger.debug('Connection to todo.db established.')
        self.c = self.conn.cursor()

        rc = self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    priority INTEGER NOT NULL
                    );''')
        
        if rc == 0:
            self.logger.debug('Table tasks created.')


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
            self.logger.warning('Invalid task name!')
            raise NameExc

        if self.find_task(task_name=name) != None:
            self.logger.warning('Task already exists!')
            raise NameExc("Task already exists in ToDo list")
        
        priority = int(input("Enter new task priority: "))
        if priority < 1:
            self.logger.warning('Invalid task priority!')
            raise PriorExc
        
        self.c.execute('''INSERT INTO tasks (name, priority) VALUES (?,?)''',
                        (name, priority))
        self.conn.commit()

        self.logger.debug("New task added: \'{0}\'.".format(name))
        
        print("Task added successfully!", end=' ')
    
    def delete_task(self):
        id = int(input("Enter task id to delete row: "))
        res = self.find_task(task_id=id)
        if id < 1 or res == None:
            self.logger.warning('Invalid task id!')
            raise IdExc
                 
        self.c.execute('''DELETE FROM tasks WHERE id = ?;''', (id,))
        self.conn.commit()

        self.logger.debug('Task with id={0} deleted.'.format(id))

        print("Task deleted successfully!", end=' ')
    
    def change_priority(self):
        priority = int(input("Enter new priority: "))
        if priority < 1:
            self.logger.warning('Invalid task priority!')
            raise PriorExc

        id = int(input("Enter task id: "))
        res = self.find_task(task_id=id)
        if id < 1 or res == None:
            self.logger.warning('Invalid task id!')
            raise IdExc
       
        self.c.execute('''UPDATE tasks SET priority = ? WHERE id = ?;''', 
                    (priority, id))
        self.conn.commit()

        self.logger.debug('Task priority for id={0} changed to -> {1}.'\
            .format(id, priority))

        print("Task priority changed successfully!", end=' ')
    
    def select_all_tasks(self): # return list with all task objects
        tasks = []
        for row in self.c.execute('''SELECT * FROM tasks;'''):
            tasks.append(ToDoTask(row[0], row[1], row[2]))
        return tasks
        
    def show_tasks(self):
        print("Current ToDo list:")
        print('-'*70)
        print("Id".ljust(4), '|', "Task name".ljust(40), "|", "Priority".ljust(8))
        print('-'*70)

        for task in self.select_all_tasks(): #
            print(str(task.id).ljust(6), task.name.ljust(42),
                 str(task.priority).ljust(10))
    
    def transform_ToDo_to_json(self):
        file = path[-1] + '\\Sources\\todo.json'
        try:
            src = open(file, 'wt')
            for task in self.select_all_tasks():
                json_str = json.dumps(task, cls = MyTaskEncoder)
                src.write(json_str + '\n')
            src.close()
        except IOError as e:
            print(e)
            self.logger.critical(e) # add critical message to evens logger
        else:
            self.logger.debug('Tasks transformed to JSON successfully!')
            print("Tasks transformed to JSON successfully!")
    
    def transform_json_to_ToDo(self):
        file = path[-1] + '\\Sources\\todo.json'
        try:
            src = open(file, 'rt')
            json_str = src.readline()
            #tasks = self.select_all_tasks()
            while json_str != '':
                read_task = json.loads(json_str, cls=MyTaskDecoder)
                res = self.find_task(task_id=read_task.id)
                if res == None:
                    self.c.execute('''INSERT INTO tasks (id, name, priority)
                        VALUES (?,?,?)''',
                        (read_task.id, read_task.name, read_task.priority))
                    self.conn.commit()
                elif res[1] != read_task.name or res[2] != read_task.priority:
                    self.c.execute('''UPDATE tasks SET name = ?, priority = ?
                        WHERE id = ?;''',
                        (read_task.name, read_task.priority, read_task.id))
                    self.conn.commit()
                json_str = src.readline()
            src.close()
        except IOError as e:
            self.logger.critical(e) # add critical message to evens logger
            print(e)
        else:
            self.logger.debug('ToDo updated from JSON successfully!')
            print("JSON transformed to Tasks (ToDo updated) successfully!")
            self.show_tasks()

    def exit(self):
        self.conn.close()
        self.logger.debug('Exit from ToDo application, connection closed.')
        print("Exit from ToDo application. Good by!")
