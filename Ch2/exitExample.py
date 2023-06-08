#! /usr/bin/python

import sys

print("What is your name?")
name = input()

while True:
    print(f"Hello {name}. If you would like to exit, please type 'exit'.")
    answer = input()

    if(answer == 'exit'):
        print("Exiting application.")
        sys.exit()
    else:
        print(f"You responded with {answer}.")
        print("You have not decided to exit. Continuing operations.")