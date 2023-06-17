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
    chance = random.randint(0,100)
    if chance <= 49:
        print('Your loss is my win.')
        removeFunds(bet)
    elif chance == 20:
        print('Holy shit, nat 20!')
        balance = getBalance() + (bet * 4)
        return balance
    else:
        print('Luck is on your side.')
        addFunds(bet)


def getBalance():
    return balance


def addFunds(bet):
    balance = getBalance() + (bet * 1.5)
    print(balance)
    return getBalance() + (bet * 1.5)


def removeFunds(bet):
    #balance = getBalance() - bet
    print(balance)
    return getBalance() - bet


# def rig():

       
def userInput():
    response = input()

    if response == '1':
        getBalance()
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