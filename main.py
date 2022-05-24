import csv
import damage_calc
import pokemon_moves


# Create moves for testing
vine_whip = pokemon_moves.Move('Vine Whip', 45, 'grass', 'Physical')
ember = pokemon_moves.Move('Ember', 40, 'fire', 'Special')


with open('pokemon_data.csv', mode='r') as data:
    reader = csv.DictReader(data)

    for pokemon in reader:
        if pokemon['name'] == 'Bulbasaur':
            bulbasaur = pokemon_moves.Pokemon(name=pokemon['name'],
                                        type1=pokemon['type1'],
                                        type2=pokemon['type2'],
                                        hp=pokemon['hp'],
                                        atk=pokemon['attack'],
                                        spatk=pokemon['sp_attack'],
                                        df=pokemon['defense'],
                                        spdf=pokemon['sp_defense'],
                                        spd=pokemon['speed'], move1=vine_whip,
                                        move2=None, move3=None, move4=None)

        if pokemon['name'] == 'Charmander':
            charmander = pokemon_moves.Pokemon(name=pokemon['name'],
                                         type1=pokemon['type1'],
                                         type2=pokemon['type2'],
                                         hp=pokemon['hp'],
                                         atk=pokemon['attack'],
                                         spatk=pokemon['sp_attack'],
                                         df=pokemon['defense'],
                                         spdf=pokemon['sp_defense'],
                                         spd=pokemon['speed'], move1=ember,
                                         move2=None, move3=None, move4=None)


dmg = damage_calc.calculate_dmg(bulbasaur, charmander, bulbasaur.move1)
print(dmg)
