#! /usr/bin/python

import random
import sys


balance = 2500
chance = random.randint(0,100)

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
    global chance
    if chance <= 49:
        print('Your loss is my win.')
        balance = removeFunds(bet)
    elif chance == 20:
        print('Holy shit, nat 20!')
        balance = getBalance() + (bet * 4)
    else:
        print('Luck is on your side.')
        balance = addFunds(bet)
    chance = random.randint(0,100)


def getBalance():
    return balance


def addFunds(bet):
    return getBalance() + (bet * 1.5)


def removeFunds(bet):
    return getBalance() - bet


def rig():
    global chance

    flip = random.randint(0,1)

    if flip == 0:
        chance = chance - 10
        print("""
        Baby don't hurt me.
        Don't hurt me.
        No more.
        """)
        return chance
    else:
        print("""
        Hold up, wait a minute, put a little LOVE in it!
        """)
        chance += random.randint(1,5)
        return chance

       
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
    elif response == '3':
        rig()
    elif response == 'exit' or response == '4' :
        sys.exit()


def banner():
   print("""

  ________              ___.   .__             __________        
 /  _____/_____    _____\_ |__ |  |   ____     \______   \___.__.
/   \  ___\__  \  /     \| __ \|  | _/ __ \     |     ___<   |  |
\    \_\  \/ __ \|  Y Y  \ \_\ \  |_\  ___/     |    |    \___  |
 \______  (____  /__|_|  /___  /____/\___  > /\ |____|    / ____|
        \/     \/      \/    \/          \/  \/           \/     

by: Golgothus (with assistance from SneakerHax)

    """)

banner()

while True:
    getMenu()
    userInput()