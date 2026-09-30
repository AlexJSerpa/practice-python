import pickle

class Pet():
    def __init__(self, name, type_animal, age):
        self.name = name
        self.type_animal = type_animal
        self.age = age

    def get_information(self):
        print("The name is: ", self.name, "\nIt's a: ", self.type_animal, 
              "Their age is: ", self.age )


cat = Pet("cat", "feline", 4)
dog = Pet("Firulais", "dog", 5)

list_pets = [cat, dog]

file_pets = open("pets", "wb")

pickle.dump(list_pets, file_pets)

file_pets.close()

del (file_pets)

open_file = open("pets", "rb")

my_pets = pickle.load(open_file)

open_file.close()

for pet in my_pets:
    pet.get_information()


