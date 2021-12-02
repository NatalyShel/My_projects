##########################################################################
#Author: Nataly
#Date: 02.12.2021
#Task:
# • create class Pizza
# • list of pizza - private in constructor
# • write method like make_a_pizza
##########################################################################

class PizzaError(Exception):    # exception if pizza not on menu
    def __init__(self, pizza = "unknown", message = ''):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):   # exception if too much cheese ordered
    def __init__(self, pizza = "unknown", cheese = '>100', message = ''):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


class Pizza():
    def __init__(self):
        # define and init menu of pizzas
        self.__pizzas = ['calzone', 'margerita', 'verde', 'romana']
    
    def make_piza(self, pizza, cheese):
        if pizza not in self.__pizzas: # check if pizza exists on menu
            raise PizzaError(pizza, "no such pizza on the menu")
        if cheese > 100:    # check if ordered more then 100% of cheese
            raise TooMuchCheeseError(pizza, cheese, "too much cheese")
        # show message if pizza made successfully     
        print("Pizza ", pizza, " ready!", sep="'")


# run test
pizza_obj = Pizza() # create object of Pizza class (and init pizza menu)

# try to make 4 pizzas
for (pz, ch) in [('calzone', 0), ('margerita', 110), ('mafia', 20), ('romana', 9)]:
    try:
        pizza_obj.make_piza(pz, ch)
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)
    except PizzaError as te:
        print(te, ':', te.pizza)