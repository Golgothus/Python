# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus
# Ch. 3 Functions
# This program will allow the user to guess a number

from random import randint

secretNum = randint(1, 100)
print('I am thinking of a number bewteen 1 & 100.')
print('Try and guess the number in less than 7 tries.')

# The player gets 7 tries.
for guessAttempt in range(1, 7):
    print('Guess attempt number ' + str(guessAttempt) + '.')
    try:
        guess = int(input())
        if guess < secretNum:
            print('Your guess is too low, try again.')
        elif guess > secretNum:
            print('Your guess is too high, try again.')
        else:
            break  # This is the correct guess!

    except ZeroDivisionError:
        print('Error: Cannot divide by 0, please use a different number .')
    except TypeError:
        print('Please insert a number.')
    except ValueError:
        print('Please insert a number.')

if guess == secretNum:
    print('Good job! You guessed the number in ' + str(guessAttempt) + ' guesses!')
else:
    print('Nope. The number I guessed was ' + str(secretNum) + ' try again later ;)')
