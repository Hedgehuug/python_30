"""
You can use the range function to easily create a list with
100 numbers, use list slices to take only those numbers that
are multiples of 3.
"""

def createList(num):
    output = []
    for i in range(num+1):
        output.append(i)
    return output
 
print(createList(100)[::3])

"""
From the list
['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
Generate the following
['o', 'l', 'l']
"""
model_list = ['o','l','l']
hello = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
print(hello[4:1:-1])
#Kinda weird that you also have to switch around the start and stop if you use a negative step

"""
Remember it doesn't only work with lists, write your name and
put it in reverse
"""
name = "Ben Waldinger"
print(name[::-1])