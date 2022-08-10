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
                            if pokemon_move['power'] == '—' or \
                                    pokemon_move['power'] == 'â€”' or \
                                    pokemon_move['power'] == '0':
                                print("Unable to pick that move\n")
                                break
                            print(f"Picked {user_move} as move {number}! \n")
                            return pokemon_move_class.Move(
                                pokemon_move['name'],
                                int(pokemon_move['power']),
                                pokemon_move['type'], pokemon_move['category'],
                                pokemon_move['accuracy'],
                                int(pokemon_move['pp']))
                else:
                    print("That move doesn't exist. \n")


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
                                                      int(pokemon['hp']),
                                                      int(pokemon['atk']),
                                                      int(pokemon['spatk']),
                                                      int(pokemon['df']),
                                                      int(pokemon['spdf']),
                                                      int(pokemon['spd']),
                                                      move1, move2, move3,
                                                      move4)
                else:
                    pass
            print('No Pokemon found. ')


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
                                           move['accuracy'], move['pp'])


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
            # TODO Remove this later
            print(moves)
            comp_moves = []
            for i in range(4):
                count = 0
                while True:
                    comp_move = pick_computer_moves(random.choice(moves))
                    if count >= 50:
                        return
                    # Last check is weird encoding thing I don't really know.
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


def create_users_pokemon():
    users_pokemon = []
    for i in range(1, 4):
        picked_pokemon = pick_pokemon(i)
        users_pokemon.append(picked_pokemon)
    return users_pokemon


def create_computers_pokemon():
    computers_pokemon = []
    while len(computers_pokemon) < 6:
        comp_pokemon = pick_computer_pokemon()
        if comp_pokemon is not None:
            computers_pokemon.append(comp_pokemon)
        else:
            pass
    return computers_pokemon


def create_copies():
    return users_pokemon.copy(), computers_pokemon.copy()


def send_out_pokemon(opponent, opponent_mon: pokemon_move_class.Pokemon):
    print(f"\n{opponent} sent out {opponent_mon.name}!")
    while True:
        try:
            current_index = int(input('\nWhich Pokemon would you like to send '
                                      f'out? (1-{len(users_pokemon_copy)}): '))
            index = current_index - 1
            if 1 <= current_index <= 6:
                current_pokemon = users_pokemon_copy[index]
                print(f'You sent out {current_pokemon.name}!\n')
                return current_pokemon
            else:
                print("Please enter a valid integer. ")
        except ValueError:
            print("Please enter a valid integer. ")


def print_pokemon():
    print('Your Pokemon: ')
    for pokemon in users_pokemon_copy:
        print(f'{users_pokemon_copy.index(pokemon) + 1}. ' + pokemon.name)

    print('\nOpponents Pokemon: ')
    for cpu_pokemon in computers_pokemon_copy:
        print(f"{computers_pokemon_copy.index(cpu_pokemon) + 1}. " +
              cpu_pokemon.name)


def print_hp(pokemon: pokemon_move_class.Pokemon,
             opponent: pokemon_move_class.Pokemon):
    # Prints the pokemon name and the health in line.
    print(f"{pokemon.name}" + str(" " * (20 - len(
        pokemon.name))) + "Health: " + str(pokemon.hp))

    print(f"{opponent.name}" + str(" " * (20 - len(opponent.name))) +
          'Health: ' + str(opponent.hp))


def switch_pokemon() -> pokemon_move_class.Pokemon:
    while True:
        try:
            print_pokemon()
            user_switch = int(input(f"What Pokemon would you like to switch to"
                                    f"? (1-{len(users_pokemon_copy)}): ")) - 1
            if 0 <= user_switch <= len(users_pokemon_copy) - 1:
                print(
                    f"You sent out {users_pokemon_copy[user_switch].name}!\n")
                return users_pokemon_copy[user_switch]
        except ValueError:
            print("Please enter a valid integer .")
        print("That Pokemon isn't in your party")


def receive_money() -> int:
    if len(users_pokemon_copy) == 1:
        return random.randint(5000, 10000)
    elif len(users_pokemon_copy) == 2:
        return random.randint(4000, 8000)
    elif len(users_pokemon_copy) == 3:
        return random.randint(3000, 6000)
    elif len(users_pokemon_copy) == 4:
        return random.randint(2000, 4000)
    elif len(users_pokemon_copy) == 5:
        return random.randint(1000, 2000)
    elif len(users_pokemon_copy) == 6:
        return random.randint(500, 1000)


# Main Battle loop
def battle(name, opponent_name):
    global money
    hp = []
    for pokemon in users_pokemon_copy:
        if pokemon.hp == 0:
            hp.append(False)
        else:
            hp.append(True)

    if True not in hp:
        print("You have no Pokemon that can battle! ")
        return

    print("""\n==============
-    Battle    -
==============""")
    print_pokemon()
    cpu_current = computers_pokemon_copy[0]
    current_pokemon = send_out_pokemon(opponent_name, cpu_current)
    print_hp(current_pokemon, cpu_current)
    while True:
        while True:
            print(f"\n{current_pokemon.name}'s Moves")
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

            if current_pokemon.spd >= cpu_current.spd:
                print(f"\n{current_pokemon.name} used {move_choice.name}")
                damage_dealt = damage_calc.calculate_dmg(current_pokemon,
                                                         cpu_current,
                                                         move_choice, True)
                print(f"It dealt {damage_dealt} damage! \n")
                cpu_current.hp -= damage_dealt

                if cpu_current.hp <= 0:
                    cpu_current.hp = 0
                    print(f"{cpu_current.name} fainted!\n")
                    computers_pokemon_copy.remove(cpu_current)
                    if len(computers_pokemon_copy) == 0:
                        print(f"{opponent_name} has no more Pokemon that can "
                              f"battle.")
                        print("Match Result: You Win!\n")
                        money_received = receive_money()
                        print(f"You received {money_received}!")
                        money += money_received
                        return
                    cpu_current = computers_pokemon_copy[0]
                    print_pokemon()
                    current_pokemon = send_out_pokemon(opponent_name,
                                                       cpu_current)
                    break
                move_damages = {}
                moves = cpu_current.list_of_moves()
                for move in moves:
                    move_damages.update({move: damage_calc.calculate_dmg(
                        cpu_current, current_pokemon, move, False)})

                sorted_moves = sorted(move_damages.items(), key=lambda
                                      item: item[1], reverse=True)
                random_choice = int(random.uniform(1, 100))

                if 1 <= random_choice <= 40:
                    picked_move = sorted_moves[0][0]
                elif 41 <= random_choice <= 70:
                    picked_move = sorted_moves[1][0]
                elif 71 <= random_choice <= 90:
                    picked_move = sorted_moves[2][0]
                elif 91 <= random_choice <= 100:
                    picked_move = sorted_moves[3][0]

                print(f"\n{cpu_current.name} used {picked_move.name}")
                damage_dealt = damage_calc.calculate_dmg(cpu_current,
                                                         current_pokemon,
                                                         picked_move, True)
                print(f"It dealt {damage_dealt} damage! \n")
                current_pokemon.hp -= damage_dealt
                if current_pokemon.hp <= 0:
                    current_pokemon.hp = 0
                    print(f"{current_pokemon.name} fainted...\n")
                    users_pokemon_copy.remove(current_pokemon)
                    if len(users_pokemon_copy) == 0:
                        print(f"{name} has no more pokemon that can battle. ")
                        print('Match Result: You lose...')
                        return
                    print_pokemon()
                    current_pokemon = send_out_pokemon(opponent_name,
                                                       cpu_current)
                    break
                print_hp(current_pokemon, cpu_current)
                while True:
                    switch = input("\nWould you like to switch another Pokemon"
                                   " in (y/n): ")
                    if switch == 'y':
                        current_pokemon = switch_pokemon()
                        break
                    elif switch == 'n':
                        break
                    else:
                        print("\nPlease enter either 'y' or 'n'. ")

            elif current_pokemon.spd < cpu_current.spd:
                move_damages = {}
                moves = cpu_current.list_of_moves()
                for move in moves:
                    move_damages.update({move: damage_calc.calculate_dmg(
                        cpu_current, current_pokemon, move, False)})

                sorted_moves = sorted(move_damages.items(),
                                      key=lambda item: item[1], reverse=True)
                random_choice = random.randint(1, 100)

                if 1 <= random_choice <= 40:
                    picked_move = sorted_moves[0][0]
                elif 41 <= random_choice <= 70:
                    picked_move = sorted_moves[1][0]
                elif 71 <= random_choice <= 90:
                    picked_move = sorted_moves[2][0]
                elif 91 <= random_choice <= 100:
                    picked_move = sorted_moves[3][0]

                print(f"\n{cpu_current.name} used {picked_move.name}.")
                damage_dealt = damage_calc.calculate_dmg(cpu_current,
                                                         current_pokemon,
                                                         picked_move, True)
                print(f"It dealt {damage_dealt} damage! \n")
                current_pokemon.hp -= damage_dealt

                if current_pokemon.hp <= 0:
                    current_pokemon.hp = 0
                    print(f"{current_pokemon.name} fainted...\n")
                    users_pokemon_copy.remove(current_pokemon)

                    if len(users_pokemon_copy) == 0:
                        print(f"{name} has no more Pokemon that can Battle!")
                        print("Match Result: You Lose...")
                        return
                    print_pokemon()
                    current_pokemon = send_out_pokemon(opponent_name,
                                                       cpu_current)
                    break

                print(f"\n{current_pokemon.name} used {move_choice.name}")
                damage_dealt = damage_calc.calculate_dmg(current_pokemon,
                                                         cpu_current,
                                                         move_choice, True)
                print(f"It dealt {damage_dealt} damage! \n")
                cpu_current.hp -= damage_dealt
                if cpu_current.hp <= 0:
                    cpu_current.hp = 0
                    print(f"{cpu_current.name} fainted!\n")
                    computers_pokemon_copy.remove(cpu_current)
                    if len(computers_pokemon_copy) == 0:
                        print(f"{opponent_name} has no more Pokemon that can"
                              f" battle. ")
                        print('Match Result: You win!')
                        money_received = receive_money()
                        print(f"You received {money_received}!")
                        money += money_received
                        return
                    cpu_current = computers_pokemon_copy[0]
                    print_pokemon()
                    current_pokemon = send_out_pokemon(opponent_name,
                                                       cpu_current)
                    break
                print_hp(current_pokemon, cpu_current)
                while True:
                    switch = input("\nWould you like to switch another Pokemon"
                                   " in (y/n): ")
                    if switch == 'y':
                        current_pokemon = switch_pokemon()
                        break
                    elif switch == 'n':
                        break
                    else:
                        print("\nPlease enter either 'y' or 'n'. ")


def print_all_hp():
    print()
    for pokemon in users_pokemon:
        print(f"{pokemon.name.ljust(15)}{pokemon.hp}/{pokemon.ORIGINAL_HP}")
    print()


def heal_pokemon(healing: int = None):
    try:
        print_all_hp()
        choice = int(input("Which Pokemon would you like to heal? (1-6): "))
        pokemon = users_pokemon[choice - 1]
        if pokemon.hp == pokemon.ORIGINAL_HP:
            print("This Pokemon is already at full HP. ")
            return False
        elif pokemon.hp == 0:
            print("This Pokemon has fainted. Use a revive or Max Revive. ")
            return False
        else:
            if healing is None:
                pokemon.reset()
                print(f"Fully healed {pokemon.name}! ")
                return
            pokemon.hp += healing
            if pokemon.hp > pokemon.ORIGINAL_HP:
                diff = pokemon.hp - pokemon.ORIGINAL_HP
                pokemon.hp = pokemon.ORIGINAL_HP
                print(f"Healed {pokemon.name} by {diff} HP. ")
            else:
                print(f"Healed {pokemon.name} by {healing} HP. ")
    except ValueError or IndexError:
        print("Please enter a valid integer. ")
        return False


def revive_pokemon(max_revive: bool = False):
    print_all_hp()
    choice = int(input("Which Pokemon would you like to heal? (1-6): "))
    pokemon = users_pokemon[choice - 1]
    if pokemon.hp != 0:
        print(f"{pokemon.name} has not fainted! ")
        return False
    else:
        if max_revive is False:
            healing_amount = int(pokemon.ORIGINAL_HP / 2)
            pokemon.hp += healing_amount
            print(f"{pokemon.name} was revived, and {healing_amount} HP "
                  f"was restored!")
        else:
            pokemon.reset()
            print(f"{pokemon.name} was revived and fully healed!")


def shop():
    global money
    global username
    print("""\n==============
-    Shop    -
==============""")

    items = [{'name': 'Potion', 'description': "Restores 20 HP to a Pokemon.",
              'price': 200, 'healing': 20},
             {'name': "Super Potion", 'description':
                 "Restores 60 HP to a Pokemon", 'price': 550, 'healing': 60},
             {'name': 'Hyper Potion', 'description': "Restores 120 HP to a "
                                                     "Pokemon", 'price':
                                                     1000, 'healing': 120},
             {'name': 'Max Potion', 'description': 'Heals a Pokemon to full '
                                                   'HP.', 'price': 1500},
             {'name': 'Revive', 'description': "Revives a fainted Pokemon "
                                               "and restores half of it's "
                                               "HP.", 'price': 1000},
             {'name': "Max Revive", 'description': "Revives a fainted "
                                                   "Pokemon and restores all"
                                                   " of it's HP.", 'price':
                                                   2000},
             {'name': "Battler's Crown", 'description': 'A crown to show '
                                                        'your dominance on '
                                                        'the battlefield.',
              'price': 10000}]

    while True:
        count = 0
        print(f"You have ${money} Poke-dollars. \n")
        for item in items:
            print(f"{count + 1}. {item['name'].ljust(17)}"
                  f"{item['description'].ljust(60)}${item['price']}")
            count += 1
        print('\nq. Return to Main Menu. ')

        try:
            purchase = int(input(f"\nWhat would you like to buy "
                                 f"(1-{len(items)}): "))

            if items[purchase - 1]['price'] > money:
                print("This item is too expensive! ")
            elif purchase == 1 or purchase == 2 or purchase == 3:
                healed = heal_pokemon(items[purchase - 1]['healing'])
                if healed is not False:
                    money -= items[purchase - 1]['price']
            elif purchase == 4:
                healed = heal_pokemon()
                if healed is not False:
                    money -= items[3]['price']
            elif purchase == 5:
                revived = revive_pokemon()
                if revived is not False:
                    money -= items[4]['price']
            elif purchase == 6:
                revived = revive_pokemon(True)
                if revived is not True:
                    money -= items[5]['price']
            elif purchase == 7:
                print("You purchased the BATTLER'S CROWN!!!\n")
                username = username + ' 👑'
                print(f"Your name will now be {username}\n")
        except ValueError:
            return


def print_menu(opponent_name):
    print("""\n==============
-    Menu    -
==============""")
    menu_options = [f"Battle against {opponent_name}.", 'Browse the Shop.']
    print()
    for i in range(len(menu_options)):
        print(f"{i + 1}. {menu_options[i]}")
    while True:
        try:
            choice = int(input("Choice (1-2): "))
            if 1 <= choice <= len(menu_options):
                return choice
            else:
                print("Please enter a valid integer. ")
        except ValueError:
            print("Please enter a valid integer. ")


def main():
    while True:
        user_choice = print_menu(opponent)
        if user_choice == 1:
            battle(username, opponent)
            break
        elif user_choice == 2:
            shop()


print("Welcome to the battle arena!")
with open('names.csv', mode='r') as names_data:
    names = list(csv.DictReader(names_data))
username = input("Enter your name: ")
money = 0

users_pokemon = create_users_pokemon()

while True:
    name_index = random.randint(1, len(names))
    opponent = names[name_index]['Names'].title()
    computers_pokemon = create_computers_pokemon()
    users_pokemon_copy, computers_pokemon_copy = create_copies()
    main()
