# GameOfThrees
This program plays the "Game of Threes". The rules are:

First, you mash in a random large number to start with. Then, repeatedly do the following:
If the number is divisible by 3, divide it by 3.
If it's not, either add 1 or subtract 1 (to make it divisible by 3), then divide it by 3.
The game stops when you reach "1".

The input is a single number: the number at which the game starts. This program plays the Threes game, and outputs a valid sequence of steps you need to take to get to 1. Each step should be output as the number you start at, followed by either -1 or 1 (if you are adding/subtracting 1 before dividing), or 0 (if you are just dividing). The last line should simply be 1.
