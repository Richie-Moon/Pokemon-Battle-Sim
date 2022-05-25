import csv
import pokemon_types

all_pokemon = {}

with open('pokemon_data.csv', mode='r') as data:
    data_reader = csv.DictReader(data, delimiter=',')

    for pokemon in data_reader:
        all_pokemon.update()

print(all_pokemon)
