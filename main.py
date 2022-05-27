import csv
import damage_calc
import pokemon_move_class


# Create moves for testing
vine_whip = pokemon_move_class.Move('Vine Whip', 45, 'grass', 'Physical')
ember = pokemon_move_class.Move('Ember', 40, 'fire', 'Special')


# TODO Finish asking the user for the moves that they want on their pokemon.
# TODO List all possible moves if asked.
def pick_moves(pokemon, number: int) -> pokemon_move_class.Move:
    with open('movesets.csv', mode='r') as data:
        reader = list(csv.DictReader(data))
        moves_list = []

        while True:
            user_move = input(f"Please enter move {number} (Type 'L' to list "
                              f"all possible moves. ): ").capitalize().strip()
            for move in reader:
                if move['species'] == pokemon:
                    for i in range(1, 175):
                        if move[f'move{i}'] != '':
                            moves_list.append(move[f'move{i}'])
                else:
                    print("No Pokemon exists with that name.")

            with open('moves.csv', mode='r') as move_data:
                moves_reader = list(csv.DictReader(move_data))
                # TODO have to use this file to get move info.
                if user_move == 'L':
                    print(", ".join(moves_list))
                elif user_move in moves_list:
                    print(f"Picked {user_move} as move {number}!")
                    return pokemon_move_class.Move()


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
