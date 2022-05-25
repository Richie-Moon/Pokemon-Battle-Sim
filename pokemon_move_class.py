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


class Move:
    def __init__(self, name, pwr, typ, category):
        self.name = name
        self.pwr = pwr
        self.category = category
        self.typ = typ
