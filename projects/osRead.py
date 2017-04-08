#!/usr/bin/env python3
# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus

import os

# if user wants to read file
# if user wants to write to file
# if user wants to create a file
# if user wants to overwrite a file
# if user wants to save a file

def filePath(userFile):
        if os.path.isfile(userFile):
            openFile = open(userFile)
            fileContent = openFile.read()
            print(fileContent)
        elif os.path.isfile(userFile) and os.path.exists()
    else:
        print("The path you entered was invalid and not a file.")

answer = None

while answer != 'No.':
    path = input('First, insert an existing file path: ')
    if not os.path.exists(path):
        answer = input('Would you like to read, write, or overwrite file?')
        if answer == 'read':
            fileRead(path)
            break
        elif answer == 'write':
            fileWrite(path)
            break
        elif answer == 'overwrite':
            fileOw(path)
            break
        else:
            print('You did insert a proper response.')

    answer = input('''Do you wish to continue?
(Insert \"No.\" to stop.)
Input = ''')
