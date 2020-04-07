## Program Skills

* Practice mixing and matching loops
* Creating and using lists

## Summary

Hobbes has had a long week full of grading exams and taking lectures and she’s exhausted by the end of it. So she decides its time to have some fun! Hobbes heads to the bar nearest to her home for some good old shots of Fireball. As the evening turns into night, Hobbes realizes she's had what one might call ‘one too many’ drinks, so it's time to go home. What makes her journey back home difficult is that there’s a nasty hole on the road (which she soberly avoided on the way to the bar). Now the question is: Can she make it home??

Write a program to find out if Hobbes makes it safely back home or not.

The program takes as input the amount of alcohol consumed to derive a ‘level’ of inebriation. Based on this level, the walk pattern and step length changes. (There are multiple walk patterns, like ‘for every 5 steps forward, take 2 steps back’ and so on.) Step lengths can vary.

The program will also need to know the distance to Hobbes’s home, and then run a simulation of Hobbes’s dangerous journey to her house. The program should store Hobbes’s location at each step in a list; if she steps in the pothole, output: “Oh no! Hobbes fell near the bar!” and if she makes it home, output: “Hurray! Hobbes makes it through the day!” and return the location list.

## Program Components

For this program, I will write four (4) functions with the following names and behaviors:

1. **run_simulation()** - the main function, which gets inputs and runs the simulation using the other functions listed below, and returns a list of the positions occupied by Hobbes during her walk. This is the only function which should include print statements.
2. **get_level(num_drinks)** - takes in the reported number of drinks and returns the level of inebriation as an integer.
3. **get_walk(drunk_level)** - takes in the level of inebriation and returns three values as a list of integers: the length of the step taken, and the step pattern (number of steps forward and number of steps backward).
4. **update(current_position, step_direction, step_length)** - takes in the current position, step direction (+1 for forward, -1 for backward) and length of step, and returns the updated position as an integer.

