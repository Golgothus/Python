#! /usr/bin/python

"""
Use the pyinputplus module
Loop through unexpected and incorrect user input
Ask the user if they'd like to close the program
"""

import pyinputplus as pyip

while True:
    prompt = "Would you like to close the program? Type yes: "
    response = pyip.inputYesNo(prompt)
    if response == "yes":
        print("Closing the program.")
        break
    else:
        print("We go again!")
