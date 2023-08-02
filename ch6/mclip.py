#! /usr/bin/python
"""
                 _ _                    
                | (_)                   
  _ __ ___   ___| |_ _ __   _ __  _   _ 
 | '_ ` _ \ / __| | | '_ \ | '_ \| | | |
 | | | | | | (__| | | |_) || |_) | |_| |
 |_| |_| |_|\___|_|_| .__(_) .__/ \__, |
                    | |    | |     __/ |
                    |_|    |_|    |___/ 

A multi-clipboard program
"""

import sys
import pyperclip

TEXT = {
    "agree": """Yes, I agree. That sounds fine to me.""",
    "busy": """Sorry, I'm unavailable at this time, I'll get back to you ASAP.""",
    "dnd": """Online focus time.""",
    "offline": """I am offline at this time.""",
}

if len(sys.argv) < 2:
    print("Usage: python mclip.py [keyphrase] - copy phrase text")
    sys.exit()

KEYPHRASE = sys.argv[1]  # first command line arg is the keyphrase

if KEYPHRASE in TEXT:
    pyperclip.copy(TEXT[KEYPHRASE])
    print(f"Text for {KEYPHRASE} copied to clipboard.")
else:
    print(f"There is no text for {KEYPHRASE}")
