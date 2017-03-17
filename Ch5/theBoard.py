# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus
# Chapter 5 - Dictionaries
import pprint

message = 'Ah you think darkness is your ally? You merely adopted the dark. \
I was born in it. I didn\'t see the light until I was already a man, \
by then it was nothing to me but blinding!'
letterCount = {}

for character in message:
    letterCount.setdefault(character, 0)
    letterCount[character] = letterCount[character] + 1

pprint.pprint(letterCount)


food = {'Apples': 'I am an apple!', 'Bananas': 'I\'m the best banana there \
ever was!', 'Kiwis': 'I\'m a fruit of the tropical variety!'}

print('The apple says - \'' + food.get('Batman', 'Batman DOESN\'T EXIST!')
 + '\'.')
