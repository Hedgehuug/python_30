"""
Map Exercises



Again use the range function to generate a sequence of
numbers from 1 to 20, use the map function to return
whether the number is even or not.
"""
my_range = list(range(1,21))

def find_even(item):
    if item % 2 == 0:
        return (item,"even")
    else:
        return (item,"not")

print(list(map(find_even,my_range)))

"""
Output:
[
    (1, 'not'), (2, 'even'), (3, 'not'), (4, 'even'), (5, 'not'), 
    (6, 'even'), (7, 'not'), (8, 'even'), (9, 'not'), (10, 'even'), 
    (11, 'not'), (12, 'even'), (13, 'not'), (14, 'even'), (15, 'not'), 
    (16, 'even'), (17, 'not'), (18, 'even'), (19, 'not'), (20, 'even')
    ]
"""


"""
Create two lists A and B of numbers, which must be given
to the function, the final result will be a new list which
will contain the sum of the values in A and B
"""
a = [2,71,9,5,24]
b = [63,34,9,23,2]

def mul_function(item_a,item_b):
    return item_a * item_b

print(list(map(mul_function,a,b)))
# Output:
# [126, 2414, 81, 115, 48]

"""
Create a list of lists, these with multiple numbers to
be averaged
- Gonna use previous lists +1
"""
lists_list = [
    [2,71,9,5,24],
    [63,34,9,23,2],
    [6,22,3,7,45]
]

def avg_function(sequence):
    return sum(sequence)/len(sequence)

print(list(map(avg_function,lists_list)))
#Output
#[22.2, 26.2, 16.6]