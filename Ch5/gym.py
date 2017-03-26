# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus
# Chapter 5 - Dictionaries MOAR work WITH Dictionaries, because I'm a masochist

exercises = {
    'Squats': {
        '8 Reps': 140,
        '6 Reps': 180,
        '4 Reps': 220
    },
    'Leg Press': {
        '8 Reps': 270,
        '6 Reps': 320,
        '4 Reps': 360
    },
    'Leg Extensions': {
        '8 Reps': 110,
        '6 Reps': 140,
        '4 Reps': 160
    }
}

for e in exercises:
    print('When working with {exercise} -'.format(exercise=e))
    for r in exercises[e]:
        print('Starting with {weight}lbs. we will do a working set of {reps}.'.format(reps=r,weight=exercises[e][r]))
    print()