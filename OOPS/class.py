class Student:

    #Default Constructor
    def __init__(self):
        pass

    #Paramiterized Constructor
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database")

S1 = Student("Debjeet",85)
print(S1.name,S1.marks)

S2 = Student("Ghosh",75)
print(S2.name,S2.marks)

# class Car:
#     color = "Blue"
#     brand = "BMW"
# C1 = Car()
# print(C1.color)
# print(C1.brand)