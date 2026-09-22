class Car:

    def __init__(self):
        self.__length = 250
        self.__width = 200
        self.__wheels = 4
        self.__underway = False

    def start(self, underway):
        self.__underway = underway

        if(self.__underway):
            return "The car is underway"
        else:
            return "The car is toped"

    def status(self):
        print("The car has length of ", self.__length, " and width ", self.__width,
            " the total wheels ", self.__wheels)

car1 = Car()
print(car1.start(True))
car1.status()

print("------ The second car --------------")

car2 = Car()
car2.__wheels = 5
car1.status()