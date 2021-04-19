"""
Memoization is not really difficult, find any other simple
example that you can implement memoization to not repeat processes.
"""

# Wow, this is a hell of a task to give me

# Gonna try create a list of random numbers to square
from timeit import timeit
import random

use_list = []
for item in range(3000000):
    use_list.append(random.randint(1,15))
history = {}

#print(use_list)
def square_numbers(num):
    if num in history:
        return history[num]

    final_value = num * num * num
    history[num] = final_value
    return final_value

# print_value = list(map(square_numbers,use_list))
final_list = list(map(square_numbers,use_list))
time1 = timeit('map(square_numbers,use_list)', 'from __main__ import square_numbers, use_list', number=1)
final_value = sum(final_list) / len(final_list)
timed = time1 + timeit('final_value', 'from __main__ import final_value', number=1)
print(time1)

# Output value