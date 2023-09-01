#! /usr/bin/python

"""
Get the text off the clipboard.
Find all phone numbers and email addresses in the text.
Paste them onto the clipboard.
Use the pyperclip module to copy and paste strings.
Create two regexes, one for matching phone numbers and the other for matching email addresses.
Find all matches, not just the first match, of both regexes.
Neatly format the matched strings into a single string to paste.
Display some kind of message if no matches were found in the text.
"""

import re
import pyperclip


def rex_phone_number():
    """
    Pattern matching for phone numbers.
    """
    phone_regex = re.compile(
        r"""(
        (\d{3}|\(\d{3}\))?              # area code
        (\s|-|\.)?                      # separator
        (\d{3})                           # middle 3 of number
        (\s|-|\.)                       # separator
        (\d{4})                           # last 4 of number
        (\s*(ext|x|ext.)\s*\d{2,5})?    # extension, if present
        )""",
        re.VERBOSE,
    )
    return phone_regex


def rex_email():
    """
    Pattern matching for emails.
    """
    email_regex = re.compile(
        r"""(
        [a-zA-Z0-9._%+-]+
        @
        [a-zA-Z0-9.-]+
        (\.[a-zA-Z]{2,63})
        )""",
        re.VERBOSE,
    )
    return email_regex


def clip_text(copied_text):
    """
    Runs necessary pattern matching functions against the copied_text
    Returns any found matches
    """
    matches = []

    for groups in rex_phone_number().findall(copied_text):
        if groups[1] != "":
            phone = "-".join([groups[1], groups[3], groups[5]])
        else:
            continue
        if groups[7] != "":
            phone += " x" + groups[8]
        matches.append(phone)

    #    for groups in rex_email().findall(copied_text):
    for groups in rex_email().findall(copied_text):
        email = ""
        if groups[0] in matches:
            continue
        else:
            email += groups[0]
        matches.append(email)

    return matches


# running initial function to kick off clip_text
match_objects = clip_text(pyperclip.paste())
# Copy results to the clipboard
new_matches = ""
for matches in match_objects:
    new_matches += matches + "\n"
pyperclip.copy(new_matches)
print(new_matches)
