class Person:
    def __init__(self,name):
        self.n = name

    def talk(self):
        print(f"Salam my name is {self.n}")


person = Person("younis")
person.talk()

person2 = Person("salma")
person2.talk()