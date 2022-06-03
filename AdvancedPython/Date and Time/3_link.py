#What's inside datetime?
import datetime

print(dir(datetime))

#datetime.date Class
'''
You can instantiate date objects from the date class.
A date object represents a date (year, month and day).
'''

import datetime

d = datetime.date(2019, 4, 13)
print(d)

#Get current date

from datetime import date

today = date.today()

print("Current date =", today)


################https://www.programiz.com/python-programming/datetime######

###https://www.programiz.com/python-programming/time/sleep
