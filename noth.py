class player:
    def __init__(self,st):
        self.st =st
    def walk(self):
        print('walk')


class defender(player):
    pass


class attacker(player):
    def attack(self):
        print(f"{self.st} attacks")

attack =attacker("younis")
attack.attack()

