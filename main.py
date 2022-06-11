import csv
import damage_calc
import random
import pokemon_move_class


def pick_moves(pokemon, number: int, used_moves: list) -> pokemon_move_class.\
        Move:
    with open('movesets.csv', mode='r') as data:
        reader = list(csv.DictReader(data))
        moves_list = set({})

        while True:
            user_move = input(f"Please enter move {number} (Type 'L' to list "
                              f"all possible moves): ").title().strip()
            for move in reader:
                if move['species'] == pokemon:
                    for i in range(1, 175):
                        if move[f'move{i}'] != '' and move[f'move{i}'] not in \
                                used_moves:
                            moves_list.add(move[f'move{i}'].strip())

            with open('moves.csv', mode='r') as move_data:
                moves_reader = list(csv.DictReader(move_data))

                if user_move == 'L':
                    print(", ".join(moves_list))
                elif user_move in used_moves:
                    print('Move already picked. \n')
                elif user_move in moves_list:
                    for pokemon_move in moves_reader:
                        if pokemon_move['name'] == user_move:
                            print(f"Picked {user_move} as move {number}! \n")
                            return pokemon_move_class.Move(
                                pokemon_move['name'],
                                pokemon_move['power'],
                                pokemon_move['type'],
                                pokemon_move['category'],
                                pokemon_move['accuracy'])
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


# users_pokemon = []
# for i in range(1, 7):
#     picked_pokemon = pick_pokemon(i)
#     users_pokemon.append(picked_pokemon)

def pick_computer_moves(move_name) -> pokemon_move_class.Move:
    with open('moves.csv', mode='r') as move_data:
        moves = list(csv.DictReader(move_data))

    for move in moves:
        if move['name'] == move_name:
            return pokemon_move_class.Move(move['name'], move['power'],
                                           move['type'], move['category'],
                                           move['accuracy'])


def pick_computer_pokemon() -> pokemon_move_class.Pokemon:
    with open('pokedex.csv', mode='r') as data:
        pokedex = list(csv.DictReader(data))
    with open('movesets.csv', mode='r') as moveset_data:
        movesets = list(csv.DictReader(moveset_data))

    cont = True
    while cont is True:
        random_index = random.randint(1, 802)
        for pokemon in pokedex:
            if int(pokemon['pokedex_number']) == random_index:
                name = pokemon['name']
                if name != 'Ditto' or name != 'Unown' or name != 'Cosmog' or \
                        name != 'Cosmoem':
                    cont = False

    for moveset in movesets:
        if moveset['species'] == name:
            moves = []
            for i in range(1, 174):
                if moveset[f'move{i}'] != '':
                    moves.append(moveset[f'move{i}'].strip())


            comp_moves = []
            for i in range(4):
                while True:
                    comp_move = pick_computer_moves(random.choice(moves))
                    print(comp_move.name)
                    if comp_move.pwr == '0' or comp_move.pwr == '—':
                        pass
                    else:
                        if comp_move.name in comp_moves:
                            pass
                        else:
                            comp_moves.append(comp_move)
                            break

            return pokemon_move_class.Pokemon(name, pokemon['type_1'],
                                              pokemon['type_2'],
                                              pokemon['hp'], pokemon['atk'],
                                              pokemon['spatk'],
                                              pokemon['df'],
                                              pokemon['spdf'],
                                              pokemon['spd'], comp_moves[0],
                                              comp_moves[1], comp_moves[2],
                                              comp_moves[3])


computers_pokemon = []
for i in range(4):
    computers_pokemon.append(pick_computer_pokemon())
    print(computers_pokemon)
    print(computers_pokemon[i].name)

