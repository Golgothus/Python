#! /usr/bin/python3

"""
Function to validate password string it is passed is strong.
Requirements:
- 8 characters long
- 1 Uppercase
- 1 lowercase
- 1 digit
You may need to test the string against multiple regex patterns to validate its strength.
"""

import re


def password_rex():
    """
    Password RegEx to match on the following:
    - at least 8 characters in length
    - 1 digit
    - 1 uppercase
    - 1 lowercase
    """

    rex = re.compile(r"[a-z]+|[A-Z]+|[0-9]+")
    return rex


def password_validation(self):
    """
    Takes input text
    Runs input against password_rex()
    """

    matches = re.findall(password_rex(), self)

    if len(self) >= 8 and repeat_characters(self) is not True:
        for mo in matches:
            if mo.islower() is True:
                continue
            if mo.isupper() is True:
                continue
            if mo.isdigit() is True:
                continue
        print(f"{self} is a usable password.")
    else:
        print(
            """
        Create a phrase longer than 8 characters.
        Required:
        - one uppercase letter
        - one lowercase letter
        - one digit
        - Refrain from repeating a character 5 times or more
        """
        )


def repeat_characters(self):
    """
    Validates the password does not contain
    consecutive, repeating values
    """

    repeat = {}

    for k in self:
        if k not in repeat:
            repeat[k] = 1
        else:
            repeat[k] += 1

    for v in repeat.values():
        if v >= 5:
            return True

    return False


USER_TEXT = "!FasterThanLight1"
USER_TEXT2 = "Aaaaaaaaaaaaaaaaaa1"
USER_TEXT3 = "Small1"
USER_TEXT4 = "UsablePassword1"
password_validation(USER_TEXT)
password_validation(USER_TEXT2)
password_validation(USER_TEXT3)
password_validation(USER_TEXT4)
