from functools import reduce
"""
Create a function that multiplies a sequence of
numbers.
"""
mul_range = range(1,10)

def multiply(num_1,num_2):
    return num_1*num_2

print(reduce(multiply,mul_range))

#Output: 362880

"""
Create a function that takes a list of
strings and return the sum of its characters.
["I", "am", "esteban"] => 1 2 and 7
10
"""
#For this I will use my list from the tutorials

str_list = ['Hello','world',"what's",'up']

def count_chars(str_1,str_2):
    try:
        return len(str_1) + len(str_2)
    except:
        return str_1 + len(str_2)

print(reduce(count_chars,str_list))
#this was a hard question so I looked up the solution once I was done, and they used - isinstance() to solve it, no clue what that is

"""
This challenge can be a bit complicated, however
remember that in the functions you can perform
conditionals, take a list of numbers and return
the largest number.
"""

num_list = [12,47,2,213,63,436,87,2,545,2,34]

def get_largest(num_1,num_2):
    if num_1 > num_2:
        return num_1
    elif num_2 > num_1:
        return num_2
    else:
        return num_1
    
print(reduce(get_largest,num_list))
#I was told this would be a hard question, it wasn't