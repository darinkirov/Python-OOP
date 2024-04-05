class Vehicle:
    def __init__(self, mileage, max_speed=150):
        self.max_speed = max_speed
        self.mileage = mileage
        self.gadgets = []

# Example usage:
car = Vehicle(50000)
print(car.max_speed)  # Output: 150 (default value)
print(car.mileage)    # Output: 50000
print(car.gadgets)    # Output: [] (empty list by default)
