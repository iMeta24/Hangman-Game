# hangman.py

import random

words = ["python", "github", "hangman"]
word = random.choice(words)
guesses = []
lives = 5

while lives > 0:
    guess = input("Enter a letter: ").lower()
    if guess in word:
        guesses.append(guess)
    else:
        lives -= 1
        print("Incorrect! Lives remaining:", lives)
    display_word = "".join([letter if letter in guesses else "_" for letter in word])
    print("Word:", display_word)
    if "_" not in display_word:
        print("You won!")
        break
else:
    print("Game over! The word was:", word)
