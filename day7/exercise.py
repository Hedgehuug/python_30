from functools import reduce
"""
Use the lambda functions with the challenges of
map, filter and reduce.

^^Litle cheap :_()
"""

"""
Map Exercises: 

Again use the range function to generate a sequence of
numbers from 1 to 20, use the map function to return
whether the number is even or not.
"""

print(list(map(lambda num: num%2==0,range(1,21))))
#easy

"""
Create two lists A and B of numbers, which must be given
to the function, the final result will be a new list which
will contain the sum of the values in A and B
"""

list_a = [6,12,3,7,2]
list_b = [6,2,4,7,8]
print(list(map(lambda item_1,item_2: item_1*item_2,list_a,list_b)))
#Output: [36, 24, 12, 49, 16]
#I thought this'd be more useful in multiple lines


"""
Create a list of lists, these with multiple numbers to
be averaged
"""
#Gonna copy my original list for this
lists_list = [
    [2,71,9,5,24],
    [63,34,9,23,2],
    [6,22,3,7,45]
]
print(list(map(lambda used_list:sum(used_list)/len(used_list),lists_list)))
#Output: (matched output from og exercise)
#[22.2, 26.2, 16.6]

"""
Filter exercises:

Using the range function, create a sequence of numbers
from 1 to 100, and using the filter function return only
those that are multiplies of 2.
"""
print(list(filter(lambda num:num%2==0,range(1,101))))
#this was in the tutorial today

"""
According to the example of older users, take the same
list of users or create your own and return those who
are underage.
"""
#Will use old dict

users = [
    {
        "name": "Esteban",
        "age": 6
    },
    {
        "name": "Jose",
        "age": 15
    },
    {
        "name": "Jaime",
        "age": 18
    }
]

print(list(filter(lambda user:user['age']<18,users)))
#Output: [{'name': 'Esteban', 'age': 6}, {'name': 'Jose', 'age': 15}]


"""
Create a new list of numbers in this case from -10 to
10 and return only those that are multiples of 3 and
negative.
"""

print(list(filter(lambda num: num%3==0 and num<0,range(-10,11))))
#output: [-9, -6, -3]




"""
Reduce exercises:

Create a function that multiplies a sequence of
numbers.
"""
sequence_list = [6,12,6,8,2]

print(reduce(lambda num_1,num_2:num_1*num_2,sequence_list))

"""
Create a function that takes a list of
strings and return the sum of its characters.
["I", "am", "esteban"] => 1 2 and 7
10
"""

string_list = ['I','am','esteban','from','earth']
lambda_reduce = reduce(lambda word_1,word_2: len(word_1)+len(word_2) if isinstance(word_1,str) else word_1+len(word_2),string_list)
print(lambda_reduce)
#Output: 19
#This was really not easy

"""
This challenge can be a bit complicated, however
remember that in the functions you can perform
conditionals, take a list of numbers and return
the largest number.
"""
list_of_numbers = [
    2,71,9,5,24,
    63,34,9,23,2,
    6,22,3,7,45
]

print(reduce(lambda num_1,num_2: num_1 if num_1>num_2 else num_2,list_of_numbers))
