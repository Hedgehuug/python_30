"""
Create a class called Pizza that allows you to create different
types of them. When you create them, give them the price of the
pizza.
The class should calculate the size of the pizza based on the
price.
0 - 10 small
11 - 20 medium
21 - 30 large
"""

class Pizza:
    def __init__(self, price, topping):
        self.price = price
        self.topping = topping
        print(self.price_method())

    def price_method(self):
        print(self.price)
        if self.price < 0 or self.price>30:
            print(f"{self.price} is out of range")
        if self.price<=10:
            return "small"
        if self.price<=20:
            return "medium"
        if self.price<=30:
            return "large"


pizza = Pizza(21,'margharita')

# So I wanted to create an alternate answer based on the official solution to the problem, because I think it's genius

class Pizza:
    def __init__(self, ingredients, price):
        self.price = price
        self.ingredients = ingredients
        self.size = self._pizza_size(price)
    
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

chicken_pizza = Pizza.chicken(10)
print(chicken_pizza.size)
print(chicken_pizza.ingredients)

italian_pizza = Pizza.italian(22)
print(italian_pizza.size)
print(italian_pizza.ingredients)

# Output:
# small
# ['cheese', 'chicken', 'mushroom']
#
# large
# ['salami', 'cheese', 'tomato', 'basil']
