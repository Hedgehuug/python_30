"""
Day 3: List Slices

doing algorithmic trading, I've worked with slices a lot to edit the Symbols, so this isn't new for me

Syntax: my_list[start:stop:step]
"""

#you don't need to pass in any variables, but then it'll just grab the whole list as is

my_list = ['H','E','Y']
print(my_list[:])

#This also works with strings just as well
my_string = "Hello World"
print(my_string[:-2])

#Just like the Range function, Slices also have a Step, this is 1 by default

print(my_string[::2])
#Can also be a negative
print(my_string[::-1])