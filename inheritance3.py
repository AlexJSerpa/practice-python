class Person():
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def description(self):
        print ("Name: ", self.name, " Age : ", self.age, " City: ", self.city)

class Worker(Person):

    def __init__(self, name, age, city, salary, position):
        super().__init__(name, age, city)
        self.salary = salary
        self.position = position

        

    def description(self):
        super().description()
        print ("Salary: ", self.salary, " Position: ", self.position)

worker1 = Worker("Alex", 140, "Bogota", 2500, "programmer")

worker1.description()
        

        