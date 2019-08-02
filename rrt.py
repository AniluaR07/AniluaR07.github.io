#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)

guess = input("Guess a number between 1 and 20 (inclusive): ")
if not guess.isnumeric(): # checks if a string is only digits 0 to 9
	print("That's not a positive whole number, try again!")
else:
	guess = int(guess) # converts a string to an integer

import Random

hidden = random.randrange(1, 201)
# print hidden
guess = int(raw_input("please enter your guess:"))

if guess == hidden:
    print"hit!"
    elif guess < hidden:
         print "your guess is too low"
         else:
             print "your guess is too high"
