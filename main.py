import csv
import damage_calc
import pokemon_move_class


# Create moves for testing
vine_whip = pokemon_move_class.Move('Vine Whip', 45, 'grass', 'Physical')
ember = pokemon_move_class.Move('Ember', 40, 'fire', 'Special')


def get_pokemon():
    with open('pokemon_data.csv', mode='r') as data:
        reader = csv.DictReader(data)

        user_pokemon = input("What Pokemon would you like to use?")




