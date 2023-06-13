#! /usr/bin/python


def regularList():
    # The following is an example of a regular list
    languages = ['Powershell','Python','HTML','CSS','jQuery']
    listLen = len(languages)

    
    print('List of languages I\'m slightly familiar with, are as follows:')


    for l in languages:
        print(f'- {l}')


def multiList():
    # The following is an example of a multi list
    # To enumerate both lists, you would need to import the zip package
    multiValueList = [['1','2','3','4'],['splunk','IDS','IPS','KQL']]
    
    
    for item in multiValueList:
        print(item)


    print(multiValueList[0][3]) # prints the item from list 0, with index 3
    print(multiValueList[1][3]) # prints the item from list 1, with index 3


def negativeList():
    languages = ['Powershell','Python','HTML','CSS','jQuery']

    print(languages[-4])
    print(languages[-3])
    print(languages[-2])
    print(languages[-1])
    print(languages[0])

print('Running regularList()')
regularList()
print('Running multiList()')
multiList()
print('Running negativeList()')
negativeList()