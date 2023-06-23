#! /usr/bin/python3

myPets = ['banana','Leo','Captain Marcus St. John','Dobby','DABI']

while True:
    name = input('Enter a pet name:')

    if name == '':
        break
    if name not in myPets:
        print('I don\'t know you, that\'s my pet!')
    else:
        print(f'{name} is one of my pets.')
        print(f'You may pet {name}.')