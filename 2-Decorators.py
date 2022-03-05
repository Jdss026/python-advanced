"""
def mydecorator(function):

    def wrapper(*args, **kargs):
        # args and kargs pass the arguments from the decorated function
        return_value = function(*args, **kargs)
        print("I am decorating your funcion")
        return return_value

    return wrapper

@mydecorator
def hello_word(person):
    print(f"Hello {person}")
    return f"Hello {person}"

print(hello_word("Mike"))
# mydecorator(hello_word)()
"""

# Pratical example #1 - Logging
"""
def logged(function):
    def wrapper(*args, **kargs):
        value = function(*args, **kargs)
        with open('logfile.log', 'a+') as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname}returned value {value}\n")
        return value
    return wrapper

@logged
def add(x, y):
    return x + y

print(add(10,20))
"""

# Pratical Example #2 - Timing

import time

def timed(function):
    def wrapper(*args, **kargs):
        before = time.time()
        value = function(*args, **kargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} seconds to execute!")
        return value

    return wrapper

@timed
def myfunction(x):
    result =1
    for i in range(1, x):
        result *= i
    return result

myfunction(90000)