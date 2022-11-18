# HANGMAN

### Discription
A program which is designed to play a game of hang man with the user

# WORD SELECTOR
```
f = open("alpha.txt", "r")
word_bank = f.readlines()
f.close()
word = random.choice(word_bank)

if word != word_bank[-1]:
    word = word[:len(word) - 1]
```
### Discription
1. Opens the Alpha.txt file and chooses a random word and stores it to the variable named word
2. Removes the \n character from the end of the word
### Example
#### Input
    word = random.choice(word_bank)`
#### Output
    word = WHOLESOME`

# WORD HIDER
```
underscored = "_" * len(word)
```
### Decription
Each letter of the randomly picked word is represented by underscores in the variable called underscored
### Example
#### Input
    word = WHOLESOME`
#### Output
    underscored = _ _ _ _ _ _ _ _ _`

# Gallows
```
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
```
### Decription
Creates a list of sellectable ACII art pictures which can be sellected depending on number of wrong guesses
### Example
#### Input
    gallows[3]`
#### Output
```
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========
```
# SCORE AND GRAVE
```
strikes = 0
graveyard = ""

while underscored != word and strikes < 6:
    print(gallows[strikes])
    print(underscored)
    print("Graveyard:", graveyard[:-2])

    guess = input("Enter a letter guess: ").upper()
        while len(guess) != 1 or not guess.isalpha() or guess in graveyard:
            print("Invalid guess")
            guess = input("Enter a letter guess: ").upper()

    if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    underscored = underscored[:i] + guess + underscored[i+1:]
        else:
            strikes += 1

        graveyard += guess + ", "

print(gallows[strikes])
```
### Description
1. Creates a variable to store the number of incorrect guesses
2. Creates a variable to store all previusly guessed letters
3. If you have not exeded the max number of wrong guesses(6) then it will print the Gallows, the tnderscored word, and Guessed Charaters
4. Prompts you to guess a letter and checks the input for validity as a single letter
5. Either displays the character in the word if it is a good guess or adds a strike to your incorrect guesses
6. Prints the gallows once you either die or win
### Example
#### Input
```
underscored = _ _ _ _ E _ _ _ _
strikes = 4
graveyard = a, e, b, t, u
```
#### Output
```
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
_ _ _ _ E _ _ _ _
a, e, b, t, u
```

#CHECKER
```
print(word)
if strikes == 6:
    print("You lose lmao!")
else:
    print("You win!")
```
### Decription
Checks the number od strikes to test if you lost the game if so it displays a looser message if not it display a win message
### Example
#### Input
    strikes = 6`
#### Output
    You lose lmao!`
