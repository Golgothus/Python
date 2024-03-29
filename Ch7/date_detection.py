#! /usr/bin/python3

"""
Write a regular expression that can detect dates in the DD/MM/YYYY format. 
Assume that the days range from 01 to 31, the months range from 01 to 12.
The years range from 1000 to 2999. 
Note that if the day or month is a single digit, it’ll have a leading zero.
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
        ((\d\d|\d)\/(\d\d|\d)\/(\d{4}))
#        |
#        ((\d\d)\-(\d\d)\-(\d{4})))
        """,
        re.VERBOSE,
    )
    return date_rex


def is_valid_date(date):
    """
    - if mm = April, June, September, November:
        - DD <= 30 days
    - if mm = February:
        - DD <= 28 days
    - Else:
        - DD <= 31 days

    format is dd/mm/yyyy
    date tuple:
    0 - full date
    1 - dd
    2 - mm
    3 - yyyy
    """

    months = {
        "01": "31",
        "02": "28",
        "03": "31",
        "04": "30",
        "05": "31",
        "06": "30",
        "07": "31",
        "08": "31",
        "09": "30",
        "10": "31",
        "11": "30",
        "12": "31",
    }

    full_date, dd, mm, yyyy = date

    # date_match().sub(r"(\d)\/(\d)\/(\d{4})", date)

    if len(dd) == 1:
        dd = "0" + dd
    if len(mm) == 1:
        mm = "0" + mm

    if is_leap_year(yyyy) is True:
        leap_year_date = {"02": "29"}
        months.update(leap_year_date)

    full_date = dd + "/" + mm + "/" + yyyy

    if mm in months.keys():
        if dd <= months[mm]:
            return full_date
        else:
            return "Not a valid date."


def is_leap_year(year):
    """
    - Every year evenly divisible by 4 AND NOT evenly divisible by 100
    - EXCEPT evenly divisible by 400
    """

    if int(year) % 4 == 0 and not int(year) % 100 == 0 or int(year) % 400 == 0:
        return True
    else:
        return False


def clip(text):
    """
    Pull clipboard text, and perform the following:
    - Check for pattern matching
    - Check for valid date criteria
    """

    for groups in date_match().findall(text):
        print(is_valid_date(groups))


dates = [
    "40/01/1993",
    "01/01/1993",
    "01/12/1976",
    "22/06/2017",
    "04/09/1999",
    "22/08/1985",
    "28/12/2008",
    "01/01/2024",
    "29/02/2024",
    "29/02/2023",
    "29/02/2000",
    "29/02/1993",
    "29/02/2020",
    "29/02/2018",
    "29/02/2100",
    "01-01-1993",
    "1/1/1993",
]

clip(str(dates))
clip(pyperclip.paste())
