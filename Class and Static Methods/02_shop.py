class Shop:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, item_name):
        if len(self.items) >= self.capacity:
            return "Not enough capacity in the shop"
        else:
            self.items[item_name] = self.items.get(item_name, 0) + 1
            return f"{item_name} added to the shop"

    def remove_item(self, item_name, amount):
        if item_name in self.items and self.items[item_name] >= amount:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                del self.items[item_name]
            return f"{amount} {item_name} removed from the shop"
        else:
            return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

# Example usage:
shop1 = Shop("Grocery Store", "Supermarket", 50)
print(shop1.add_item("Apples"))          # Output: "Apples added to the shop"
print(shop1.add_item("Bananas"))         # Output: "Bananas added to the shop"
print(shop1.add_item("Apples"))          # Output: "Apples added to the shop"
print(shop1.remove_item("Apples", 2))    # Output: "2 Apples removed from the shop"
print(shop1.remove_item("Bananas", 3))   # Output: "Cannot remove 3 Bananas"
print(repr(shop1))                        # Output: "Grocery Store of type Supermarket with capacity 50"
