# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus
# Chapter 4 - Lists
# Practice assignment for Chapter 4
spam = []

def passList(i):
    spam.append(i)

response = ''

while response != 'No.':
    print('Insert items to a list below: ')
    passList(input())
    print('Would you like to continue adding items?')
    response = input()

print(spam)
