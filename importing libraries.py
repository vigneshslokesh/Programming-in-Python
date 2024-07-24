#import - directly brings library into the python program

# importing libraries
# structure - import (library name)
# calling function - (libname).function()

# import math # math libraries - log(), pow(), cos(), sin(), factorial
# import random
# # random - randint, random, randrange

import calendar #importing calendar

print(calendar.month(2024, 7)) # specific month
print(calendar.calendar(2024)) # specific year

# <--------->
from calendar import month, calendar # get only the necessary content
# # to bring entire content everything in the calendar library into this python program

print(month(2024, 11))
print(calendar(2024))

# <--------->
# moving the entire library into a variable

import calendar as c
print(c.month(2024, 11))

from calendar import month as m
print(m(2024, 11))

