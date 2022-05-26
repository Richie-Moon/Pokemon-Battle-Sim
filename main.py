import csv
import damage_calc
import pokemon_move_class


# Create moves for testing
vine_whip = pokemon_move_class.Move('Vine Whip', 45, 'grass', 'Physical')
ember = pokemon_move_class.Move('Ember', 40, 'fire', 'Special')


# TODO Finish asking the user for the moves that they want on their pokemon.
# TODO List all possible moves if asked.
def pick_moves(number):
    with open('movesets.csv', mode='r') as data:
        reader = list(csv.DictReader(data))

        while True:
            user_move = input(f"Please enter move {number}: ")


def pick_pokemon(number) -> pokemon_move_class.Pokemon:
    with open('pokedex.csv', mode='r') as data:
        reader = list(csv.DictReader(data))

        while True:
            user_pokemon = input(f"Pokemon {number}: ").capitalize().strip()
            for pokemon in reader:
                if pokemon['name'] == user_pokemon:
                    print(f"You chose {pokemon['name']}!")

                    return pokemon_move_class.Pokemon(pokemon['name'],
                                                      pokemon['type_1'],
                                                      pokemon['type_2'],
                                                      pokemon['hp'],
                                                      pokemon['atk'],
                                                      pokemon['spatk'],
                                                      pokemon['df'],
                                                      pokemon['spdf'],
                                                      pokemon['spd'],
                                                      pokemon[])
                else:
                    pass
            print('No Pokemon found. ')


users_pokemon = []
for i in range(1, 7):
    picked_pokemon = pick_pokemon(i)
    users_pokemon.append(picked_pokemon)

print(users_pokemon)
