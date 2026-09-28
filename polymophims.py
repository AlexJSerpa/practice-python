class car:
    def description(self):
        print("to get around in 4 wheels")

class Motorcycle:
    def description(self):
        print("to get around in 2 wheels")

class Truck:
    def description(self):
        print("to get around in 6 wheels")

def vehicle_description(vehicle):
    vehicle.description()

myVehicle =  Truck()

vehicle_description(myVehicle)


