# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# Ch. 2 Conditional Statements cont.

userName = ''
while not userName:
    print('Please enter your username:')
    userName = raw_input()
    print('How many keys will you need to purchase?')
    numKeys = raw_input()
    if numKeys:
        print('Make sure you have enough keys for your team.')
print('Donezo. You need ' +  str(10 + int(numKeys)) + ' number of keys.')
