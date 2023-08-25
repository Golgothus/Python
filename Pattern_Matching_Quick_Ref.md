# Pattern Matching Quick Reference

## Overview

This document will provide quick references to notation and pattern matching for RegEx in Python.

## Process

1. Import the regex module with `import re`.
2. Create a Regex object with the `re.compile()` function. (Remember to use a raw string.)
3. Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
4. Call the Match object’s group() method to return a string of the actual matched text.

Example of this process:

```Python
# this expression is to capture Phone-Numbers
phone_rex = re.compile(r'\d{3}-\d{3}-\d{4}')
# mo = shorthand for Match Object
# If there is a match against your Regular Expression, a Match object will be created
mo = phone_rex.search('Test Phone Number is: 111-222-3333')
print(f'Number found: {mo.group()}')
```

> Reference: [Automate the Boring Stuff with Python, 2nd Edition by Al Sweigart, Chapter 7 "Review of Regular Expression Matching"](https://automatetheboringstuff.com/2e/chapter7/)

The following items will need to be escaped if attempting to capture them in patterns using regex:

`.  ^  $  *  +  ?  {  }  [  ]  \  |  (  )`


## Notation Quick Reference

- The ? matches zero or one of the preceding group.
- The * matches zero or more of the preceding group.
- The + matches one or more of the preceding group.
- The {n} matches exactly n of the preceding group.
- The {n,} matches n or more of the preceding group.
- The {,m} matches 0 to m of the preceding group.
- The {n,m} matches at least n and at most m of the preceding group.
- {n,m}? or *? or +? performs a non-greedy match of the preceding group.
- ^spam means the string must begin with spam.
- spam$ means the string must end with spam.
- The . matches any character, except newline characters.
- \d, \w, and \s match a digit, word, or space character, respectively.
- \D, \W, and \S match anything except a digit, word, or space character, respectively.
- [abc] matches any character between the brackets (such as a, b, or c).
- [^abc] matches any character that isn’t between the brackets.

### Re-usable patterns for RegEx
```Python
# RegEx for matching on IP Addresses
print(r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$') # will match on a line starting, ending with an IP
print(r'\s((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}') # will look for patterns where a space precedes the IP
print(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

# RegEx for matching on a phone number
def rex_phone_number(item):
    phone_regex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?              # area code
                        (\s|-|\.)?                      # separator
                        \d{3}                           # middle 3 of number
                        (\s|-|\.)                       # separator
                        \d{4}                           # last 4 of number
                        (\s*(ext|x|ext.)\s*\d{2,5})?    # extension, if present
                        )''',re.VERBOSE)

# RegEx for matching on email
def rex_email(item):
    email_regex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+
        @
        [a-zA-Z0-9.-]+
        (\.[a-zA-Z]{2,63})
        )''',re.VERBOSE)
```

> Reference: https://automatetheboringstuff.com/2e/chapter7, Review of Regex Symbols 

There is also the book [Regular Expressions Cookbook](https://www.oreilly.com/library/view/regular-expressions-cookbook/9780596802837/) which has several pre-made patterns.