class Vet:
    # Class attributes
    total_animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if len(self.animals) < Vet.space:
            self.animals.append(animal_name)
            Vet.total_animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        else:
            return "Not enough space"

    def unregister_animal(self, animal_name):
        if animal_name in self.animals:
            self.animals.remove(animal_name)
            Vet.total_animals.remove(animal_name)
            return f"{animal_name} unregistered successfully"
        else:
            return f"{animal_name} not in the clinic"

    def info(self):
        number_animals = len(self.animals)
        space_left_in_clinic = Vet.space - len(Vet.total_animals)
        return f"{self.name} has {number_animals} animals. {space_left_in_clinic} space left in clinic"


# Example usage:
vet1 = Vet("Dr. Smith")
vet2 = Vet("Dr. Johnson")

print(vet1.register_animal("Dog"))
print(vet1.register_animal("Cat"))
print(vet2.register_animal("Parrot"))
print(vet1.info())

print(vet1.unregister_animal("Dog"))
print(vet2.unregister_animal("Parrot"))
print(vet1.unregister_animal("Elephant"))
print(vet1.info())
