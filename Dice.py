import random


class Dice:
    def roll(self):
        first = random.randint(1, 20)
        second = random.randint(1, 20)
        return first, second


dice = Dice()
print(dice.roll())
