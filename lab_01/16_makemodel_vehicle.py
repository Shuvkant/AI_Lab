class Vehicle():
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")


class car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def drive(self):
        print(f"Driving the {self.make} {self.model} car")


vehicle1 = Vehicle("Toyota", "Tundra")
vehicle1.drive()
car1 = car("Tata", "Nexus")
car1.drive()
