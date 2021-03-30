"""
Day 6: Reduce

higher order function
takes (function,sequence) as input
uses the first 2 elements of the sequence for the calculations
NEEDS TO BE IMPORTED
"""
from functools import reduce

test_list = [1,5,3,7,4]

#The function has to take 2 inputs
def add(num_a,num_b):
    return num_a + num_b

print(reduce(add,test_list))

#Let's create a single string from a list of strings

def join_string(str_a,str_b):
    return f"{str_a} {str_b}"

str_list = ['Hello','world',"what's",'up']

print(reduce(join_string,str_list))

#While working on this problem, also found out about F-strings, this is a little different in javascript, but I like that something so easy can make such change