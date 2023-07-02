#! /usr/bin/python3

# say you have a value like this:
# spam = ['apples','bananas','tofu','cats']
# Write a function that takes a list value as an argument and returns a string
# with all the items separated by a comma and a space, with and inserted before
# the last item
# example: 'apples, bananas, tofu, and cats'

userList = []

def outList(item):

    userList.append(item)

    if item == 'exit':
        userList.remove('exit')
        userList[-1] = "and " + userList[-1]
        return ', '.join(userList)
    
while True:
    item = input('enter an item, otherwise type exit: \n')

    if item == 'exit':
        print(outList(item))
        break
    else:
        outList(item)