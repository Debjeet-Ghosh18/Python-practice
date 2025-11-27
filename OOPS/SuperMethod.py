class Car:

    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car Started..")

    @staticmethod
    def stop():
        print("Car Stopped")
        
class Toyota_Car(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        super().start()

t1 = Toyota_Car("Fortuner","Diesel")

print(t1.type)

       