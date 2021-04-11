"""
Keep using the Pizza class, this time add some basic
methods for calculating and comparing each of the Pizza
objects created.
"""

class Pizza:
    def __init__(self, ingredients, price):
        self.price = price
        self.ingredients = ingredients
        self.size = self._pizza_size(price)

    # Object representation
    def __repr__(self):
        return f"Price: {self.price}, Ingredients: {self.ingredients}, Size: {self.size}"
        # So __repr__ can only return strings
        """return {
            'Price': self.price,
            'Ingredients': self.ingredients,
            'size': f"Based on price: {self.price}, {self.size}"
            }"""

    # Method to know if the pizza has any ingredients e.g. "cheese" in pizza_n
    def find_ingredient(self,to_find):
        ingredient = to_find
        ingredients_list = self.ingredients
        for i in ingredients_list:
            if not isinstance(ingredient,str):
                return 'Incorrect ingredient'
            if i == ingredient:
                return f"{ingredient} is on pizza"
            if i != ingredient:
                return f"{ingredient} is not on pizza"

    # Count the pizza ingredients
    def __len__(self):
        return len(self.ingredients)

    
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

    def __lt__(self,other_instance):
        return self.price < other_instance.price

    def __gt__(self,other_instance):
        return self.price > other_instance.price

    def __sub__(self,other_instance):
        return self.price - other_instance.price

chicken_pizza = Pizza.chicken(13)
italian_pizza = Pizza.italian(25)

print(italian_pizza<chicken_pizza)
print(italian_pizza>chicken_pizza)
difference = chicken_pizza-italian_pizza
print(difference)
# Output:
# False
# True
# -12
