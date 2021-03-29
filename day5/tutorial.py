"""
Day 5: Filter

Like Map, it recieves (function,sequence) as variables
If the function returns True with the element of the sequence, it'll keep the value, if it returns False, it'll discard
"""

#Example below keeps only the word "hello" out of the list

def keep_hello(string):
    return string == 'hello'

hello_list = ['hello','my','name','is','Ben']


print(list(filter(keep_hello,hello_list)))


#example below shows how to validate legal age
#copied from tutorial
users = [
    {
        "name": "Esteban",
        "age": 26
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

def validate_age(user):
    return user["age"] >= 18

print(list(filter(validate_age, users)))

# Output:
# [
#   {'name': 'Esteban', 'age': 26},
#   {'name': 'Jaime', 'age': 18}
# ]

