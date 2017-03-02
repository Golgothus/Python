"""
Beginning of the end.
I'm embarking on my journey to learn Python
These comments will always be in the beginning of my programs
Enjoy, Golgothus
https://github.com/Golgothus
Ch. 3 Functions
"""

import sys

while True:
    print('Type exit to close.')
    userText = raw_input()
    if userText.lower() == 'close':
        sys.exit()
    print('The program did not close because you typed \'' + userText.lower() + '\'.')
