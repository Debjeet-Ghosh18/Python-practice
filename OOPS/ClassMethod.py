class Person:
    name = "anonymous"

    # def change_name(self,name):
    #     # Person.name = name
    #     self.__class__.name = "Debjeet"

    @classmethod
    def change_name(cls,name):
        cls.name = name
        
p1 = Person()
p1.change_name("Ghosh")
print(Person.name)   
print(p1.name)     