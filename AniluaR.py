import random

# A list of words that
potential_words = ["Masterpiece", "Monster", "Computer", "Improvements", "juice"]

word = random.choice(potential_words)
caracters = len(word)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = ["_"] # TIP: the number of letters should match the word
for a in range(caracters - 1):
    current_word.append("_")
# Some useful variables

guesses = []
maxfails = 5
fails = 0

while fails < maxfails:
    guess = input("Guess a letter: ")

	# check if the guess is valid: Is it one letter? Have they already guessed it?
check = False
while check == False:
    guess = input("guess the word")
	# check if the guess is correct: Is it in the word? If so, reveal the letters!
if guess == word:
    check = True
    print(current_word)


    fails = fails+1
    print("You have " + str(maxfails - fails) + " tries left!")

else:
    check = False
    print("try again")
    check = True
    print("you won!")
