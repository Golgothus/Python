# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# Ch. 2

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (it is a fish.)')
    password = input()
    if password == 'swardFish':
        break
print('Access Granted. Welcome, Joe.')
