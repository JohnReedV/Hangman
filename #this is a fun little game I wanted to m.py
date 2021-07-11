#hangman
#fun little game I wanted to make
import time
secret = set(word := input("Input the secret word for this hangman game! ").lower())
MAX_ATTEMPTS = 5

guesses = set()
num_attempt = 0

while num_attempt < MAX_ATTEMPTS:
    print(' '.join(char if char in guesses else '_' for char in word))
    letter = input("Guess a letter! ").lower()
    if letter in secret:
        print('Correct!')
        guesses.add(letter)
    else:
        num_attempt += 1
        print(f"Nope.. you have {MAX_ATTEMPTS - num_attempt} more attempts! ")
    if not secret - guesses:
        print(f'Congradz! You won! The word was "{word}".')
        time.sleep(5)
        break
else:
    print(f'GAME OVER!!!!! The word was "{word}".')
    time.sleep(5)
    