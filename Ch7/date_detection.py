#! /usr/bin/python3

"""
Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single digit, it’ll have a leading zero.
"""

import re
import pyperclip


def date_match():
    """
    - Expression matching DD/MM/YYYY
    - Days range from 01 - 31
    - Months range from 01 - 12
    - Years range from 1000 - 2999
    - If day / month = single digit
        - add a leading zero
        - use .sub()
    """
    date_rex = re.compile(
        r"""
        ((\d\d)\/(\d\d)\/(\d{4}))
        """,
        re.VERBOSE,
    )
    return date_rex


# TODO: is_valid_date()
def is_valid_date(date):
    """
    - if mm = April, June, September, November:
        - DD <= 30 days
    - if mm = February:
        - DD <= 28 days
    - Else:
        - DD <= 31 days
    """


# TODO: is_leap_year()
def is_leap_year(year):
    """
    - Every year evenly divisible by 4 AND NOT evenly divisible by 100 EXCEPT evenly divisible by 400
    """


def clip(text):
    for groups in date_match().findall(text):
        print(groups)
        print(type(groups))


clip(pyperclip.paste())
