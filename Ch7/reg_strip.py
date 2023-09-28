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


def reg_strip(self, rex=None):
    """
    if rex = None:
        self.strip()
    Else:
        Characters specified in the second argument to the function will be removed from the string.
    """

    user_input = self

    if rex == None:
        return user_input.strip()
    else:
        return string_strip(user_input, rex)


user_input = "     Pickles are my favorites      "
print(user_input)
print(reg_strip(user_input))
print(reg_strip(user_input, "Pckea"))
