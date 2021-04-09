"""
Day 14: Operator Overloading

We do comparisons every day
Often comparing integers: 2 < 6
Operator Overloading allows us to define values to Classes which to compare them by
"""

# For now we create a basic Products class
"""
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __repr__(self):
        return f"Product: {self.__name}"


pizza = Product('pizza',12)
hotdog = Product('hotdog',7)

print(pizza)
print(hotdog)
"""
# Output: 
# Product: pizza
# Product: hotdog

"""
If we try to compare the two, we get an error
print(pizza > hotdog)
print(pizza < hotdog)
print(pizza == hotdog)

# Output:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '>' not supported between instances of 'Product' and 'Product'
"""
# We can solve this by defining ways of comparing our objects manually
"""
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __repr__(self):
        return f"Product: {self.__name}"

    # This is not explained in the tutorial, but I think this stands for Less Than(lt)
    def __lt__(self, other_instance):
        return self.__price < other_instance.__price

    # greater than(gt)
    def __gt__(self, other_instance):
        return self.__price > other_instance.__price

    def __eq__(self, other_instance):
        return self.__price == other_instance.__price

pizza = Product('pizza',12)
hotdog = Product('hotdog',9)
# Let's try and make the comparisons again
print(pizza>hotdog)
print(pizza<hotdog)
print(pizza==hotdog)"""
# Output: 
# True
# False
# False

# Operations
# We can also define operations to do in-case they are called, such as add, mul, div etc..
class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __repr__(self):
        return f"Product: {self.__name}"

    def __add__(self, other_instance):
        return self.__price + other_instance.__price

    def __mul__(self, other_instance):
        return self.__price * other_instance.__price

pizza = Product('pizza',12)
hotdog = Product('hotdog',9)

total_sum = pizza+hotdog
total_mul = pizza*hotdog
print(total_sum)
print(total_mul)
# Output:
# 21
# 108