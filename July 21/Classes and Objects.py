#__init__

class Animal:
    """
    This is the Animal class
    """
    def __init__(self, name, habitat, _type, legs = 4):
        self.name = name
        self.habitat = habitat
        self.type = _type
        self.legs = legs

    def eat(self):
        if self.name == 'Dog':
            print("Animal eats meat")
        else:
            print("Animal eats grass")
    def walk(self):
        print("Animal walks")

    def __str__(self):
        return self.name;

a = Animal(name = 'Dog',habitat = 'Land', _type = 'omnivorous')
b = Animal(name = 'Kangaroo', habitat = 'Land', _type = 'herbivorous', legs=2)
print(type(a))
print(a.name, a.legs, a.type, a.habitat)
a.eat()
a.walk()
b.eat()
b.walk()
print(a.__doc__)
print(a)