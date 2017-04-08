#!/usr/bin/env python3
# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus

import os

"""
def userDir(path):
    if os.path.exists(path) and os.path.isfile(path):
        filePath = open(path)
        fileContent = filePath.read()
        print(fileContent)
    else:
        print("The path you entered was invalid and not a file.")

answer = None

while answer != 'No.':
    answer = input('Please insert a file path: ')
    userDir(answer)
    print()
    answer = input("Do you wish to continue? \n(Insert No. to stop.)")
"""

sonnetFile = open('sonnet29.txt')
print(sonnetFile.readlines())
