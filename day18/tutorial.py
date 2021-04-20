"""
Day 18: Decorators

Decorators are powerful for people that can use them properly

Following good practices, decorators make the code easier to read and remove repetition

What are decorators?
    Decorators are functions that take other functions and extend their capabilities without modifying the original
"""

def decorator(fun, arg_1, arg_2):
    total = fun(arg_1,arg_2)
    print(f'the result of {arg_1} and {arg_2} is {total}')


def sum_function(num_1,num_2):
    return num_1+num_2

# decorator(sum_function,6,5)
# Output: the result of 6 and 5 is 11
# This is an example of how a decorator works, but python has built-in methods for ACTUALLY using decorators

# The same process with decorators would look like:
def decorator_2(fun):
    def wrapper(arg_a,arg_b):
        total = fun(arg_a,arg_b)
        print(f'the result of {arg_a} and {arg_b} is {total}')
    return wrapper

# The way to declare an operator is by putting @ with the name of the function you want to take from behind it
@decorator_2
def addition(num_a,num_b):
    return num_a + num_b

addition(3,4)
# Output: the result of 3 and 4 is 7
# just writing this down I don't get it yet


"""
Functions with Arguments:
functions with arguments is a type of decorator:

The structure of decorators is made by nesting functions and returning each one of them
depending on the values we receive (function/arguments). When a function to be decorated 
receives arguments, the decorator changes and a new function is nested which receives
the arguments that the main function receives.
^^ I have no idea what this means yet
Let's take a look at the following example
"""

from functools import wraps
# This is not something mentioned in the tutorial, I had to watch a separate video to understand this

def operation(function):
    print('function is an argument')
    @wraps(function)
    def wrapper(*args,**kwargs):
        print('All function parameters are arguments')
        return function(*args,**kwargs)
    return wrapper

@operation
def add(num_1,num_2):
    print('Decorated Function')
    return num_1,num_2

print(add(3,4))


# Decorators with Arguments
# @decorator(argument)
import random

# Exponent in maths is the value we want to raise to
def power_of(arg):

    def decorator(fnc):

        def inner():
            return fnc() ** exponent

        return inner
        # Okay this is very interesting, if we verify whether the argument is a function or not we can remove the () from the @power_of
    if callable(arg):
        exponent = 2
        return decorator(arg)

# This allows us to determine what power we want to raise the value to
@power_of
def random_odd_digit():
    return random.choice([1,3,5,7,9])

print(random_odd_digit())

