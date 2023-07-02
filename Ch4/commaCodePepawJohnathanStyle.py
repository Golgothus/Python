#! /usr/bin/python3

# say you have a value like this:
# spam = ['apples','bananas','tofu','cats']
# Write a function that takes a list value as an argument and returns a string
# with all the items separated by a comma and a space, with and inserted before
# the last item
# example: 'apples, bananas, tofu, and cats'


def banner():
    return '''
    _____                              _       _                 _   _                               
    |  __ \                            | |     | |               | | | |                              
    | |__) |__ _ __   __ ___      __   | | ___ | |__  _ __   __ _| |_| |__   __ _ _ __    _ __  _   _ 
    |  ___/ _ \ '_ \ / _` \ \ /\ / /   | |/ _ \| '_ \| '_ \ / _` | __| '_ \ / _` | '_ \  | '_ \| | | |
    | |  |  __/ |_) | (_| |\ V  V / |__| | (_) | | | | | | | (_| | |_| | | | (_| | | | |_| |_) | |_| |
    |_|   \___| .__/ \__,_| \_/\_/ \____/ \___/|_| |_|_| |_|\__,_|\__|_| |_|\__,_|_| |_(_) .__/ \__, |
            | |                                                                        | |     __/ |
            |_|                                                                        |_|    |___/ 
    '''           


userList = []


def outList(item):

    userList.append(item)

    if item == 'exit' and range(len(userList) == 1):
        userList.remove('exit')

        return 'Program closing, no items provided.'
    elif item == 'exit':
        userList.remove('exit')
        userList[-1] = "and " + userList[-1]
        return ', '.join(userList)
    
    
print(banner())


while True:
    item = input('enter an item, otherwise type exit: \n')

    if item == 'exit':
        print(outList(item))
        break
    else:
        outList(item)