"""
Day 11: Classmethod and Staticmethod

Decorators, we'll be exploring 2 decorators provided by python, classmethod and staticmethod
To use decorators, they need to be put over the definition of a method with an @

Methods are a kind of function defined in a class, I know this
"""

#Instance methods
#Instance methods are the most commonly used methods, they are simply the base method for a class, they require an instance of the class to be called

class MyClass:
    def my_instance(self):
        print("instance method called")

class_instance = MyClass()
class_instance.my_instance()
# Output: instance method called
# Instance methods require self as their first arguments

# Classmethod:
# So my guess is classmethod doesn't require an instance, and we can just access any time

class ClassmethodClass:
    #Example of a class' attributes
    attribute = 'hello World'
    
    # This is a decorator
    @classmethod
    def class_method(cls):
        #so it seems the only argument will just be used to access attributes of the class
        print(cls.attribute)

ClassmethodClass.class_method()

# Staticmethods:
# Our last decorator for now, staticmethods take no mandatory arguments, they are just in the class, but don't interact with the class

class StaticClass:
    def __init__(self):
        #We can initiate the class, that'll call the method, or call the method by itself
        self.static_method(25)

    @staticmethod
    # Staticmethods cannot access attributes or other methods of the class
    def static_method(number):
        print('static method called')
        print(number*2)
    
StaticClass.static_method(50)
# Output:
# static method called
# 100

instance = StaticClass()
# Output:
# static method called
# 50


#So the usefulness of these methods is to separate logic that needs and logic that doesn't need the instance
#Good practice to separate these things



