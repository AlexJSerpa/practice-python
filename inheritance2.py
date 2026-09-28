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

class ElectricVehicle():
    def __init__(self):
        self.vehicle_range = 100 

class Motorcycle(Vehicle):
    wheelie = ""

    def do_wheelie(self):
        self.wheelie = "Doing a wheelie"

    def status(self):
        print(
            "Brand:", self.brand,
            "\nModel:", self.model,
            "\nRunning:", self.running,
            "\nAccelerates:", self.accelerates,
            "\nBrakes:", self.brakes,
            "\n", self.wheelie
        )

    
myMotorcycle = Motorcycle("Ducati", "Hypermotard 950")

myMotorcycle.status()
        