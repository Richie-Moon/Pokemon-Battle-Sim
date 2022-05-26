import csv
import damage_calc
import pokemon_move_class


# Create moves for testing
vine_whip = pokemon_move_class.Move('Vine Whip', 45, 'grass', 'Physical')
ember = pokemon_move_class.Move('Ember', 40, 'fire', 'Special')


def pick_pokemon(number) -> dict:
    with open('pokedex.csv', mode='r') as data:
        reader = list(csv.DictReader(data))

        while True:
            user_pokemon = input(f"Pokemon {number}: ").capitalize().strip()
            for pokemon in reader:
                if pokemon['name'] == user_pokemon:
                    print(f"You chose {pokemon['name']}!")
                    return pokemon
                else:
                    pass
            print('No Pokemon found. ')


users_pokemon = []
for i in range(1, 7):
    picked_pokemon = pick_pokemon(i)
    users_pokemon.append(picked_pokemon)

print(users_pokemon)
