"""
Day 17: Memoization

Memoization is not memorization

memoization is a caching technique that saves the result of complex computations to use later

We can use this to optimise the speed of our app and the memory usage of it
"""

# following function can be a bit computation-intensive depending on the input num
from timeit import timeit
'''
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n-2)
'''
# print(timeit("fibonacci(35)", setup='from __main__ import fibonacci',number=1))
# Output: 3.624875227
# This process can be optimized, if we pass in 35 again, we will get the same results over and over, this is called a Pure-Function
# We don't want to wait 4 seconds every time we pass in 35

# We can save some of these results to decrease later computation time

history = {}
def fibonacci(n):
    if n in history:
        return history[n]

    if n == 0:
        return 0
    elif n == 1:
        return 1

    fibonacci_result = fibonacci(n - 1) + fibonacci(n-2)
    history[n] = fibonacci_result

    return fibonacci_result

print(timeit("fibonacci(35)", setup='from __main__ import fibonacci',number=1))
# Output: 1.8756000000001716e-05
# When calculating fibonacci, we sometimes return to the same numbers, so by creating a history, some of those numbers will be much quicker to retrieve

