"""
Day 4: Map

higher order function
map function receives two arguments
- a function
- a sequence - list/tuple

oh so map runs items in the list through the function given, can be used to make recursion prettier?
"""

#mapping takes a function
def used_function(item):
    return item * 2

#and a list
used_list = [2,6,4,21,9]

#and oredered 1:function 2:list - it'll run all the items in the used_list through the function, creating a new final_ list with the new values
final_list = map(used_function,used_list)

print(list(final_list))

#can be used for dictionaries too
#example below was copied from the tutorial

users = [
    {
        "name": "Esteban",
        "age": 26
    },
    {
        "name": "Jose",
        "age": 23
    },
    {
        "name": "Jaime",
        "age": 40
    }
]

def get_age(user):
    return user["age"]

print(list(map(get_age, users)))


# Output:
# [26, 23, 40]
#I like this Output comment, I will definitely start including it for myself, I always have to refresh the layout of the output
    

#Multiple Sequences: Map functions can take multiple inputs at the same time

def print_info(name,age,likes):
    return {
        "name": name,
        "age": age,
        "likes": likes
    }
names = ['Kobi','Nathan','Izelda']
ages = [39,27,24]
likes = ['Kobie','Sailing','Curses']
print(list(map(print_info,names,ages,likes)))
"""
Output:
[
    {'name': 'Kobi', 'age': 39, 'likes': 'Kobie'},
    {'name': 'Nathan', 'age': 27, 'likes': 'Sailing'},
    {'name': 'Izelda', 'age': 24, 'likes': 'Curses'}
    ]
"""