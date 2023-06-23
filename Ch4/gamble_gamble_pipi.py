#! /usr/bin/python

import random
import sys


balance = 2500


def getMenu():
    menu = f"""
    Step right up, lets play a game!
    Balance: {getBalance()}
    If you would like to stop playing, please type 'exit'.

    Here's the action menu:
    --- Type 1 to get your balance.
    --- Type 2 to place your bet.
    --- Type 3 to shake the machine.
    --- Type 4 or exit to leave the game.
    """

    print(menu)


def gamble(bet):
    global balance
    chance = random.randint(0,100)
    if chance <= 49:
        print('Your loss is my win.')
        balance = removeFunds(bet)
        return balance
    #elif chance == 20:
    #    print('Holy shit, nat 20!')
    #    balance = getBalance() + (bet * 4)
    else:
        print('Luck is on your side.')
        balance = addFunds(bet)
        return balance


def getBalance():
    global balance
    return balance


def addFunds(bet):
    return getBalance() + (bet * 1.5)


def removeFunds(bet):
    return getBalance() - bet


# def rig():

       
def userInput():
    response = input()


    if response == '1':
        print(f'Your current balance is {getBalance()}.')
    elif response == '2':
        try:
            bet = int(input('Enter bet amount:'))
            gamble(bet)
        except(ValueError):
            print('Value must be an integer.')
    #elif response == '3'
    elif response == 'exit' or response == '4' :
        sys.exit()


while True:
    getMenu()
    userInput()