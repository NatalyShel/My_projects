##########################################################################
#Author: Nataly
#Date: 05.12.2021
#Task:
# • create class Pizza
# • list of pizza - private in constructor
# • write method like make_a_pizza
##########################################################################

from os import strerror

class PizzaError(Exception):    # exception if pizza not on menu
    def __init__(self, pizza = "unknown", message = ''):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):   # exception if too much cheese ordered
    def __init__(self, pizza = "unknown", cheese = '>100', message = ''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


class Pizza():
    # define and init menu of pizzas
    list_of_pizzas = ['calzone', 'margerita', 'verde', 'romana']
    def __init__(self):
        pass
    
    def add_pizza(self, pizza):
        # check if pizza exists on menu
        if pizza in self.list_of_pizzas:
            raise PizzaError(pizza, "already presents in list of pizzas")
        else:
            self.list_of_pizzas.append(pizza)
            print(pizza, ": successfully added to list of pizzas")
            print("List of pizzas", self.list_of_pizzas)
    
    def remove_pizza(self, pizza):
        # check if pizza exists on menu
        if pizza not in self.list_of_pizzas:
            raise PizzaError(pizza, "pizza not exist!")
        else:
            self.list_of_pizzas.remove(pizza)
            print(pizza, ": successfully removed from list of pizzas")
            print("List of pizzas", self.list_of_pizzas)


class Order(Pizza):
    def __init__(self):
        super().__init__()
        self.orders = {}    # init dictionary of pizzas in order
        self.counter = 1    # init counter of pizzas in order
        self.message = ""   # init message to print into file and console
        self.__fo = open('pizza_order.txt', 'wt')   # new file for order created
        self.__fo.close()

    def make_piza(self, pizza, cheese):
        if pizza not in self.list_of_pizzas: # check if pizza exists on menu
            raise PizzaError(pizza, "no such pizza on the menu")
        if cheese > 100:    # check if ordered more then 100% of cheese
            raise TooMuchCheeseError(pizza, cheese, "too much cheese")
        
        # add into orders counter as key and pizza name as value of dict element
        self.orders[self.counter] = pizza
        # build message
        self.message = str(self.counter) + " " + self.orders[self.counter]\
                        + ": successfully created!"
        # show message that pizza made successfully    
        print(self.message)
        # write made pizza to file
        try:
            self.__fo = open('pizza_order.txt', 'at')
            self.__fo.write(self.message)
            self.__fo.write('\n')
            self.__fo.close()
            print("File successfully written!")
        except IOError as e:
            print("I/O error occured: ", strerror(e.errno))
        
        self.counter += 1   # increment counter


# run test
pizzeria = Order()

# make order
for (pz, ch) in [('calzone', 0), ('margerita', 110), ('margerita', 40), ('mafia', 20)]:
    try:
        pizzeria.make_piza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)

print()
print()

# add pizzas
for pz in ['peperoni', 'calzone', 'mafia', 'margharita']:
    try:
        pizzeria.add_pizza(pz)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)

print()
print()

# remove pizzas
for pz in ['peperoni', 'calzone', 'mafia', 'margharita', "blablabla"]:
    try:
        pizzeria.remove_pizza(pz)
    except PizzaError as pe:
        print(pe, ':', pe.pizza)