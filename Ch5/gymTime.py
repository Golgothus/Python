# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus
# Chapter 5 - Dictionaries

legDay = {
    'Leg Press': {'8 Reps': 270, '6 Reps': 320, '4 Reps': 360},
    'Leg Extensions': {'8 Reps': 110, '6 Reps': 140, '4 Reps': 160},
    'Leg Curls': {'8 Reps': 80, '6 Reps': 120, '4 Reps': 140},
    'Calf Raises': {'8 Reps': 90, '6 Reps': 110, '4 Reps': 140}
}


def workout(reps):
    for e, r in reps.items():
        print(legDay[reps].items())

print('Exercises to be done on legday: ')
print('Potato ' + str(workout(legDay['Leg Press'])))
# print(str(workout(legDay, 'Leg Extensions')))
# print(str(workout(legDay, 'Leg Curls')))
# print(str(workout(legDay, 'Calf Raises')))

# print(legDay['Leg Extensions'])

