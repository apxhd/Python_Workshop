# Program with a Nepali class and a subclass Newari


class Nepali:
    def __init__(self):
        print("Namaste")


class Newari(Nepali):
    def __init__(self):
        Nepali.__init__(self)
        print("Jujulapa")


n1 = Newari()
