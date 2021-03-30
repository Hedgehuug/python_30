"""
Using the range function, create a sequence of numbers
from 1 to 100, and using the filter function return only
those that are multiplies of 2.
"""

range_100 = list(range(1,101))

def div_by2(item):
    return item%2 == 0

print(list(filter(div_by2,range_100)))
#Output:
# [2, 4, 6, 8, 10, 12, 14, ...94, 96, 98, 100]


"""
According to the example of older users, take the same
list of users or create your own and return those who
are underage.
"""
def validate_age(user):
    return user['age'] < 18

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

print(list(filter(validate_age,users)))

#Output: [{'name': 'Esteban', 'age': 6}, {'name': 'Jose', 'age': 15}]

"""
Create a new list of numbers in this case from -10 to
10 and return only those that are multiples of 3 and
negative.
"""

negative_range = list(range(-10,11))

def get_negative3(item):
    if item % 3 == 0:
        return item < 0
    else:
        return False

print(list(filter(get_negative3,negative_range)))
#Output: [-9, -6, -3]

