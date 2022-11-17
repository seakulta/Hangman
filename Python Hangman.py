"""
HANG MAN:
Chooses a random word for a list of words and plays hangman with the user

RANDOM WORD SELECTION:
Existing File that contains possible word choices
> Each line is a single word
> Word choices contain no space, symbol, or number characters

WORD DISPLAY:
Displays the word as underscores, one for each letter

GALLLOWS:
Displays the gallows and the man being hung 

GRAVEYARD:
Shows a graveyard of your previously used character

WIN LOSE:
Determines if you won or lost the game
"""

import random

# Opens the document with the words which can be picked to guess
f = open("alpha.txt", "r")
word_bank = f.readlines()
f.close()
word = random.choice(word_bank)

# Removes the /n (new line) charachter at the end of the word
if word != word_bank[-1]:
    word = word[:len(word) - 1]

#generates the lines for each letter in the word
underscored = "_" * len(word)

#creates a list of the possible hang man hanging states
gallows = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

#stores the number of wrong guesses and all of the previously guessed letters
strikes = 0
graveyard = ""

#Checks to make sure the number of wrong guesses is under 6 and that the word hasn't been guesses
while underscored != word and strikes < 6:
    print(gallows[strikes])
    print(underscored)
    print("Graveyard:", graveyard[:-2])

#Takes user input for a 1 letter guess, if it is not 1 character or is not a letter it will promp for a new input
    guess = input("Enter a letter guess: ").upper()
    while len(guess) != 1 or not guess.isalpha() or guess in graveyard:
        print("Invalid guess")
        guess = input("Enter a letter guess: ").upper()

#Checks if the guess is in the word and if it is it replaces the underscore with the letter
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                underscored = underscored[:i] + guess + underscored[i+1:]
    else:
        strikes += 1

    graveyard += guess + ", "

print(gallows[strikes])

#checks if you are dead, if so it displays death message otherwise it say you win
print(word)
if strikes == 6:
    print("You lose lmao!")
else:
    print("You win!")
main.py
Displaying main.py.