#!/usr/bin/env python3
# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus

import os

path = input('Enter a path you\'d like to view the size of - ')
path = '//home/golgothus/' + path

print()
print('The directory you have opted into working with is as folows:')
print(os.path.dirname(path))

# print('The files within the directory you chose are below:')
# print(os.listdir(path))

print()
print('The amount of data within the directory is below:')
print(os.path.getsize(path))
# path = "//home/golgothus/Python/join.py"
# os.path.basename(path)
