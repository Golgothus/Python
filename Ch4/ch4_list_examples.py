#! /usr/bin/python


languages = ['Powershell','Python','HTML','CSS','jQuery']


def regularList(list):
    # The following is an example of a regular list
    #languages = ['Powershell','Python','HTML','CSS','jQuery']
    return len(list)

    
    print('List of languages I\'m slightly familiar with, are as follows:')


    for l in list:
        print(f'- {l}')


def multiList():
    # The following is an example of a multi list
    # To enumerate both lists, you would need to import the zip package
    multiValueList = [['1','2','3','4'],['splunk','IDS','IPS','KQL']]
    
    
    for item in multiValueList:
        print(item)


    print(multiValueList[0][3]) # prints the item from list 0, with index 3
    print(multiValueList[1][3]) # prints the item from list 1, with index 3


def negativeList(list):
    print(list[-4])
    print(list[-3])
    print(list[-2])
    print(list[-1])
    print(list[0])


def sliceList(list):
    print(list)
    # you can additionally leave out the second integer
    # which will print the starting index:length_of_the_list
    print(f'Printing slice [3:], {list[3:]}')
    print(f'Printing slice [1:], {list[1:]}')
    print(f'Printing slice [0:], {list[0:]}')
    print(f'Printing slice [:3], {list[:3]}')


def getListLen(list):
    return len(list)


def changeList(list):
    print(list)
    list[1] = 'special'
    print (list)


def catList(list):
    newList = ['test1','test2','test3']
    newList = newList + list
    print(newList)
    newList = newList * 3
    return newList


def remList(list):
    print(list)
    del list[1]
    print(list)


print('Running regularList()')
regularList(languages)
print('Running multiList()')
multiList()
print('Running negativeList()')
negativeList(languages)
print('Running sliceList():')
sliceList(languages)
print('Running getListLen():')
print(getListLen(languages))
print('Running changeList():')
changeList(languages)
print('Running catList():')
catList(languages)
print('Running remList():')
remList(languages)
regularList(languages)