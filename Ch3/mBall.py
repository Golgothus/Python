# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus
# Ch. 3 Functions
import random

def mFortune(answer):
    if answer == 1:
        return 'Try again later.'
    elif answer == 2:
        return 'Chances are likely.'
    elif answer == 3:
        return 'You land a critical hit.'
    elif answer == 4:
        return 'You left your ammo in your other pants, gg.'
    elif answer == 5:
        return 'The goblin stole your coin purse, send help.'
    elif answer == 6:
        return 'You learn the \'steal\' skill, good luck adventurer!'
    elif answer == 7:
        return 'Why is this happening?'
    elif answer == 8:
        return 'Don\'t touch me there!'
    elif answer == 9:
        return 'Pay your bills, nerd.'
    elif answer == 10:
        return 'Do your homework, Dad.'
def roll():
    r = random.randint(1,10)
    fortune = mFortune(r)
    print('You rolled a ' + str(r) + ', your fortune is as follows:')
    print(fortune)

# I could combine the above by doing print(mFortune(random.randint(1,10)))

for i in range(1,20):
    roll()
    print('')
