#! /usr/bin/python

import re

message = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Contact:
Mobile: 111-222-4444
"""

def phone_rex(text):
    rex1 = re.compile(r'\d{3}-\d{3}-\d{4}')
    rex2 = re.compile(r'(\d{3})-(\d{3}-\d{4})')

    mo1 = rex1.search(text)
    mo2 = rex2.search(text)
    area_code, main_number = mo2.groups()

    print(f'Items in group 1: {mo2.group(1)}')
    print(f'Items in group 2: {mo2.group(2)}')
    print(f'Total number of groups in the second match object: {len(mo2.groups())}')
    print(f'({area_code}) {main_number}')

print(message)
phone_rex(message)
