#! /usr/bin/python

languages = ['Powershell','Python','HTML','CSS','jQuery','banana','grapes','Dobby']

def regularList(list):
    # The following is an example of a regular list
    #languages = ['Powershell','Python','HTML','CSS','jQuery']
    return len(list)

def multiList():
    # The following is an example of a multi list
    # To enumerate both lists, you would need to import the zip package
    multiValueList = [['1','2','3','4'],['splunk','IDS','IPS','KQL']]
    
    for item in multiValueList:
        print(item)
    
    print(multiValueList[0][3]) # prints the item from list 0, with index 3
    print(multiValueList[1][3]) # prints the item from list 1, with index 3

    return

def negativeList(list):
    print(list[-4])
    print(list[-3])
    print(list[-2])
    print(list[-1])
    print(list[0])

def getListLen(list):
    return len(list)

def changeList(list):
    list[1] = 'special'
    return

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

def sortList(list):
    print(f'Printing list in normal format: {list}')
    list.sort(key=str.lower)
    print(list)

def reverseList(list):
    print(f'Printing list in normal format: {list}')
    list.reverse()
    return list

print(f'Running regularList():')
regularList(languages)
print('Running multiList():')
multiList()
print(f'Running negativeList():')
negativeList(languages)
print(f'Running getListLen(): \n {getListLen(languages)}')
print(f'Running changeList(): \n {changeList(languages)}')
print('Running catList():')
catList(languages)
print('Running remList():')
remList(languages)
regularList(languages)
print('Running sortList():')
sortList(languages)
print('Running reverseList():')
print(reverseList(languages))