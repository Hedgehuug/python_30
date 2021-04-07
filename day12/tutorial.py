"""
Day 12: Property

In OOP, getters and setters help us access private attributes of a class in a defined manner

Python doesn't have the capability to define Private/Public variables,
but we can use conventions to indicate to other developers the accessibility

we use 2:
Protected: protected methods and attributes usually have a single underscore before the variable name = _protected_variable
Private: Private attributes have two underscores before the name = __private_variable
"""

# Getter/Setter
class User:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter
    def get_name(self):
        return self.__name

    # Setter
    def set_name(self,name):
        self.__name = name

# Instances
user = User('Esteban',26)
print(user.get_name())
# Output: Esteban
user.set_name("Georgie")
print(f"name has been changed to {user.get_name()}")
# Output: name has been changed to Georgie


# Property: 
# Property can be used to make getters/setters in a more Pythonic way

# Property is a decorator used for this
# Same example as above
class NewUser:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    
    #Property seems to create a global variables in a similar state to a usual getter
    @property
    def name(self):
        print('Getter called')
        return self.__name

    @name.setter
    def name(self,name):
        print('Setter called')
        self.__name = name
    
    #Went back to create an age getter/setter too

    @property
    def age(self):
        print('Age getter')
        return self.__age

    @age.setter
    def age(self,age):
        print('Age setter')
        if not isinstance(age,int) or age<0:
            raise ValueError('Invalid age')
        self.__age = age


new_user = NewUser('Johnathan',32)
print(f"Name: {new_user.name}")
new_user.name = 'Soroda'
print(f"Name: {new_user.name}")
#Output:
# Getter called
# Name: Johnathan
# Setter called
# Getter called
# Name: Soroda

print(new_user.age)
# Output: 32
new_user.age = 45
print(new_user.age)