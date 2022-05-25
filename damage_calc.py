import pokemon_moves
import random
import pokemon_types


# Damage Formula can be found at https://bulbapedia.bulbagarden.net/wiki/Damage
# Only using the values that I will incorporate into the program. (Not using
# ZMove, Targets, weather, etc).
def calculate_dmg(poke1: pokemon_moves.Pokemon, poke2: pokemon_moves.Pokemon,
                  move: pokemon_moves.Move):
    # Calculate the critical hit damage multiplier.
    crit_chance = random.randint(1, 25)
    if crit_chance == 1:
        crit_dmg = 1.5
    else:
        crit_dmg = 1

    # All Pokémon levels are set to 50.
    LEVEL = 50

    # Calculate the random part of the formula. It is a multiplier. A random
    # value between 85 and 100 is chosen, then divided by 100.
    random_value = random.randint(85, 100) / 100

    # Calculate if the move is Special or Physical (Category) and set attack
    # defence values based on the category.
    if move.category == 'Physical':
        attack = int(poke1.atk)
        defence = int(poke2.df)
    else:
        attack = int(poke1.spatk)
        defence = int(poke2.spdf)

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

    damage = int(
        ((((2 * LEVEL // 5) + 2) * move.pwr * (attack // defence) // 50)
         + 2) * crit_dmg * random_value * STAB * type_multiplier)
    return damage
