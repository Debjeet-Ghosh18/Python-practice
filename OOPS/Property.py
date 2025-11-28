class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    # def calculatepercentage(self):
    #     self.percentage = self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"

stu1 = Student(46,68,74)
print(stu1.percentage)

stu1.phy = 60
print((stu1.phy))
# stu1.calculatepercentage()
print(stu1.percentage)        