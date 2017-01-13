# Beginning of the end.
# I'm embariking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# Ch. 2 Boolean Statements

#Prompt user for name

print('What is your name?')
name = input()
print('What is your age?')
age = int(input())

if name == 'Alice':
    print('Hi, Alice.')
elif age < 45:
    print('Nice try, bucko.')
elif age > 45:
    print('You are not Alice, bb kun.')
elif age > 200:
    print('Uh, you dead. Less you\'re some kind of immortal being...')
elif age > 100:
    print('But... How old are you really?')

# Problem with elif statements is the first one true
# is the condition that will be executed

print()
print()
print('-----')
print()
print()

if name == 'Alice':
    print('Hi Alice.')
elif age < 30:
    print ('Whaddup governa, you aren\'t Alice doe.')
else:
    print ('Well what a shame! You failed everything!')

print()
print()
print('-----')
print()
print()

# This section contains a bug because one of the Statements
# will never occur

if name == 'Alice':
    print('Hi Alice.')
elif age < 30
    print('Aight, you younger than 30')
elif age > 100
    print('You old.')
elif age > 2000 # this statement will never occur
    print('Love me :C')
