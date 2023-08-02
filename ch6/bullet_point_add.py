#! /usr/bin/python
# bullet_point_add.py

import pyperclip

"""
script will get the text from the clipboard
add a star and space to the beginning of each line
and then paste this new text to the clipboard
"""

# text = "Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars"
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)