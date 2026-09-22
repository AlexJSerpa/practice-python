class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.running = False
        self.accelerates = False
        self.brakes = False

    def start(self):
        self.running = True

    def speed_up(self):
        self.accelerates = True

    def brake(self):
        self.brakes = True

    def status(self):
        print("Brand: ", self.brand, "\nModel: ", self.model, "\nRunning ", self.running
              , "\nAccelerates: ", self.accelerates, "\nBrakes: ", self.brakes)

class Motorcycle(Vehicle):
    pass

myMotorcycle = Motorcycle("Ducati", "Hypermotard 950")

myMotorcycle.status()
        