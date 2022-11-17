# HANGMAN

### Discription
A program which is designed to play a game of hang man with the user

# WORD DISPLAY
```
f = open("alpha.txt", "r")
word_bank = f.readlines()
f.close()
word = random.choice(word_bank)

if word != word_bank[-1]:
    word = word[:len(word) - 1]

underscored = "_" * len(word)
```
### Discription
Opens the Alpha.txt file and chooses a random word and stores it to the variable named word
Then each letter of the word is represented by underscores in the variable called underscored
