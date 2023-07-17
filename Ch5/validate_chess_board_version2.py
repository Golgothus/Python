#! /usr/bin/python3

'''
Used the baseline of steps for this application, defined at:

https://stackoverflow.com/a/60029522

Define the set of all chess pieces
Define the valid count range of pieces by type
Count the pieces on the board
Check pieces counts in a valid range
Check that positions are valid
Check that pieces names are valid
'''

all_pieces = []
player_color = ['b','w']
piece_type = ['king','queen','bishop','knight','rook','pawn']
piece_count = {
    'king': (1,1),
    'queen': (0,1),
    'bishop': (0,2),
    'knight': (0,2),
    'rook': (0,2),
    'pawn': (0,8)
    }

for color in player_color:
    for piece in piece_type:
        all_pieces.append(color + piece)

print(all_pieces)
