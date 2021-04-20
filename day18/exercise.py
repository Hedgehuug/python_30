"""
Create a decorator that works as a cache for the different
calls we make to a function, you can test with the function
fibonacci.
"""

from timeit import timeit


history = {}
def test_func(fnc):
    def inner(num):
        if num in history:
            return history[num]
        history[num] = fnc(num)
        return fnc(num)
    return inner

@test_func
def fibonacci(num):
    if num in [0, 1]:
        return num
    
    # So I have to send this result to a history[()]
    return fibonacci(num - 1) + fibonacci(num - 2)
    
# Output: 9227465
print(timeit("fibonacci(35)", setup="from __main__ import fibonacci", number=1))

"""
Create a decorator logger which prints out what you are calling
and what you get as a result of the function.
"""

import random
num_list = range(1,5001)


# ---- This is definitely an important function, I should use this for all of my code
def logging_func(fnc):
    def inner(num):
        print(f"Starts with: {num}")
        print(f"Returns: {fnc(num)}")
        return fnc(num)
    return inner

@logging_func
def sum_2(num):
    return num + num

list(map(sum_2,num_list))
# Output:
# Starts with: 5000
# Returns: 10000
