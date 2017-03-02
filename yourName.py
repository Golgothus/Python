# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# Ch. 2 While Statements

name = ''
while name.lower() != 'your name':
# Above statment makes the users input and forces it to all lower case
    print('Please type \'your name\'.')
    name = input()

print('Thank you.')

print('')
print('-----')
print('')
# Break Statements

while True:
    print('Please type your name.')
    name = input().lower()
    if name == 'your name':
        break
print('Thanks!')
