#!/usr/bin/env python
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
guesses_left = 3
guess = int(raw_input("Your guess:"))

while guesses_left > 0:
    if guess == random_number:
        print "You win!"
        break
    if guess != random_number:
        guesses_left -= 1
        print guesses_left
else:
    if guesses_left != 0:
        print "You lose.."

# Start your game!
