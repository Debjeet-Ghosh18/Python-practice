class Car:
    @staticmethod
    def start():
        print("Car Started...")

    def stop():
        print("Car Stopped...")

class Toyota_Car(Car):
    def __init__(self,name):
        self.name = "Debjeet"

Car1 = Toyota_Car("Fortuner")
Car2 = Toyota_Car("Prius")

print(Car1.start())
        