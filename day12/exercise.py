"""
Use the class created about Pizza and implement the
property decorator for each of its attributes.
"""

class Pizza:
    def __init__(self, ingredients, price):
        self.__price = price
        self.__ingredients = ingredients
        self.__size = self._pizza_size(price)

    # Price Property
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,price):
        self.__price = price

    # Ingredients Property
    @property
    def ingredients(self):
        return self.__ingredients
    @ingredients.setter
    def ingredients(self,ingredients):
        self.__ingredients = ingredients

    # Size Property
    @property
    def size(self):
        return self.__size
    
    # So this is a wonderful use of classmethod, to create a function for initiating a class from within the class
    @classmethod
    def chicken(cls, price):
        ingredients = ["cheese", "chicken", "mushroom"]
        return cls(ingredients, price)
    
    @classmethod
    def italian(cls, price):
        ingredients = ["salami", "cheese", "tomato", "basil"]
        return cls(ingredients, price)
    
    #Static methods have no dependance to the rest of the class, so we can use it for always-the-same calculations
    @staticmethod
    def _pizza_size(price):
        sizes = {
            "small": (0, 10),
            "medium": (11, 20),
            "large": (21, 30)
        }

        pizza_size = ""
        for size, (min_price, max_price) in sizes.items():
            if min_price <= price <= max_price:
                pizza_size = size
                break
        
        return pizza_size

margi  = Pizza.chicken(13)
print(margi.ingredients)