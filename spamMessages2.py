# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus
# Ch. 3 Functions

def hello(name):
    print('Hi, ' + name + '.')

message = ''

if message.lower() != 'No':
    print('Please enter your name: ')
    name = raw_input()
    hello(name)
    print('Would you like to close this program?')
    message = raw_input()
