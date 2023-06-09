#! /usr/bin/python3


import sys


def collatz(userInput):
    if userInput % 2 == 0:
        print(userInput // 2)
        return userInput // 2
    elif userInput % 2 == 1:
        print(3 * userInput + 1)
        return 3 * userInput + 1


def userInput():
    print('Provide a userInput, or type \'exit\'.')
    response = input()


    if response == 'exit':
            sys.exit()
    else:     
        try:
            collatz(int(response))
        except ValueError:
            print('Value needs to be an integer.')


while True:
    userInput()