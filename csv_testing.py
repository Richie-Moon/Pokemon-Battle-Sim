import csv
import pokemon_types

with open('pokemon_data.csv', mode='r') as data:
    data_reader = csv.DictReader(data, delimiter=',')

    for pokemon in data_reader:
        print(pokemon['name'])
        print(pokemon_types.type_multiplier('fire', pokemon['type1'], pokemon['type2']))
