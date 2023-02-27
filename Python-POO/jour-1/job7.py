class Animal:

    def __init__(self):
        self.age = 0
        self.prenom = ''

    def viellir(self): 
        self.age += 1

    def nommer(self):
        self.prenom = "Luna"

animal = Animal()
animal.viellir()
animal.nommer()

print("L'age de l'animal est ", animal.age )
print("Le prenom de l'animal est", animal.prenom)

    