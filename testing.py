import damage_calc
import pokemon_move_class as pokemon

# All pokemon and moves are examples only.
shadow_ball = pokemon.Move('Shadow Ball', 80, 'Ghost', 'Special', 100)
facade = pokemon.Move('Facade', 70, 'Air', 'Physical', 100)
dark_pulse = pokemon.Move('Dark Pulse', 80, 'Dark', 'Special', 100)
thunderbolt = pokemon.Move('Thunderbolt', 90, 'Electric', 'Special', 100)
gengar = pokemon.Pokemon("Gengar", 'Ghost', 'Poison', 60, 65, 130, 60, 75, 110,
                         shadow_ball, facade, dark_pulse, thunderbolt)

psychic = pokemon.Move('Psychic', 90, 'Psychic', 'Special', 100)
wood_hammer = pokemon.Move('Wood Hammer', 120, 'Grass', 'Physical', 100)
hyper_beam = pokemon.Move('Hyper Beam', 150, 'Normal', 'Special', 90)
energy_ball = pokemon.Move('Energy Ball', 90, 'Grass', 'Special', 100)
exeggutor = pokemon.Pokemon('Exeggutor', 'Grass', "Psychic", 95, 95, 125, 85,
                            75, 55, psychic, wood_hammer, hyper_beam,
                            energy_ball)

print(damage_calc.calculate_dmg(exeggutor, gengar, exeggutor.move3))
