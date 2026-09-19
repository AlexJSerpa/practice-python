class Car():
    length = 250
    width = 100
    wheels = 4
    underway = False

    def start(self):
        self.underway = True

    def status(self):
        if (self.underway):
            return "The car is underway"
        else :
            return "The car is top"

myCar = Car()
myCar.start()
print(myCar.status())


