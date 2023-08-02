#! /usr/bin/python

"""
Exercises from Automate the Boring Stuff 2nd Edition, Chapter 6

Covers additional practice / context around isx() string methods
"""

while True:
    print("Enter your age")
    age = input()
    if age.isdecimal():
        break
    print("Please enter a number for your age.")

while True:
    print("Select a new password (letters and numbers only).")
    password = input()
    if password.isalnum():
        break
    print("Passwords can only have letters and numbers.")
