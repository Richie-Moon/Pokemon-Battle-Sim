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

               'rock': {'normal': NEUTRAL, 'fighting': NOT_EFF, 'flying': SUPER_EFF, 'poison': NEUTRAL, 'ground': NOT_EFF, 'rock': NEUTRAL, 'bug': SUPER_EFF, 'ghost': NEUTRAL, 'steel': NEUTRAL, 'fire': NEUTRAL, 'water': NEUTRAL, 'grass': NEUTRAL, 'electric': NEUTRAL, 'psychic': NEUTRAL, 'ice': NEUTRAL, 'dragon': NEUTRAL, 'dark': NEUTRAL, 'fairy': NEUTRAL}
               }
