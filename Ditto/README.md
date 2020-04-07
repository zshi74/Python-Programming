## Program Skills

* Practice using lists of iterables
* Creating and using dictionaries
* Practice using the random module

## Summary

You are out for a pleasant Pokéwalk with your favorite Pokémon, Ditto:


*(DITTO rearranges its cell structure to transform itself into other shapes)*

Ditto has the ability to absorb the powers and mimic the appearance of other Pokémon you encounter. It will be up to you to write a program to help generate these Pokémon and help your Ditto decide whether to add other Pokémon's powers to its repertoire, or let them pass by.

## Program Requirements

For this program, I will write five (5) functions with the following names and behaviors:

1. **generate_pokemon(names, powers)** - takes in two lists of potential Pokémon names and powers, randomly selects one of each and generates a power level, and returns a dictionary representing one new Pokémon.
2. **get_level(ditto)** - takes in your Ditto's information as a dictionary and returns its current level as a float.
3. **should_absorb(ditto, pokemon)** - takes in your Ditto's and another Pokémon's information as dictionaries and returns True if the Ditto would benefit from absorbing the Pokémon, False if not.
4. **absorb(ditto, pokemon)** - takes in your Ditto's and another Pokémon's information as dictionaries and updates the Ditto's dictionary to reflect the new power and level in place.
5. **take_walk(pokemon_list)** - takes in an already-generated list of Pokémon dictionaries and returns your Ditto's dictionary of information.
