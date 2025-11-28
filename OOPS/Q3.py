class Circle:
    def __init__(self,radi):
        self.radi = radi

    def area(self):
        return (22/7) * self.radi **2
    
    def perimeter(self):
        return 2 * (22/7) * self.radi
    
c1 = Circle(8)

print(c1.area())
print(c1.perimeter())
        