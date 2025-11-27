class Car:
    @staticmethod
    def start():
        print("Car Started...")

    def stop():
        print("Car Stopped...")

class Toyota_Car(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(Toyota_Car):
    def __init__(self,type):
        self.type = type

For1 = Fortuner("Diesel")

For1.start()


        