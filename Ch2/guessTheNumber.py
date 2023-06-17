#! /usr/bin/python3

import random

guess = 0
numberOfGuesses = 0
randomNumber = random.randint(0,1000)

while guess != randomNumber:
    print("Guess a number between 0 and 1000.")
    guess = int(input())
    numberOfGuesses += 1

    if guess > randomNumber:
        print(f"Your guess of {guess} is too high.")
    elif guess < randomNumber:
        print(f"Your guess of {guess} is too low.")

print(f"You have guessed the correct number of {randomNumber}.")
print(f"It took you {numberOfGuesses} attempts.")