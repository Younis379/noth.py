class Person:
    def __init__(self,name):
        self.name = name

    def talking(self):
        print(f"salam i'm {self.name}")


var = Person("younis")
print(var.talking())

vari2 = Person("ibrahim")
print(vari2.name)
