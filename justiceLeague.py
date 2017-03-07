# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus
# Chapter 4 - Lists
# Code takes a users input and creats a list

justiceLeague = []
while True:
    print('Enter the name of hero #' + str(len(justiceLeague) + 1 ) +
    ' (Or enter nothing to stop.):')
    hero = input()
    if hero == '':
        break
    justiceLeague = justiceLeague + [hero] # list concatination

print('You have chosen: ')
for hero in justiceLeague:
    print(' ' + hero + ' to be in your Justice League.')
