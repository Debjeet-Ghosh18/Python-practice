class Student:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks


    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi",self.name,"your avg score is:",sum/3)

s1 = Student("Debjeet",[60,70,80])
s1.get_avg()     

s1.name = "Ghosh"
s1.get_avg()
