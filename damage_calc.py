import pokemon_move_class
import random
import pokemon_types


# Damage Formula can be found at https://bulbapedia.bulbagarden.net/wiki/Damage
# Only using the values that I will incorporate into the program. (Not using
# ZMove, Targets, weather, etc).
def calculate_dmg(poke1: pokemon_move_class.Pokemon,
                  poke2: pokemon_move_class.Pokemon,
                  move: pokemon_move_class.Move):
    """Calculate the damgage that 1 pokemon would deal to another, using the
    damage formula. """

    # Calculate the critical hit damage multiplier.
    crit_chance = random.randint(1, 25)
    if crit_chance == 1:
        crit_dmg = 1.5
        print("Crit!")
    else:
        crit_dmg = 1

    # All Pokémon levels are set to 50 (In competitive Pokemon).
    LEVEL = 50

    # Calculate the random part of the formula. It is a multiplier. A random
    # value between 85 and 100 is chosen, then divided by 100.
    random_value = random.randint(85, 100) / 100

    # Calculate if the move is Special or Physical (Category) and set attack
    # defence values based on the category. Effective stat calculation formula
    # can be found here: https://pokemon.fandom.com/wiki/Statistics#Formula
    IV = 31
    if move.category == 'Physical':
        attack = int(0.01 * (2 * poke1.atk + IV) * LEVEL) + 5
        defence = int(0.01 * (2 * poke2.df + IV) * LEVEL) + 5
    elif move.category == 'Special':
        attack = int(0.01 * (2 * poke1.spatk + IV) * LEVEL) + 5
        defence = int(0.01 * (2 * poke2.spdf + IV) * LEVEL) + 5

    # Calculate whether the type of the move used is the same type as one of
    # the Pokémon types. This adds a 1.5x multiplier called Same Type Attack
    # Bonus (STAB)
    if move.typ == poke1.type1 or move.typ == poke1.type2:
        STAB = 1.5
    else:
        STAB = 1

    # Calculate Type Effectiveness using pokemon_types.py
    type_multiplier = pokemon_types.type_multiplier(move.typ, poke2.type1,
                                                    poke2.type2)
    if type_multiplier >= 2:
        print("Super Effective!")
    elif type_multiplier <= 0.5:
        print("Not very effective...")

    # damage is calculated line by line as after each calculation, all number
    # are rounded down to an integer. First line is an int as all values are
    # whole numbers, and we are using floor division.

    damage = (((2 * LEVEL // 5) + 2) * move.pwr * attack // defence // 50) + 2
    damage = int(damage * crit_dmg)
    damage = int(damage * random_value)
    damage = int(damage * STAB)
    damage = int(damage * type_multiplier)
    return damage
