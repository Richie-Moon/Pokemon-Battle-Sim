IMMUNE = 0
NOT_EFF = 0.5
NEUTRAL = 1
SUPER_EFF = 2

attack_type = {'Normal': {'Normal': NEUTRAL, 'Fighting': NEUTRAL,
                          'Flying': NEUTRAL, 'Poison': NEUTRAL,
                          'Ground': NEUTRAL, 'Rock': NOT_EFF, 'Bug': NEUTRAL,
                          'Ghost': IMMUNE, 'Steel': NOT_EFF, 'Fire': NEUTRAL,
                          'Water': NEUTRAL, 'Grass': NEUTRAL,
                          'Electric': NEUTRAL, 'Psychic': NEUTRAL,
                          'Ice': NEUTRAL, 'Dragon': NEUTRAL, 'Dark': NEUTRAL,
                          'Fairy': NEUTRAL},

               'Fighting': {'Normal': SUPER_EFF, 'Fighting': NEUTRAL,
                            'Flying': NOT_EFF, 'Poison': NOT_EFF,
                            'Ground': NEUTRAL, 'Rock': SUPER_EFF,
                            'Bug': NOT_EFF, 'Ghost': IMMUNE,
                            'Steel': SUPER_EFF, 'Fire': NEUTRAL,
                            'Water': NEUTRAL, 'Grass': NEUTRAL,
                            'Electric': NEUTRAL, 'Psychic': NOT_EFF,
                            'Ice': SUPER_EFF, 'Dragon': NEUTRAL,
                            'Dark': SUPER_EFF, 'Fairy': NOT_EFF},

               'Flying': {'Normal': NEUTRAL, 'Fighting': SUPER_EFF,
                          'Flying': NEUTRAL, 'Poison': NEUTRAL,
                          'Ground': NEUTRAL, 'Rock': NOT_EFF,
                          'Bug': SUPER_EFF, 'Ghost': NEUTRAL,
                          'Steel': NOT_EFF, 'Fire': NEUTRAL,
                          'Water': NEUTRAL, 'Grass': SUPER_EFF,
                          'Electric': SUPER_EFF, 'Psychic': NEUTRAL,
                          'Ice': NEUTRAL, 'Dragon': NEUTRAL,
                          'Dark': NEUTRAL, 'Fairy': NEUTRAL},

               'Poison': {'Normal': NEUTRAL, 'Fighting': NEUTRAL,
                          'Flying': NEUTRAL, 'Poison': NOT_EFF,
                          'Ground': NOT_EFF, 'Rock': NOT_EFF, 'Bug': NEUTRAL,
                          'Ghost': NOT_EFF, 'Steel': IMMUNE, 'Fire': NEUTRAL,
                          'Water': NEUTRAL, 'Grass': SUPER_EFF,
                          'Electric': NEUTRAL, 'Psychic': NEUTRAL,
                          'Ice': NEUTRAL, 'Dragon': NEUTRAL, 'Dark': NEUTRAL,
                          'Fairy': SUPER_EFF},

               'Ground': {'Normal': NEUTRAL, 'Fighting': NEUTRAL,
                          'Flying': IMMUNE, 'Poison': SUPER_EFF,
                          'Ground': NEUTRAL, 'Rock': SUPER_EFF, 'Bug': NOT_EFF,
                          'Ghost': NEUTRAL, 'Steel': SUPER_EFF,
                          'Fire': SUPER_EFF, 'Water': NEUTRAL,
                          'Grass': NOT_EFF, 'Electric': SUPER_EFF,
                          'Psychic': NEUTRAL, 'Ice': NEUTRAL,
                          'Dragon': NEUTRAL, 'Dark': NEUTRAL,
                          'Fairy': NEUTRAL},

               'Rock': {'Normal': NEUTRAL, 'Fighting': NOT_EFF,
                        'Flying': SUPER_EFF, 'Poison': NEUTRAL,
                        'Ground': NOT_EFF, 'Rock': NEUTRAL, 'Bug': SUPER_EFF,
                        'Ghost': NEUTRAL, 'Steel': NOT_EFF, 'Fire': SUPER_EFF,
                        'Water': NEUTRAL, 'Grass': NEUTRAL,
                        'Electric': NEUTRAL, 'Psychic': NEUTRAL,
                        'Ice': SUPER_EFF, 'Dragon': NEUTRAL, 'Dark': NEUTRAL,
                        'Fairy': NEUTRAL},

               'Bug': {'Normal': NEUTRAL, 'Fighting': NOT_EFF,
                       'Flying': NOT_EFF, 'Poison': NOT_EFF, 'Ground': NEUTRAL,
                       'Rock': NEUTRAL, 'Bug': NEUTRAL, 'Ghost': NOT_EFF,
                       'Steel': NOT_EFF, 'Fire': NOT_EFF, 'Water': NEUTRAL,
                       'Grass': SUPER_EFF, 'Electric': NEUTRAL,
                       'Psychic': SUPER_EFF, 'Ice': NEUTRAL, 'Dragon': NEUTRAL,
                       'Dark': SUPER_EFF, 'Fairy': NOT_EFF},

               'Ghost': {'Normal': IMMUNE, 'Fighting': NEUTRAL,
                         'Flying': NEUTRAL, 'Poison': NEUTRAL,
                         'Ground': NEUTRAL, 'Rock': NEUTRAL, 'Bug': NEUTRAL,
                         'Ghost': SUPER_EFF, 'Steel': NEUTRAL, 'Fire': NEUTRAL,
                         'Water': NEUTRAL, 'Grass': NEUTRAL,
                         'Electric': NEUTRAL, 'Psychic': SUPER_EFF,
                         'Ice': NEUTRAL, 'Dragon': NEUTRAL, 'Dark': NOT_EFF,
                         'Fairy': NEUTRAL},

               'Steel': {'Normal': NEUTRAL, 'Fighting': NEUTRAL,
                         'Flying': NEUTRAL, 'Poison': NEUTRAL,
                         'Ground': NEUTRAL, 'Rock': SUPER_EFF, 'Bug': NEUTRAL,
                         'Ghost': NEUTRAL, 'Steel': NOT_EFF, 'Fire': NOT_EFF,
                         'Water': NOT_EFF, 'Grass': NEUTRAL,
                         'Electric': NOT_EFF, 'Psychic': NEUTRAL,
                         'Ice': SUPER_EFF, 'Dragon': NEUTRAL, 'Dark': NEUTRAL,
                         'Fairy': SUPER_EFF},

               'Fire': {'Normal': NEUTRAL, 'Fighting': NEUTRAL,
                        'Flying': NEUTRAL, 'Poison': NEUTRAL,
                        'Ground': NEUTRAL, 'Rock': NOT_EFF, 'Bug': SUPER_EFF,
                        'Ghost': NEUTRAL, 'Steel': SUPER_EFF, 'Fire': NOT_EFF,
                        'Water': NOT_EFF, 'Grass': SUPER_EFF,
                        'Electric': NEUTRAL, 'Psychic': NEUTRAL,
                        'Ice': SUPER_EFF, 'Dragon': NOT_EFF, 'Dark': NEUTRAL,
                        'Fairy': NEUTRAL},

               'Water': {'Normal': NEUTRAL, 'Fighting': NEUTRAL,
                         'Flying': NEUTRAL, 'Poison': NEUTRAL,
                         'Ground': SUPER_EFF, 'Rock': SUPER_EFF,
                         'Bug': NEUTRAL, 'Ghost': NEUTRAL, 'Steel': NEUTRAL,
                         'Fire': SUPER_EFF, 'Water': NOT_EFF, 'Grass': NOT_EFF,
                         'Electric': NEUTRAL, 'Psychic': NEUTRAL,
                         'Ice': NEUTRAL, 'Dragon': NOT_EFF, 'Dark': NEUTRAL,
                         'Fairy': NEUTRAL},

               'Grass': {'Normal': NEUTRAL, 'Fighting': NEUTRAL,
                         'Flying': NOT_EFF, 'Poison': NOT_EFF,
                         'Ground': SUPER_EFF, 'Rock': SUPER_EFF,
                         'Bug': NOT_EFF, 'Ghost': NEUTRAL, 'Steel': NOT_EFF,
                         'Fire': NOT_EFF, 'Water': SUPER_EFF, 'Grass': NOT_EFF,
                         'Electric': NEUTRAL, 'Psychic': NEUTRAL,
                         'Ice': NEUTRAL, 'Dragon': NOT_EFF, 'Dark': NEUTRAL,
                         'Fairy': NEUTRAL},

               'Electric': {'Normal': NEUTRAL, 'Fighting': SUPER_EFF,
                            'Flying': NEUTRAL, 'Poison': NEUTRAL,
                            'Ground': IMMUNE, 'Rock': NEUTRAL, 'Bug': NEUTRAL,
                            'Ghost': NEUTRAL, 'Steel': NEUTRAL,
                            'Fire': NEUTRAL, 'Water': SUPER_EFF,
                            'Grass': NOT_EFF, 'Electric': NOT_EFF,
                            'Psychic': NEUTRAL, 'Ice': NEUTRAL,
                            'Dragon': NOT_EFF, 'Dark': NEUTRAL,
                            'Fairy': NEUTRAL},

               'Psychic': {'Normal': NEUTRAL, 'Fighting': SUPER_EFF,
                           'Flying': NEUTRAL, 'Poison': SUPER_EFF,
                           'Ground': NEUTRAL, 'Rock': NEUTRAL, 'Bug': NEUTRAL,
                           'Ghost': NEUTRAL, 'Steel': NOT_EFF, 'Fire': NEUTRAL,
                           'Water': NEUTRAL, 'Grass': NEUTRAL,
                           'Electric': NEUTRAL, 'Psychic': NOT_EFF,
                           'Ice': NEUTRAL, 'Dragon': NEUTRAL, 'Dark': IMMUNE,
                           'Fairy': NEUTRAL},

               'Ice': {'Normal': NEUTRAL, 'Fighting': NEUTRAL,
                       'Flying': SUPER_EFF, 'Poison': NEUTRAL,
                       'Ground': SUPER_EFF, 'Rock': NEUTRAL, 'Bug': NEUTRAL,
                       'Ghost': NEUTRAL, 'Steel': NOT_EFF, 'Fire': NOT_EFF,
                       'Water': NOT_EFF, 'Grass': SUPER_EFF,
                       'Electric': NEUTRAL, 'Psychic': NEUTRAL, 'Ice': NOT_EFF,
                       'Dragon': SUPER_EFF, 'Dark': NEUTRAL, 'Fairy': NEUTRAL},

               'Dragon': {'Normal': NEUTRAL, 'Fighting': NEUTRAL,
                          'Flying': NEUTRAL, 'Poison': NEUTRAL,
                          'Ground': NEUTRAL, 'Rock': NEUTRAL, 'Bug': NEUTRAL,
                          'Ghost': NEUTRAL, 'Steel': NOT_EFF, 'Fire': NEUTRAL,
                          'Water': NEUTRAL, 'Grass': NEUTRAL,
                          'Electric': NEUTRAL, 'Psychic': NEUTRAL,
                          'Ice': NEUTRAL, 'Dragon': SUPER_EFF, 'Dark': NEUTRAL,
                          'Fairy': IMMUNE},

               'Dark': {'Normal': NEUTRAL, 'Fighting': NOT_EFF,
                        'Flying': NEUTRAL, 'Poison': NEUTRAL,
                        'Ground': NEUTRAL, 'Rock': NEUTRAL, 'Bug': NEUTRAL,
                        'Ghost': SUPER_EFF, 'Steel': NEUTRAL, 'Fire': NEUTRAL,
                        'Water': NEUTRAL, 'Grass': NEUTRAL,
                        'Electric': NEUTRAL, 'Psychic': SUPER_EFF,
                        'Ice': NEUTRAL, 'Dragon': NEUTRAL, 'Dark': NOT_EFF,
                        'Fairy': NOT_EFF},

               'Fairy': {'Normal': NEUTRAL, 'Fighting': SUPER_EFF,
                         'Flying': NEUTRAL, 'Poison': NOT_EFF,
                         'Ground': NEUTRAL, 'Rock': NEUTRAL, 'Bug': NEUTRAL,
                         'Ghost': NEUTRAL, 'Steel': NOT_EFF, 'Fire': NOT_EFF,
                         'Water': NEUTRAL, 'Grass': NEUTRAL,
                         'Electric': NEUTRAL, 'Psychic': NEUTRAL,
                         'Ice': NEUTRAL, 'Dragon': SUPER_EFF,
                         'Dark': SUPER_EFF, 'Fairy': NEUTRAL}
               }


def type_multiplier(move_type, type1, type2):
    """This function will calculate the multiplier. This multiplier will be
    used in the damage formula. It takes the move type, and the types of the
    Pokemon defending the attack as parameters. It then uses the nested dict
    above to calculate the multiplier and return the value. Raise KeyError
    if the move type doesn't exist. """
    try:
        if type2 == 'None':
            return attack_type[move_type][type1]
        else:
            multiplier1 = attack_type[move_type][type1]
            multiplier2 = attack_type[move_type][type2]
            return multiplier1 * multiplier2
    except KeyError:
        raise KeyError(f"Pokemon type not found. "
                       f"move_type: {move_type}, type1: {type1}, "
                       f"type2: {type2}")

