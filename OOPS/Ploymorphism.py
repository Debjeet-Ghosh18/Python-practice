# print(1+2) #add
# print(type(1))

# print("Debjeet" + " Ghosh") #Concatenation
# print(type("Debjeet"))

# print([1,2,3]+[4,5]) #Merge
# print(type([1,2,3]))
class Complex:

    def __init__(self,real,img):
        self.real = real 
        self.img = img
    
    def Shownumber(self):
        print(self.real,"i+",self.img,"j")

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)
    
c1 = Complex(6,5)
c1.Shownumber()

c2 = Complex(3,3)
c2.Shownumber()

c3 = c1 - c2
c3.Shownumber()

c4 = c1 + c2
c4.Shownumber()