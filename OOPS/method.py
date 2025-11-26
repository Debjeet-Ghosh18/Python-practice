class Student:

    #Default Constructor
    def __init__(self):
        pass

    #Parameterized Constructor
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("Welcome",self.name)

    def get_marks(self):
        return self.marks


S1 = Student("Debjeet",85)
S1.welcome()
print(S1.get_marks())

