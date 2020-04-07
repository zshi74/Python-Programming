## Program Skills

* Creating and using classes and objects

## Summary

Once again, we're out for a pleasant Pokéwalk with our favorite Pokémon, Ditto:

Ditto has the ability to absorb the powers and mimic the appearance of other Pokémon you encounter. It will be up to you to write a program to help generate these Pokémon and help your Ditto decide whether to add other Pokémon's powers to its repertoire, or let them pass by.

To mix things up this time, you'll be situating these functions as methods within a Ditto class!

## Program Structure

Resue two functions from our original Ditto program.

1. **generate_pokemon(names, powers)** - takes in two lists of potential Pokémon names and powers, randomly selects one of each and generates a power level, and returns a dictionary representing one new Pokémon.
2. **take_walk(pokemon_list)** - takes in an already-generated list of Pokémon dictionaries and returns your Ditto object.

Additionally, you must create a Ditto class, which will include at least these three (3) methods.

1. **ditto.get_level()** - returns the Ditto's current level as a float.
2. **ditto.should_absorb(pokemon)** - takes in another Pokémon's information as a dictionary and returns True if the Ditto would benefit from absorbing the Pokémon, False if not.
3. **ditto.absorb(pokemon)** - takes in another Pokémon's information as a dictionary and updates the Ditto object to reflect the new power and level in place.
