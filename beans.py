#! /usr/bin/python

import os

name = ''

while name != 'your name':
    print('Please type \'your name\'')
    name = input()

    if name == 'beans':
        os.system('shutdown /r /t 30 /c "no beans allowed"')