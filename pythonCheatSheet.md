# Python Quick Reference Guide

This document will provide references to things I've found useful while reading [Automate the Boring Stuff with Python 2nd Edition](https://automatetheboringstuff.com/2e).

[TOC]

## Useful methods

- id()
- dir()
- keys()
- values()
- items()

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