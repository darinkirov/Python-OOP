class PizzaDelivery:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity

        self.price += quantity * price_per_quantity

    def remove_ingredient(self, ingredient, quantity, price_per_quantity):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

        if self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"

        self.ingredients[ingredient] -= quantity
        self.price -= quantity * price_per_quantity

    def make_order(self):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        self.ordered = True
        ingredients_str = ", ".join(f"{ingredient}: {quantity}" for ingredient, quantity in self.ingredients.items())
        return f"You've ordered pizza {self.name} prepared with {ingredients_str} and the price will be {self.price}lv."


# Example usage:
pizza = PizzaDelivery("Margherita", 10.99, {"tomato": 1, "cheese": 2, "basil": 1})

print(pizza.add_extra("tomato", 1, 0.5))  # Output: None (no return value for successful operation)
print(pizza.add_extra("mushrooms", 2, 1.5))  # Output: None (no return value for successful operation)
print(pizza.remove_ingredient("cheese", 3, 0.5))  # Output: "Please check again the desired quantity of cheese!"
print(pizza.remove_ingredient("cheese", 2, 0.5))  # Output: None (no return value for successful operation)
print(
    pizza.make_order())  # Output: "You've ordered pizza Margherita prepared with tomato: 2, cheese: 0, basil: 1 and the price will be 15.49lv."
print(pizza.make_order())  # Output: "Pizza Margherita already prepared, and we can't make any changes!"
