class car:
    def __init__(self):
        self.clutch = False
        self.brk = False
        self.acc = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started")

C1 = car()
C1.start()