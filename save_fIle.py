import pickle

class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.gender}, {self.age}"

class People:
    people = []

    def __init__(self):
        listPeople = open("externalFile", "ab+")
        listPeople.seek(0)

        try:
            self.people = pickle.load(listPeople)
            print("{} people were loaded from external file".format(len(self.people)))
        except:
            print("The file is empty")
        finally:
            listPeople.close()
            del (listPeople)

    def add_person(self, person):
        self.people.append(person)
        self.savePeopleOnExternalFile()

    def showPeople(self):
        for person in self.people:
            print(person)

    def savePeopleOnExternalFile(self):
        listPeople = open("externalFile", "wb")
        pickle.dump(self.people, listPeople)
        listPeople.close()
        del (listPeople)

    def showExternalFileInfo(self):
        print("The information of the external file is")
        for person in self.people:
            print(person)

myList = People()
person = Person("Sasuke", "Male", 16)
myList.add_person(person)
myList.showExternalFileInfo()

    