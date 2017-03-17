# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus
# Chapter 5 - Dictionaries

movies = {'The Good Dinosaur': 'November 25, 2015 - Pixar Animation Studios', \
'Zootopia': 'March 4, 2016 - Walt Disney Animation Studios', \
'Moana': 'November 23, 2016 - Walt Disney Animation Studios'}

print(movies.keys())

while True:
    print("Please enter a recent release from Disney to view its airing date.")
    name = input()
    if name == '':
        break

    if name in movies:
        print('The release date is - ' + movies[name])
    else:
        print('The movie was not found.')
        print('When is its release date?')
        release = input()
        movies[name] = release
        print('Your movie has been added, sorry for the inconvenience!')
