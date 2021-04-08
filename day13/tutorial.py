"""
Day 13: Dunder Methods

"Everything in Python is an Object"

Dunder methods are methods we can define in our classes to give them more functionality than they have
Dunder refers to the double underscore at the beginning and end of the variable name e.g.: __init__
"""

#Initiating a class with __init__
"""
class User:
    def __init__(self,name):
        self.__name = name

    @classmethod
    def create_person(cls,name):
        return cls(name)

new_person = User.create_person('Elizabeth')
print(new_person)
"""
# Ouput: <__main__.User object at 0x102232be0>
# This is not what we need, object representation helps with this


# Object representation
# __repr__ is a method for defining what represents a class
"""
class User:
    def __init__(self, name):
        self.__name = name

    # So now when we print() an instance, it'll print what we return in here
    def __repr__(self):
        return f"Class User: {self.__name}"

new_person = User('Elise')
print(new_person)
"""
# Output:  Class User: Elise

# Count
"""
class User:
    def __init__(self, name):
        self.__name = name

    def __repr__(self):
        return f"Class User: {self.__name}"

    def __len__(self):
        return len(self.__name)

new_person = User('Cleaford')
print(new_person.__len__())
"""
# Output: 8
# This honestly feels a little pointless?




