class Animal:
    def __init__(self,legs):
        self.legs = legs


class Dog(Animal):
    def __init__(self,legs,name,owner):
        Animal.__init__(self,legs)
        self.name = name
        self.owner = owner

class Labrador(Dog):
    def __init__(self,legs,name,owner,habitat):
        Dog.__init__(self,legs,name,owner)
        self.habitat = habitat

d1 = Labrador(4,"Tiger","Aabiskar","Wild")
print(d1.__dict__)