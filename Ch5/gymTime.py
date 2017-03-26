# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus
# Chapter 5 - Dictionaries

press = {
    'workout': 'Press',
     '8 Reps': 270,
     '6 Reps': 320,
     '4 Reps': 360
}
extensions = {
    'workout': 'Extensions',
    '8 Reps': 110,
    '6 Reps': 140,
    '4 Reps': 160
}
curls = {
    'workout': 'Curls',
    '8 Reps': 80,
    '6 Reps': 120,
    '4 Reps': 140
}
raises = {
    'workout': 'Calf Raises',
    '8 Reps': 90,
    '6 Reps': 110,
    '4 Reps': 140
}

exercises = (press,extensions,curls,raises)

for e in exercises:
    print('We will be working with - {r}'.format(r=str(e['workout'])))
    print('First set {r} at 8 reps.'.format(r=str(e['8 Reps'])))
    print('Second set {r} at 6 reps.'.format(r=str(e['6 Reps'])))
    print('Finishing with  {r} at 4 reps.'.format(r=str(e['4 Reps'])))
    print()

for e in exercises:
    for key in e:
        if 'Reps' in key:
            print("We will be working {workout} with - {amount} at {reps}".format(workout=key,amount=e[key], reps=key))
    print()