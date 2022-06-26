import random


class Pokemon:
    def __init__(self, name, type1, type2, hp, atk, spatk, df, spdf, spd,
                 move1, move2, move3, move4):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
        self.atk = atk
        self.spatk = spatk
        self.df = df
        self.spdf = spdf
        self.spd = spd
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4

    def random_move(self):
        random_int = random.randint(1, 4)
        if random_int == 1:
            return self.move1
        if random_int == 2:
            return self.move2
        if random_int == 3:
            return self.move3
        if random_int == 4:
            return self.move4


class Move:
    def __init__(self, name, pwr, typ, category, accuracy):
        self.name = name
        self.pwr = pwr
        self.category = category
        self.typ = typ
        self.accuracy = accuracy
