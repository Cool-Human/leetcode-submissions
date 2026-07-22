class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def species(self):
        return self.species
    
    def name(self):
        return self.name




# Do not modify below this line
my_pet = Pet("Fluffy", "cat")
print(f"My pet is a {my_pet.species} named {my_pet.name}")
