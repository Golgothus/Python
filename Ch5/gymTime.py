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


print(legDay.keys()[1][2])


print('Exercises to be done on legday: ')
print('Leg Press with - ' + str(workout(legDay, 'Leg Press')))
print('Leg Extensions - ' + str(workout(legDay, '8 Reps')))
print('Leg Curls - ' + str(workout(legDay, '8 Reps')))
print('Calf Raises - ' + str(workout(legDay, '8 Reps')))
