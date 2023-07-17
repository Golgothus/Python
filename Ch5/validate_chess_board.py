#! /usr/bin/python

'''
In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board. Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h';
that is, a piece can’t be on space '9z'.

The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.

This function should detect when a bug has resulted in an improper chess board.

https://en.wikipedia.org/wiki/Algebraic_notation_(chess)
'''

import string

chessBoard = {}
ALPHABET = string.ascii_lowercase

def test_make_board():
    '''Creates a dictionary as reference for the \'physical\' board.'''
    for row in range(8,0,-1):
        print()
        for column in range(0,8,1):
            print(f'{ALPHABET[column]}{row} | ',end='')

def make_board():
    '''Creates the list item which will be fed into the KeyList for the Chess Board dictionary variable.'''
    key_list = []

    for row in range(8,0,-1):
        for column in range(0,8,1):
            key_list.append(ALPHABET[column]+str(row))

    return key_list

def chess_board_dict():
    '''Creates the dictionary variable and assigns its KeyList values.'''
    for d in make_board():
        chessBoard[d] = None
    return chessBoard

#def add_dict():
#    '''Takes the value and assigns to the associated key pairing from the chessBoard dictionary.'''

def is_valid_chess_board(chessBoardDict):
    '''
    A valid board will have exactly:
    - one black king and exactly one white king

    Each player can only have:
    - 16 pieces, out of the 16, 8 will be pawns
    - all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'.
    '''

    check_pieces(chessBoardDict)
    check_position(chessBoardDict)

def check_pieces(pieces):
    '''Checkes pieces are valid.'''

    count = {}

    for piece in pieces:
        count.setdefault(piece,0)
        count[piece] = count[piece] + 1

    print(count)


def check_position(pieces):
    '''Checks the placement is valid.'''

print(chess_board_dict())
test_make_board()
#is_valid_chess_board(chess_board_dict)
check_pieces(chessBoard)
