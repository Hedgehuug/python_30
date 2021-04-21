"""
Day 19: Generators

To understand Generators, we need to understand Iterators

Iterators:
An iterator is an object that is used to cycle through the elements of a list one-by-one
iterators have a next() which calls the next piece, when there are no more elements, it throws a Stopiteration exception

Generators:
generators are basically Iterators, but the elements are not saved in memory, so we can only loop through it all once
generators can only be created with functions
functions for generators use the Yield keyword instead of Return
"""


def generator():
    counter = 0
    while counter < 10:
        yield counter
        counter += 1


my_gen = (generator())

# Without the next() keyword, print() just returns a generator object: <generator object generator at 0x10bdf7430>

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
# Output: 
# 0
# 1
# 2

# We can use for loops to iterate through the whole thing, and it'll just end instead of throwing an exception
gen_history = []
# This'll only start looping after the next() has been called
# next() wes called 3 times before, so we only start on the 4th element for this loop
for num in my_gen:
    gen_history.append(num)
    print(num)

print(gen_history)
# Like so:
# Output: 
# [3, 4, 5, 6, 7, 8, 9]



"""Send:"""
# send() can be used to inject values into the generator, making it continue from the passed value instead of the original location

def send_generator():
    counter = 0
    while counter < 10:
        new_value = yield counter
        if new_value:
            counter = new_value
        else:
            counter += 1

new_gen = send_generator()

print(next(new_gen))
print(new_gen.send(6))
print(next(new_gen))
# Output:
# 0
# 6
# 7
# Because of the nature of the solution, the count will continue from the injected amount


