#! /usr/bin/python3

import random

userList = []

while True:
    userInput = input("Add items to your list:")
    
    if userInput == "" or userInput == "exit":
        print('You either did not enter anything, or you typed exit.')
        print('Closing program.')
        break
    else:
        userList.append(userInput)
        print(f"""
            Your list is currently comprised of the following:
            {userList}
            """)

def catSlice():
    name = 'Zophie a cat'

    for i in range(len(name)):
        print(f'Index of {i} contains: {name[i]}')

catSlice()
# randIndex = random.randint(0,len(list) - 1)

def sliceList(list):
    print(list)
    # you can additionally leave out the second integer
    # which will print the starting index:length_of_the_list
    print(f'Printing slice [3:], {list[3:]}')
    print(f'Printing slice [1:], {list[1:]}')
    print(f'Printing slice [0:], {list[0:]}')
    print(f'Printing slice [:3], {list[:3]}')