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


def rex_phone_number():
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
    matches = []

    for groups in rex_phone_number().findall(copied_text):
        if groups[1] != "":
            phone = "-".join([groups[1], groups[3], groups[5]])
        else:
            continue
        if groups[7] != "":
            phone += " x" + groups[8]
        matches.append(phone)

    return matches


# TODO: Copy results to the clipboard

# print(clip_text(pyperclip.paste()))
# print(clip_text(pyperclip.paste()))
phone_numbers = clip_text(pyperclip.paste())
new_phone = ""
for number in phone_numbers:
    new_phone += number + "\n"

print(new_phone)
