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
    #def allergens():


pizza = Pizza(21,'margharita')
