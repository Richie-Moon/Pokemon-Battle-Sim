import csv
import damage_calc
import pokemon_move_class

# Create moves for testing
vine_whip = pokemon_move_class.Move('Vine Whip', 45, 'grass', 'Physical')
ember = pokemon_move_class.Move('Ember', 40, 'fire', 'Special')


def pick_moves(pokemon, number: int, used_moves: list) -> pokemon_move_class.Move:
    with open('movesets.csv', mode='r') as data:
        reader = list(csv.DictReader(data))
        moves_list = set({})

        while True:
            user_move = input(f"Please enter move {number} (Type 'L' to list "
                              f"all possible moves): ").title().strip()
            for move in reader:
                if move['species'] == pokemon:
                    for i in range(1, 175):
                        if move[f'move{i}'] != '' and move[f'move{i}'] not in used_moves:
                            moves_list.add(move[f'move{i}'].strip())
                            print(moves_list)

            with open('moves.csv', mode='r') as move_data:
                moves_reader = list(csv.DictReader(move_data))

                if user_move == 'L':
                    print(", ".join(moves_list))
                elif user_move in used_moves:
                    print(used_moves)
                    print('Move already picked. \n')
                elif user_move in moves_list:
                    for pokemon_move in moves_reader:
                        if pokemon_move['name'] == user_move:
                            print(f"Picked {user_move} as move {number}! \n")
                            return pokemon_move_class.Move(
                                pokemon_move['name'],
                                pokemon_move['power'],
                                pokemon_move['type'],
                                pokemon_move['category'])
                else:
                    print("That move doesn't exist. ")


def pick_pokemon(number) -> pokemon_move_class.Pokemon:
    with open('pokedex.csv', mode='r') as data:
        reader = list(csv.DictReader(data))

        while True:
            user_pokemon = input(f"Pokemon {number}: ").title().strip()
            for pokemon in reader:
                if pokemon['name'] == user_pokemon:
                    print(f"You chose {pokemon['name']}!")

                    moves = []

                    move1 = pick_moves(pokemon['name'], 1, moves)
                    moves.append(move1.name)
                    move2 = pick_moves(pokemon['name'], 2, moves)
                    moves.append(move2.name)
                    move3 = pick_moves(pokemon['name'], 3, moves)
                    moves.append(move3.name)
                    move4 = pick_moves(pokemon['name'], 4, moves)
                    moves.append(move4.name)

                    return pokemon_move_class.Pokemon(pokemon['name'],
                                                      pokemon['type_1'],
                                                      pokemon['type_2'],
                                                      pokemon['hp'],
                                                      pokemon['atk'],
                                                      pokemon['spatk'],
                                                      pokemon['df'],
                                                      pokemon['spdf'],
                                                      pokemon['spd'],
                                                      move1, move2, move3,
                                                      move4)
                else:
                    pass
            print('No Pokemon found. ')


users_pokemon = []
for i in range(1, 7):
    picked_pokemon = pick_pokemon(i)
    users_pokemon.append(picked_pokemon)

print(users_pokemon)
