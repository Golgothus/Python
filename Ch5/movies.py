# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus
# Chapter 5 - Dictionaries

movies = {
    'The Good Dinosaur': 'November 25, 2015 - Pixar Animation Studios',
    'Zootopia': 'March 4, 2016 - Walt Disney Animation Studios',
    'Moana': 'November 23, 2016 - Walt Disney Animation Studios'
}

# k will pull in the index for the dict key
print("Upcoming Disney releases!")
for k in movies:
    print(k)

print('')

# The loop below will run until the user presses enter
# This loop will check the dictionary, if there is a key
# It will output the key-value pair
# If no key is found, it will allow for the user to add one

while True:
    print('Please enter a recent release from Disney to view its airing date.')
    print('(Leave blank to quit)')
    name = input()
    if name == '':
        break
    if name in movies:
        print('The release date is - ' + movies[name])
    else:
        print('The movie was not found.')
        release = input('When is its release date?')
        movies[name] = release
        print('Your movie has been added, sorry for the inconvenience!')
