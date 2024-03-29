#! /usr/bin/python
"""
picnicTable.py
"""


def print_picnic(items_dict, left_width, right_width):
    """
    Function which takes a dictionary and then justifies items
    based on certain criteria
    """
    print("PICNIC ITEMS".center(left_width + right_width, "-"))
    for k, v in items_dict.items():
        print(k.ljust(left_width, ".") + str(v).rjust(right_width))


picnicItems = {"sandwiches": 4, "apples": 12, "cups": 4, "cookies": 8000}
print_picnic(picnicItems, 12, 5)
print_picnic(picnicItems, 20, 6)
