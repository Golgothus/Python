#! /usr/bin/python

name = ''


while not name:
    print('Enter your name.')
    name = input()


print('How many guests?')


guests = ''

while not guests:
    guests = int(input())
    print('Be sure to have a enough room for all of your guest(s)')


    if not guests:
        print('You\'re having a party, at least invite one person.')
        print('How many guests?')


print('Done.')