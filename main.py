import csv
import damage_calc
import random
import pokemon_move_class


def pick_moves(pokemon, number: int, used_moves: list) -> pokemon_move_class. \
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


move1 = pokemon_move_class.Move('Surf', 90, "Water", 'Special', 100)
move2 = pokemon_move_class.Move('Night Slash', 70, 'Dark', 'Physical', 100)
move3 = pokemon_move_class.Move('Hydro Pump', 110, 'Water', 'Physical', 80)
move4 = pokemon_move_class.Move("Ice Beam", 90, 'Ice', 'Special', 100)

users_pokemon = [pokemon_move_class.Pokemon('Greninja', 'Water', 'Dark', 1,
                                            1, 1, 1, 1, 1,
                                            move1, move2, move3, move4),
                 pokemon_move_class.Pokemon('Pikachu', 'Electric', 'None', '1',
                                            '1', '1', '1', '1', '1',
                                            None, None, None, None),
                 pokemon_move_class.Pokemon('Pichu', 'Electric', 'None', '1',
                                            '1', '1', '1', '1', '1',
                                            None, None, None, None),
                 pokemon_move_class.Pokemon('Charizard', 'Fire', 'Flying', '1',
                                            '1', '1', '1', '1', '1',
                                            None, None, None, None),
                 pokemon_move_class.Pokemon('Venusaur', 'Grass', 'Poison', '1',
                                            '1', '1', '1', '1', '1',
                                            None, None, None, None),
                 pokemon_move_class.Pokemon('Gengar', 'Ghost', 'Poison', '1',
                                            '1', '1', '1', '1', '1',
                                            None, None, None, None)
                 ]


# for i in range(1, 7):
#     picked_pokemon = pick_pokemon(i)
#     users_pokemon.append(picked_pokemon)


def return_pokemon(force=None):
    with open('pokedex.csv', mode='r') as data:
        pokedex = list(csv.DictReader(data))

    if force is None:
        while True:
            random_index = random.randint(1, 802)
            for pokemon in pokedex:
                if int(pokemon['pokedex_number']) == random_index:
                    name = pokemon['name']
                    if name == 'Ditto' or name == 'Unown' or name == 'Cosmog' \
                            or name == 'Cosmoem':
                        pass
                    else:
                        return pokemon['name']
    else:
        for pokemon in pokedex:
            if pokemon['name'] == force:
                return pokemon['type_1'], pokemon['type_2'], \
                       int(pokemon['hp']), int(pokemon['atk']), \
                       int(pokemon['spatk']), int(pokemon['df']), \
                       int(pokemon['spdf']), int(pokemon['spd'])


def pick_computer_moves(move_name) -> pokemon_move_class.Move:
    with open('moves.csv', mode='r') as move_data:
        moves = list(csv.DictReader(move_data))

    for move in moves:
        if move['name'] == move_name:
            return pokemon_move_class.Move(move['name'], move['power'],
                                           move['type'], move['category'],
                                           move['accuracy'])


def pick_computer_pokemon():
    with open('movesets.csv', mode='r') as moveset_data:
        movesets = list(csv.DictReader(moveset_data))

    name = return_pokemon()
    print(name)

    for moveset in movesets:
        if moveset['species'] == name:
            moves = []
            for i in range(1, 174):
                if moveset[f'move{i}'] != '':
                    moves.append(moveset[f'move{i}'].strip())
            print(moves)
            comp_moves = []
            for i in range(4):
                count = 0
                while True:
                    comp_move = pick_computer_moves(random.choice(moves))
                    if count >= 50:
                        return
                    if comp_move.pwr == '0' or comp_move.pwr == '—' or \
                            comp_move.pwr == 'â€”':
                        count += 1
                    else:
                        if comp_move.name in comp_moves:
                            pass
                        else:
                            comp_move.pwr = int(comp_move.pwr)
                            comp_moves.append(comp_move)
                            moves.remove(comp_move.name)
                            break

            type_1, type_2, hp, atk, spatk, df, spdf, spd = \
                return_pokemon(name)

            return pokemon_move_class.Pokemon(name, type_1, type_2, hp, atk,
                                              spatk, df, spdf, spd,
                                              comp_moves[0], comp_moves[1],
                                              comp_moves[2], comp_moves[3])


computers_pokemon = []
while len(computers_pokemon) < 6:
    comp_pokemon = pick_computer_pokemon()
    if comp_pokemon is not None:
        computers_pokemon.append(comp_pokemon)
    else:
        pass

# Main Battle loop
while True:
    print('Your Pokemon: ')
    for pokemon in users_pokemon:
        print(f'{users_pokemon.index(pokemon) + 1}. ' + pokemon.name)

    print('\nOpponents Pokemon: ')
    for cpu_pokemon in computers_pokemon:
        print(f"{computers_pokemon.index(cpu_pokemon) + 1}. " +
              cpu_pokemon.name)
    cpu_current = computers_pokemon[0]
    while True:
        try:
            current_index = int(input('\nWhich Pokemon would you like to send '
                                      'out? (1-6): '))
            index = current_index - 1
            if 1 <= current_index <= 6:
                current_pokemon = users_pokemon[index]
                print(f'You sent out {current_pokemon.name}!')
                print(f"Opponent sent out {cpu_current.name}!\n")
                break
            else:
                print("Please enter a valid integer. ")
        except ValueError:
            print("Please enter a valid integer. ")

    # Prints the pokemon name and the health in line.
    print(f"{current_pokemon.name}" + str(" " * (20 - len(
        current_pokemon.name))) + "Health: " + str(current_pokemon.hp))

    print(f"{cpu_current.name}" + str(" " * (20 - len(cpu_current.name))) +
          'Health: ' + str(cpu_current.hp))

    while True:
        print("\nYour Moves")
        print('1.', current_pokemon.move1.name + str(" " * (20 - len(
            current_pokemon.move1.name))) + "Power: " +
              str(current_pokemon.move1.pwr))
        print('2.', current_pokemon.move2.name + str(" " * (20 - len(
            current_pokemon.move2.name))) + 'Power: ' +
              str(current_pokemon.move2.pwr))
        print('3.', current_pokemon.move3.name + str(" " * (20 - len(
            current_pokemon.move3.name))) + 'Power: ' +
              str(current_pokemon.move3.pwr))
        print('4.', current_pokemon.move4.name + str(" " * (20 - len(
            current_pokemon.move4.name))) + 'Power: ' +
              str(current_pokemon.move4.pwr))

        while True:
            try:
                move = int(input('Your Move (1-4): '))
                if 1 <= move <= 4:
                    if move == 1:
                        move_choice = current_pokemon.move1
                    elif move == 2:
                        move_choice = current_pokemon.move2
                    elif move == 3:
                        move_choice = current_pokemon.move3
                    elif move == 4:
                        move_choice = current_pokemon.move4
                    break
                else:
                    print('Please enter a valid integer. ')
            except ValueError:
                print("Please enter a valid integer. ")

        if current_pokemon.spd > cpu_current.spd:
            print(f"\n{current_pokemon.name} used {move_choice.name}")
            damage_dealt = damage_calc.calculate_dmg(current_pokemon,
                                                     cpu_current,
                                                     move_choice)
            print(f"\nIt dealt {damage_dealt} damage! ")
            cpu_current.hp -= damage_dealt

            if cpu_current.hp <= 0:
                cpu_current.hp = 0
                print(f"{cpu_current.name} fainted!")
            else:
                pass
        elif current_pokemon.spd < cpu_current.spd:
            random_move = cpu_current.random_move()
            print(f"\n{cpu_current.name} used {random_move.name1}")
            damage_dealt = damage_calc.calculate_dmg(cpu_current,
                                                     current_pokemon,
                                                     random_move)
            print(f"\nIt dealt {damage_dealt} damage! ")
            current_pokemon.hp -= damage_dealt

            if current_pokemon.hp <= 0:
                current_pokemon.hp = 0
                print(f"{current_pokemon.name} fainted!")
                users_pokemon.remove(current_pokemon)

            if len(users_pokemon) == 0:
                print("You have no more Pokemon that can Battle!")
                print("Match Result: You Lose...")

        break
    break
