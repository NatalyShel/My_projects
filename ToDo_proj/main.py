from sys import path
path.append("C:\\Users\\tillo\\git_proj\\My_projects\\ToDo_proj")

# import my packages
from Packages.ToDo_Class import ToDo
from Packages.ToDo_Exceptions import NameExc, PriorExc, IdExc

def menu_controller(put = 0):
    if put == 5:
        app.exit()
    elif put == 1:
        app.show_tasks()
    else:
        try:
            if put == 2:
                app.add_task()
            elif put == 3:
                app.change_priority()
            elif put == 4:
                app.delete_task()
            else:
                print("Invalid operation number!")
        except NameError as ne:
            print(ne)
        except PriorExc as pe:
            print(pe)
        except IdExc as ie:
            print(ie)
        except:
            print("Something goes badly!")
        else:
            print(":-)")


app = ToDo()

run = True

while run:
    print('''
    1. Show all tasks in ToDo list
    2. Add task
    3. Change priority
    4. Delete task
    5. Exit
    ''')

    try:
        put = int(input("Put number from menu above (1 or 2 or 3 or 4 or 5): "))
        if put == 5:
            run =False
        menu_controller(put)
    except:
        print("Smth has gone badly!")