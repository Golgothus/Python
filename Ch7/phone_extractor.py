#! /usr/bin/python

# Get the text off the clipboard.
# Find all phone numbers and email addresses in the text.
# Paste them onto the clipboard.
# Use the pyperclip module to copy and paste strings.
# Create two regexes, one for matching phone numbers and the other for matching email addresses.
# Find all matches, not just the first match, of both regexes.
# Neatly format the matched strings into a single string to paste.
# Display some kind of message if no matches were found in the text.

import pyperclip, re

def rex_phone_number(item):
    phone_regex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?              # area code
        (\s|-|\.)?                      # separator
        \d{3}                           # middle 3 of number
        (\s|-|\.)                       # separator
        \d{4}                           # last 4 of number
        (\s*(ext|x|ext.)\s*\d{2,5})?    # extension, if present
        )''',re.VERBOSE)

    print(item)

    mo = phone_regex.search(item)
    return mo.groups()

def rex_email(item):
    email_regex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+
        @
        [a-zA-Z0-9.-]+
        (\.[a-zA-Z]{2,63})
        )''',re.VERBOSE)

def clip_text():
    matches = []
    #text = str(pyperclip.paste())

    print(rex_phone_number("999-999-9999"))

    rex_email(text)

# TODO: Copy results to the clipboard

clip_text()