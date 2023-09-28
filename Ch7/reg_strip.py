#! /usr/bin/python

"""
Write a function that takes a string and does the same thing as the strip() string method.
If no other arguments are passed other than the string to strip, 
then whitespace characters will be removed from the beginning and end of the string. 
Otherwise, the characters specified in the second argument to the function will be removed from the string.
"""

import re


def string_strip(text, characters):
    rex = f"[{characters}]"
    print(characters)
    return re.sub(rex, "---F's in chat---", text)


def reg_strip(text, rex=None):
    """
    if rex = None:
        text.strip()
    Else:
        Characters specified in the second argument to the function will be removed from the string.
    """

    if rex == None:
        return text.strip()
    else:
        return string_strip(text, rex)


text = "     Pickles are my favorites      "
print(text)
print(reg_strip(text))
print(reg_strip(text, "Pckea"))
