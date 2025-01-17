class Engine:
    def __init__(self, type):
        self.type = type

    def start(self):
        return f"{self.type} engine started"

    def stop(self):
        return f"{self.type} engine stopped"


class Wheel:
    def __init__(self, type):
        self.type = type

    def start(self):
        return f"{self.type} wheels started"

    def stop(self):
        return f"{self.type} wheels stopped"


class Car:
    def __init__(self, engine_type, wheel_type):
        self.engine = Engine(engine_type)
        self.wheels = Wheel(wheel_type)

    def start_car(self):
        print(self.engine.start())
        print(self.wheels.start())
        print("Car started\n")

    def stop_car(self):
        print(self.engine.stop())
        print(self.wheels.stop())
        print("Car stopped\n")


car1 = Car("Toyota", "Alloy")
car1.start_car()
car1.stop_car()
