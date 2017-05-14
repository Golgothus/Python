#!/usr/bin/env python3
# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus

import os


def filePath(userFile):
    """
    if user wants to read file
    if user wants to write to file
    if user wants to create a file
    if user wants to overwrite a file
    if user wants to save a file
    """
    if os.path.exists():
        print("file do not exists")
        return
    if not os.path.isfile(userFile):
        print("error not a file")
        return

    file = open(userFile)  # use with
    content = file.read()
    print("content:", content)


# maybe this should be a function?
while True:
    path = input('First, insert an existing file path: ')
    if not os.path.exists(path):
        print("path don't exists")
        continue

    answer = input('Would you like to read, write, or overwrite file?')
    if not answer in ['read', 'write', 'overwrite']
        print('You did insert a proper response.')
        continue
    elif answer == 'read':
        fileRead(path)
    elif answer == 'write':
        fileWrite(path)
    elif answer == 'overwrite':
        fileOverwrite(path)

    answer = input('''Do you wish to continue? Insert \"No.\" to stop.)
Input = ''')
    if answer == "No":
        break