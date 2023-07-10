#! /usr/bin/python

import string

chessBoard = {}
alphabet = string.ascii_lowercase

def makeBoard():
    keyList = []
    for row in range(8,0,-1):
        #print()
        for column in range(0,8,1):
            #print(f'{alphabet[column]}{row} | ',end='')
            keyList.append(alphabet[column]+str(row))

    #print(f'Length of keyList is {len(keyList)}')
    return keyList
            #boardList.append(alphabet[column]+str(row))

def chessBoardDict():
    for d in makeBoard():
        chessBoard[d] = None
    return chessBoard

print(type(chessBoardDict()))