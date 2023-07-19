#! /usr/bin/python

import calendar
import time

currentTime = time.gmtime()
currentMonth = time.strftime("%m",currentTime)

for m in range(int(currentMonth),13,1):
    print(calendar.month(2023,m))