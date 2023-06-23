#! /usr/bin/python3

catNames = []

while True:
    print(f'Enter the name of a cat {str(len(catNames) + 1)} or press enter to exit.')
    name = input()
    if name == '':
        break
    catNames += [name]

print('The cat names are:')

for n in catNames:
    print(f' - {n}')