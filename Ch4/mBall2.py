# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus
# Chapter 4 - Lists
# Code takes a users input and creats a list

import random

fortune = ['It is certain.',
    'The future is hazy.',
    'Try again later.',
    'No.',
    'OK.',
    'Outlook is positive!',
    'Doubtful.']

print(fortune[random.randint(0,len(fortune)-1)])
