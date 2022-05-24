IMMUNE = 0
NOT_EFF = 0.5
NEUTRAL = 1
SUPER_EFF = 2

attack_type = {'normal': {'normal': NEUTRAL, 'fighting': NEUTRAL,
                          'flying': NEUTRAL, 'poison': NEUTRAL,
                          'ground': NEUTRAL, 'rock': NOT_EFF, 'bug': NEUTRAL,
                          'ghost': IMMUNE, 'steel': NOT_EFF, 'fire': NEUTRAL,
                          'water': NEUTRAL, 'grass': NEUTRAL,
                          'electric': NEUTRAL, 'psychic': NEUTRAL,
                          'ice': NEUTRAL, 'dragon': NEUTRAL, 'dark': NEUTRAL,
                          'fairy': NEUTRAL},

               'fighting': {'normal': SUPER_EFF, 'fighting': NEUTRAL,
                            'flying': NOT_EFF, 'poison': NOT_EFF,
                            'ground': NEUTRAL, 'rock': SUPER_EFF,
                            'bug': NOT_EFF, 'ghost': IMMUNE,
                            'steel': SUPER_EFF, 'fire': NEUTRAL,
                            'water': NEUTRAL, 'grass': NEUTRAL,
                            'electric': NEUTRAL, 'psychic': NOT_EFF,
                            'ice': SUPER_EFF, 'dragon': NEUTRAL,
                            'dark': SUPER_EFF, 'fairy': NOT_EFF},

               'flying': {'normal': NEUTRAL, 'fighting': SUPER_EFF,
                          'flying': NEUTRAL, 'poison': NEUTRAL,
                          'ground': NEUTRAL, 'rock': NOT_EFF,
                          'bug': SUPER_EFF, 'ghost': NEUTRAL,
                          'steel': NOT_EFF, 'fire': NEUTRAL,
                          'water': NEUTRAL, 'grass': SUPER_EFF,
                          'electric': SUPER_EFF, 'psychic': NEUTRAL,
                          'ice': NEUTRAL, 'dragon': NEUTRAL,
                          'dark': NEUTRAL, 'fairy': NEUTRAL},

               'poison': {'normal': NEUTRAL, 'fighting': NEUTRAL,
                          'flying': NEUTRAL, 'poison': NOT_EFF,
                          'ground': NOT_EFF, 'rock': NOT_EFF, 'bug': NEUTRAL,
                          'ghost': NOT_EFF, 'steel': IMMUNE, 'fire': NEUTRAL,
                          'water': NEUTRAL, 'grass': SUPER_EFF,
                          'electric': NEUTRAL, 'psychic': NEUTRAL,
                          'ice': NEUTRAL, 'dragon': NEUTRAL, 'dark': NEUTRAL,
                          'fairy': SUPER_EFF},

               'ground': {'normal': NEUTRAL, 'fighting': NEUTRAL,
                          'flying': IMMUNE, 'poison': SUPER_EFF,
                          'ground': NEUTRAL, 'rock': SUPER_EFF, 'bug': NOT_EFF,
                          'ghost': NEUTRAL, 'steel': SUPER_EFF,
                          'fire': SUPER_EFF, 'water': NEUTRAL,
                          'grass': NOT_EFF, 'electric': SUPER_EFF,
                          'psychic': NEUTRAL, 'ice': NEUTRAL,
                          'dragon': NEUTRAL, 'dark': NEUTRAL,
                          'fairy': NEUTRAL},

               'rock': {'normal': NEUTRAL, 'fighting': NOT_EFF,
                        'flying': SUPER_EFF, 'poison': NEUTRAL,
                        'ground': NOT_EFF, 'rock': NEUTRAL, 'bug': SUPER_EFF,
                        'ghost': NEUTRAL, 'steel': NOT_EFF, 'fire': SUPER_EFF,
                        'water': NEUTRAL, 'grass': NEUTRAL,
                        'electric': NEUTRAL, 'psychic': NEUTRAL,
                        'ice': SUPER_EFF, 'dragon': NEUTRAL, 'dark': NEUTRAL,
                        'fairy': NEUTRAL},

               'bug': {'normal': NEUTRAL, 'fighting': NOT_EFF,
                       'flying': NOT_EFF, 'poison': NOT_EFF, 'ground': NEUTRAL,
                       'rock': NEUTRAL, 'bug': NEUTRAL, 'ghost': NOT_EFF,
                       'steel': NOT_EFF, 'fire': NOT_EFF, 'water': NEUTRAL,
                       'grass': SUPER_EFF, 'electric': NEUTRAL,
                       'psychic': SUPER_EFF, 'ice': NEUTRAL, 'dragon': NEUTRAL,
                       'dark': SUPER_EFF, 'fairy': NOT_EFF},

               'ghost': {'normal': IMMUNE, 'fighting': NEUTRAL,
                         'flying': NEUTRAL, 'poison': NEUTRAL,
                         'ground': NEUTRAL, 'rock': NEUTRAL, 'bug': NEUTRAL,
                         'ghost': SUPER_EFF, 'steel': NEUTRAL, 'fire': NEUTRAL,
                         'water': NEUTRAL, 'grass': NEUTRAL,
                         'electric': NEUTRAL, 'psychic': SUPER_EFF,
                         'ice': NEUTRAL, 'dragon': NEUTRAL, 'dark': NOT_EFF,
                         'fairy': NEUTRAL},

               'steel': {'normal': NEUTRAL, 'fighting': NEUTRAL,
                         'flying': NEUTRAL, 'poison': NEUTRAL,
                         'ground': NEUTRAL, 'rock': SUPER_EFF, 'bug': NEUTRAL,
                         'ghost': NEUTRAL, 'steel': NOT_EFF, 'fire': NOT_EFF,
                         'water': NOT_EFF, 'grass': NEUTRAL,
                         'electric': NOT_EFF, 'psychic': NEUTRAL,
                         'ice': SUPER_EFF, 'dragon': NEUTRAL, 'dark': NEUTRAL,
                         'fairy': SUPER_EFF},

               'fire': {'normal': NEUTRAL, 'fighting': NEUTRAL,
                        'flying': NEUTRAL, 'poison': NEUTRAL,
                        'ground': NEUTRAL, 'rock': NOT_EFF, 'bug': SUPER_EFF,
                        'ghost': NEUTRAL, 'steel': SUPER_EFF, 'fire': NOT_EFF,
                        'water': NOT_EFF, 'grass': SUPER_EFF,
                        'electric': NEUTRAL, 'psychic': NEUTRAL,
                        'ice': SUPER_EFF, 'dragon': NOT_EFF, 'dark': NEUTRAL,
                        'fairy': NEUTRAL},

               'water': {'normal': NEUTRAL, 'fighting': NEUTRAL,
                         'flying': NEUTRAL, 'poison': NEUTRAL,
                         'ground': SUPER_EFF, 'rock': SUPER_EFF,
                         'bug': NEUTRAL, 'ghost': NEUTRAL, 'steel': NEUTRAL,
                         'fire': SUPER_EFF, 'water': NOT_EFF, 'grass': NOT_EFF,
                         'electric': NEUTRAL, 'psychic': NEUTRAL,
                         'ice': NEUTRAL, 'dragon': NOT_EFF, 'dark': NEUTRAL,
                         'fairy': NEUTRAL},

               'grass': {'normal': NEUTRAL, 'fighting': NEUTRAL,
                         'flying': NOT_EFF, 'poison': NOT_EFF,
                         'ground': SUPER_EFF, 'rock': SUPER_EFF,
                         'bug': NOT_EFF, 'ghost': NEUTRAL, 'steel': NOT_EFF,
                         'fire': NOT_EFF, 'water': SUPER_EFF, 'grass': NOT_EFF,
                         'electric': NEUTRAL, 'psychic': NEUTRAL,
                         'ice': NEUTRAL, 'dragon': NOT_EFF, 'dark': NEUTRAL,
                         'fairy': NEUTRAL},

               'electric': {'normal': NEUTRAL, 'fighting': SUPER_EFF,
                            'flying': NEUTRAL, 'poison': NEUTRAL,
                            'ground': IMMUNE, 'rock': NEUTRAL, 'bug': NEUTRAL,
                            'ghost': NEUTRAL, 'steel': NEUTRAL,
                            'fire': NEUTRAL, 'water': SUPER_EFF,
                            'grass': NOT_EFF, 'electric': NOT_EFF,
                            'psychic': NEUTRAL, 'ice': NEUTRAL,
                            'dragon': NOT_EFF, 'dark': NEUTRAL,
                            'fairy': NEUTRAL},

               'psychic': {'normal': NEUTRAL, 'fighting': SUPER_EFF,
                           'flying': NEUTRAL, 'poison': SUPER_EFF,
                           'ground': NEUTRAL, 'rock': NEUTRAL, 'bug': NEUTRAL,
                           'ghost': NEUTRAL, 'steel': NOT_EFF, 'fire': NEUTRAL,
                           'water': NEUTRAL, 'grass': NEUTRAL,
                           'electric': NEUTRAL, 'psychic': NOT_EFF,
                           'ice': NEUTRAL, 'dragon': NEUTRAL, 'dark': IMMUNE,
                           'fairy': NEUTRAL},

               'ice': {'normal': NEUTRAL, 'fighting': NEUTRAL,
                       'flying': SUPER_EFF, 'poison': NEUTRAL,
                       'ground': SUPER_EFF, 'rock': NEUTRAL, 'bug': NEUTRAL,
                       'ghost': NEUTRAL, 'steel': NOT_EFF, 'fire': NOT_EFF,
                       'water': NOT_EFF, 'grass': SUPER_EFF,
                       'electric': NEUTRAL, 'psychic': NEUTRAL, 'ice': NOT_EFF,
                       'dragon': SUPER_EFF, 'dark': NEUTRAL, 'fairy': NEUTRAL},

               'dragon': {'normal': NEUTRAL, 'fighting': NEUTRAL,
                          'flying': NEUTRAL, 'poison': NEUTRAL,
                          'ground': NEUTRAL, 'rock': NEUTRAL, 'bug': NEUTRAL,
                          'ghost': NEUTRAL, 'steel': NOT_EFF, 'fire': NEUTRAL,
                          'water': NEUTRAL, 'grass': NEUTRAL,
                          'electric': NEUTRAL, 'psychic': NEUTRAL,
                          'ice': NEUTRAL, 'dragon': SUPER_EFF, 'dark': NEUTRAL,
                          'fairy': IMMUNE},

               'dark': {'normal': NEUTRAL, 'fighting': NOT_EFF,
                        'flying': NEUTRAL, 'poison': NEUTRAL,
                        'ground': NEUTRAL, 'rock': NEUTRAL, 'bug': NEUTRAL,
                        'ghost': SUPER_EFF, 'steel': NEUTRAL, 'fire': NEUTRAL,
                        'water': NEUTRAL, 'grass': NEUTRAL,
                        'electric': NEUTRAL, 'psychic': SUPER_EFF,
                        'ice': NEUTRAL, 'dragon': NEUTRAL, 'dark': NOT_EFF,
                        'fairy': NOT_EFF},

               'fairy': {'normal': NEUTRAL, 'fighting': SUPER_EFF,
                         'flying': NEUTRAL, 'poison': NOT_EFF,
                         'ground': NEUTRAL, 'rock': NEUTRAL, 'bug': NEUTRAL,
                         'ghost': NEUTRAL, 'steel': NOT_EFF, 'fire': NOT_EFF,
                         'water': NEUTRAL, 'grass': NEUTRAL,
                         'electric': NEUTRAL, 'psychic': NEUTRAL,
                         'ice': NEUTRAL, 'dragon': SUPER_EFF,
                         'dark': SUPER_EFF, 'fairy': NEUTRAL}
               }


def type_multiplier(move_type, type1, type2):
    # TODO Write comment for this function.
    try:
        if type2 == 'None':
            return attack_type[move_type][type1]
        else:
            multiplier1 = attack_type[move_type][type1]
            multiplier2 = attack_type[move_type][type2]
            return multiplier1 * multiplier2
    except KeyError:
        raise KeyError(f"Pokemon type not found. "
                       f"\nmove_type: {move_type}, type1: {type1}, "
                       f"type2: {type2}")

