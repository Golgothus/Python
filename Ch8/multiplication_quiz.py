#! /usr/bin/python

"""
Import pyinputplus
Use the following methods:
 - allowRegexes
 - blockRegexes
 - timeout
 - limit
"""

import pyinputplus as pyip
import random, time

number_of_questions = 10
correct = 0

for q in range(number_of_questions):
    # create numbers to multiply

    x = random.randint(0, 12)
    y = random.randint(0, 12)

    prompt = f"Question # {q}: {x} * {y} = "

    try:
        # Right answers are handled by allowRegexes
        # Wrong answers are handled by blockRegexes
        pyip.inputStr(
            prompt,
            allowRegexes=[f"^{x*y}$"],
            blockRegexes=[(".*", "Incorrect.")],
            timeout=8,
            limit=3,
        )
    except pyip.TimeoutException:
        print("Sorry, you are out of time. Next question...")
    except pyip.RetryLimitException:
        print("No more attempts. Moving on...")
    else:
        # Runs if no exceptions are caught
        print("Answer is correct. Moving on...")
        correct += 1

    time.sleep(3)  # pausing to show answer

print(f"Score is {correct} / {number_of_questions}.")
