# Python Quick Reference Guide

This document will provide references to things I've found useful while reading [Automate the Boring Stuff with Python 2nd Edition](https://automatetheboringstuff.com/2e).

[TOC]

## Useful methods

- id()
- dir()
- keys()
- values()
- items()
- isx()
- .join()
- .split()
- .startswith()
- .endswith()

## Pattern Matching

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

> Reference: [Automate the Boring Stuff with Python, 2nd Edition by Al Sweigart, Chapter 7 "Review of Regular Expression Matching"](https://automatetheboringstuff.com/2e/chapter7/#calibre_link-1143)

The following items will need to be escaped if attempting to capture them in patterns using regex:

`.  ^  $  *  +  ?  {  }  [  ]  \  |  (  )`

## Useful readings

- [Scoping / Global Variables](https://stackoverflow.com/questions/17911831/python-global-variable-not-updating)
- [Click Module](https://click.palletsprojects.com/en/8.1.x/)
- [PEP-8 Standard](https://peps.python.org/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds)
- [Python 3 Documentation](https://docs.python.org/3/tutorial/index.html)

## Setup your Python Environment

### Choose your IDE / Text Editor

IDE's:
- [Visual Studio Code](https://code.visualstudio.com/)
- [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows)

Text Editor's:
- [Notepad++](https://notepad-plus-plus.org/downloads/)
- [SublimeText](https://www.sublimetext.com/)
- Vim
- nano

### Install PIP
1. Python3 should already come pre-packaged with pip
2. Check if Python is installed:
```bash
python --version
pip -V
```
> reference: https://www.geeksforgeeks.org/how-to-install-pip-on-windows/

### Setting up your virtual environment

- First we'll install the virtualenv module via pip
- Run the following in your shell:
  ```python
  python3 -m pip install virtualenv
  ```
- Navigate to your working directory for Python in your terminal.
- Run the following command:
  ```bash
  python3 -m venv ./
  ```
- This will create a virtual environment in your current working directory
- To activate the environment, type `./scripts/activate` in your shell

> Reference: https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/

## Learning Resources

- [Automate the Boring Stuff with Python 2nd Edition](https://automatetheboringstuff.com/2e)
- [Python for Defenders](https://taggartinstitute.org/p/python-for-defenders-pt1)]