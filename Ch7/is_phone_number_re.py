#! /usr/bin/python

import re

message = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Contact:
Mobile: 111-222-4444
"""

def phone_rex(text):
    rex1 = re.compile(r'\d{3}-\d{3}-\d{4}')
    #rex2 = re.compile(r)

    mo1 = rex1.search(text)
    #area_code, main_number = mo2.groups()
    # in Python 3.8<=, := is the assignment operator, so in the line below we are setting a value to the variable match
    # reference - https://stackoverflow.com/questions/26000198/what-does-colon-equal-in-python-mean
    if (match := re.search(r'(\d{3})-(\d{3}-\d{4})',text)) is not None:
        #print(f'Items in group 1: {mo2.group(1)}')
        #print(f'Items in group 2: {mo2.group(2)}')
        print(match.group(1))
        print(match.group(2))
    #print(f'Total number of groups in the second match object: {len(mo2.groups())}')
    #print(f'({area_code}) {main_number}')

print(message)
phone_rex(message)


hero_rex = re.compile(r'Batman|Tina Fey')
mo1 = hero_rex.search('Batman and Tina Fey')
print(mo1.group())
mo2 = hero_rex.search('Tina Fey and Batman')
print(mo2.group())

# You can find all matching occurrences with the findall() method that’s discussed in “The findall() Method” on page 171.
# You can also use the pipe to match one of several patterns as part of your regex. For example, say you wanted to match any of the strings 'Batman', 'Batmobile', 'Batcopter', and 'Batbat'.

bat_rex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_rex.search('Batbat lost a finger.')
print(mo.group())

# () since this constitutes a group item in regex
# The following will return 'bat'
print(mo.group(1))

# optional pattern matching with the Question Mark
# The following will capture the previous group (wo) whenever it is presented in a match, along witht the required items after the ?
bat_rex = re.compile(r'Bat(wo)?man')
mo = bat_rex.search('Batwoman')
print(mo.group())

bat_rex = re.compile(r'Bat(wo)*man')
mo1 = bat_rex.search('The Adventures of Batman')
print(mo1.group())
mo2 = bat_rex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = bat_rex.search('The Adventures of Batwowowowowowoman')
print(mo3.group())

bat_rex = re.compile(r'Bat(wo)+man')
mo1 = bat_rex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = bat_rex.search('The Adventures of Batwowowowowowoman')
print(mo2.group())

if bat_rex.search('The Adventures of Batman') == None:
    print('No match on match object 3.')

greedy_rex = re.compile(r'(Ha){3,5}')
mo1 = greedy_rex.search('HaHaHaHaHa')
print(mo1.group())
non_greedy_rex = re.compile(r'(Ha){3,5}?')
mo2 = non_greedy_rex.search('HaHaHaHaHaHaHa')
print(mo2.group())

# caveat for findall() is that it will return a list of strings
# as long as there are no groups in the pattern
# if there are groups, a list of tuples will be returned

test_phone_rex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo1 = test_phone_rex.findall('Cell: 415-555-9999 Work: 212-555-0000')
phone = str(mo1[0][:]).replace('\', \'','-')
print(phone)
print(type(phone))

xmas_rex = re.compile(r'\d+\s\w+')
print(xmas_rex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

# you can make your own class by encapsulating characters in a []
# example, [aeiouAEIOU] would capture only these characters
# to capture _only_ letters, you could do [a-zA-Z] since
# there is no shorthand class for only letters
# The hyphen allows us to capture a range of values between points
# You do not need to escape characters within brackets
# they will be interpreted as literals
# Example: [\\share\path] will explicitly match on "\\share\path"
# To NOT match on a class, use the following:
# [^]
# Matching multiple groups:
# First Name: ([a-zA-Z.]*)\nLast Name: ([a-zA-Z]*)
# regex for matching on IP's
# ^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$
# \s((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}

# Complex RegEx
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

# Easier to read complex RegEx
phoneRegex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?
                        (\s|-|\.)?
                        \d{3}
                        (\s|-|\.)
                        \d{4}
                        (\s*(ext|x|ext.)\s*\d{2,5})?
                        )''',re.VERBOSE)
