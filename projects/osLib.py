#!/usr/bin/env python3
# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus

import os

def userDir(path):
    if os.path.exists(path) and os.path.isdir(path):
        val = 'Your input is a directory.'
        print(val)
    elif os.path.exists(path) and os.path.isfile(path):
        val = 'Your input is a file.'
        print(val)
    else:
        val = 'Please adjust your input to either a file or a directory.'
        print(val)

answer = None

while answer != 'No.':
    path = input('Please insert a directory or a file: ')
    userDir(path)
    print()
    answer = input("Do you wish to continue? ")
