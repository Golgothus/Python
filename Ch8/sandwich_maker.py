#! /usr/bin/python

"""
Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:

Using inputMenu() for a bread type: wheat, white, or sourdough.

Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.

Using inputYesNo() to ask if they want cheese.
If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.

Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.

Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.

Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.
"""

import pyinputplus as pyip
import random

cost = 0
total = 0


def sandwich():
    """
    Method provides a list of items, choices the user can use to create their sandwich
    """
    bread = pyip.inputMenu(["wheat", "white", "sourdough"], numbered=True)
    protein = pyip.inputMenu(
        ["Ham", "Turkey", "Salami", "Bacon", "Prosciutto", "Vegetarian"]
    )
    if protein == "Vegetarian":
        veggies = pyip.inputMenu(
            ["Tofu", "Lettuce", "Tomato", "Peppers", "Olives", "Cucumber Slices", numbered=True]
        )
    else:
        veggies = None
    cheese = pyip.inputYesNo("Would you like cheese? ")
    if cheese == "yes":
        cheese_type = pyip.inputMenu(
            ["American", "Cheddar", "Pepperjack", "Smoked Gouda", "Provologne", numbered=True]
        )
    else:
        cheese_type = None
    condiments = pyip.inputYesNo("Would you like condiments? ")
    if condiments == "yes":
        condiments_choice = pyip.inputMenu(
            [
                "Ketchup",
                "Mustard",
                "Oil and Vinegar",
                "Spices and Oregano",
                "Caesar Dressing",
                "Ranch Dressing",
            ], numbered=True
        )
    else:
        condiments_choice = None

    completed_order = {
        "Bread": bread,
        "Protein": protein,
        "Veggies": veggies,
        "Cheese": cheese_type,
        "Condiments": condiments_choice,
    }

    cost = random.randint(1, 100)

    if cost < 25:
        cost = 6
    if cost >= 25 and cost < 50:
        cost = 9
    else:
        cost = 13

    return completed_order, cost


amount_of_sandwiches = pyip.inputInt(
    "How many sandwiches would you like to order? [1 - 9999] ", min=1, max=9999
)

for amount in range(amount_of_sandwiches):
    completed_sandwich, cost = sandwich()
    total += cost
    print("Your order consists of the following:")
    print(completed_sandwich)
    print(f"For a total cost of: ${total}")
