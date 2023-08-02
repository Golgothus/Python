#! /usr/bin/python


"""
Test with start/endswith functions.
"""


def string_start(text, findstr):
    """
    Test with start/endswith functions
    """
    while True:
        # the following will set input to UPPER, and check if it endswith find.upper()
        if text.upper().endswith(findstr.upper()):
            print(f"User input ends with find.upper(): {findstr.upper()}")
        elif text.upper().startswith(findstr.upper()):
            print(f"User input starts with find.upper(): {findstr.upper()}")
        else:
            print("This did not work as presumed.")
            break


def str_split(text):
    """
    Turns the string to lower
    Splits the string based on the character 'm'
    """
    print(text.lower().split("m"))


def str_part(text):
    """
    This will create a tuple, breaking the string down
    to the following pieces:
    before, sep, after
    """
    print(text.partition(","))


def str_padded(text):
    """
    Following examples are for justified / aligned text
    """
    print(text.rjust(20, "="))
    print(text.center(20, "="))
    print(text.ljust(20, "="))


def str_strip(text):
    """
    Example for strip()
    """
    print(text.strip("heto"))


print("Type some text:")
user_input = input()
str_padded(user_input)
str_strip(user_input)
