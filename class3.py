class Car:

    def __init__(self):
        self.__length = 250
        self.__width = 200
        self.__wheels = 4
        self.__start_up = False

    def start(self, start_up):
        self.__start_up = start_up
        isCheck = self.__check()


        if(self.__start_up and isCheck):
            return "The car is start up"
        elif(self.__start_up and isCheck == False): 
            return "Something was wrong"
        else:
            return "The car is stop"

    def status(self):
        print("The car has length of ", self.__length, " and width ", self.__width,
            " the total wheels ", self.__wheels)

    def __check(self):
        self.gasoline = "OK"
        self.doors = "OK"
        self.oil = "lol"
        if (self.gasoline == "OK" and self.doors == "OK" and self.oil == "OK") :
            return True
        else :
            return False

        

car1 = Car()
print(car1.start(True))
car1.status()

print("------ The second car --------------")

car2 = Car()
car2.status()
