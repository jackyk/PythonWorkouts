class Pets:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def get_name(self):
        return self.name
    def get_species(self):
        return self.species

polly = Pets("Polly","Parrot")
print polly.get_species()
print polly.get_name()
