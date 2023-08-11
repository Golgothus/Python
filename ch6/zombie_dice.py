#! /usr/bin/python3

import zombiedice
import random

class my_zombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class on_a_roll:
    def __init__(self, name):
    # All zombies must have a name:
        self.name = name

    # A bot that, after the first roll, randomly decides if it will continue or stop

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        roll_count = 0

        while diceRollResults is not None:
            brains += diceRollResults['brains']
            roll_count += 1
            roll_or_go = list(range(1,1000))
            random_index= random.randrange(1,1000)
            #print(f"Amount of rolls this round - {roll_count}")

            if roll_or_go[random_index-1] > 25:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class the_brains:
    def __init__(self, name):
    # All zombies must have a name:
        self.name = name

    # A bot that stops rolling after it has rolled two brains

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains <= 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class the_brawn:
    def __init__(self, name):
    # All zombies must have a name:
        self.name = name

    # A bot that stops rolling after it has rolled two shotguns

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        shotties = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotties += diceRollResults['shotgun']

            if shotties < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class the_escapist:
    def __init__(self, name):
    # All zombies must have a name:
        self.name = name

    # A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        roll_count = 0

        while diceRollResults is not None:
            brains += diceRollResults['brains']
            roll_count += 1
            print(f"Number of shotguns rolled - {diceRollResults['shotgun']}")

            if diceRollResults['shotgun'] == 3:
                print('I just wanted to talk about your extended warranty! ... --GASP-- ZRRROWWWW SKRRREEEE --POW, POW, POW--')
            if diceRollResults['shotgun'] < 2:
                print(f"Too risky. Number of shotguns rolled - {diceRollResults['shotgun']}")
                break
            elif roll_count < 4:
                diceRollResults = zombiedice.roll() # roll again
            else:
                print(roll_count)
                break

class the_hunger:
    def __init__(self, name):
    # All zombies must have a name:
        self.name = name

    # A bot that stops rolling after it has rolled more shotguns than brains

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        shotties = 0

        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotties += diceRollResults['shotgun']

            if shotties < brains:
                print("heh heh, need br-r-r-r-r-ain")
                print(f"total brain accumulated: {brains}")
                diceRollResults = zombiedice.roll() # roll again
            else:
                print("over c-c-c-c-c-onfident --BAM--")
                break 


zombies = (
    #zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    #zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    #zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    my_zombie(name='Patient 0'),
    # Add any other zombie players here.
    on_a_roll(name='One and run?'),
    the_brains(name='The brains'),
    the_brawn(name='The muscle'),
    the_escapist(name='The escape artist'),
    the_hunger(name='Famine')
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=10)
