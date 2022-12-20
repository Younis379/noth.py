import random
class Dice:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def roll(self):
       roll1 = random.randint(self.x, self.y)
       roll2 = random.randint(self.x, self.y)

       print(f"({roll1},{roll2})")


dice =Dice(1, 20)
dice.roll()