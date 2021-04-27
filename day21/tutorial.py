"""
Day 21: Datetime

Datetime is the library of python used to manipulate date and time
dateime comes with python, so no need to install a package

What I've misunderstood is that datime works with Datetime OBJECTS, not strings

there are 4 main objects that we use to handle dates:
- date
- time
- datetime
- timedelta

datetime above is an object within datetime: (datetime)
"""
import datetime

datetime.time
datetime.date
datetime.datetime
datetime.timedelta

# Date:
# date class object lets us work with dates(year,month,day)

date = datetime.date

birthday = datetime.date(1993,5,14)

print(birthday)
# Output:
# 1993-05-14
# this is not a string
print(type(birthday))
# Output:
# <class 'datetime.date'>


# Today:
# The date object has a method that lets us get today's date in date format
today = date.today()
print(today)
# Output:
# 2021-04-27

# Time:
# the time class allows us to create time objects with given data, the way to give it data is: Hour:Minute:Seconds
time = datetime.time

four_20 = time(16, 20, 00)
print(four_20)
# Output:
# 16:20:00

# by default it turns to 00:00:00
print(time())
# Output: 00:00:00

# Datetime
# datetime is the combination of date and time, with 6 variables: datetime(year, month, day, hour, minute, second)
# just like with time(), the last 3 inputs are not mandatory

datetimes = datetime.datetime

random_date = datetimes(2014,8,14,23,42,6)
print(random_date)
# Output:
# 2014-08-14 23:42:06

# Now
# just like with time() you can get a datetime object with the current datetime

now = datetimes.now()
print(now)
# Output:
# 2021-04-27 18:55:11.259068

# Attributes:
# all these object have attributes we can get from them

print(now.day)
# Output: 27
print(now.second)
# Output: 3

# Methods:
# there are multiple methods we can take advantage of:

# weekday:
# weekday ranges from 0 for monday to 6 for sunday
weekday = today.weekday()
print(weekday)
# Output: 1(tuesday)
# isoweekday() returns weekdays 1-7

# strftime:
# strftime returns time AS A STRING

strftime = now.strftime("%b %dth, %Y %H:%M")
print(strftime)
# Output:
# Apr 27th, 2021 19:06
# I have no idea what the %b %dth, %Y %H:%M mneans, will have to look that up
"""
I found info on it:

%b: Month as locale’s abbreviated name. (Aug)
%d: Day of the month as a zero-padded decimal number. (05)
%Y: Year with century as a decimal number. (2020)
%H: Hour (24-hour clock) as a zero-padded decimal number. (17)
%M: Minute as a zero-padded decimal number. (59)
"""

# Timedelta:
# Timedelta lets us compare two dates with dunder methods contained in (datetime)
# we can also define time/date as variables and use them in equations
timedelta = datetime.timedelta

# Creating 3 days as a variable
three_days = timedelta(days=3)
print(three_days)
# Output: 3 days, 0:00:00

# Now we can use this in equations through magical methods
three_days_past = now - three_days
print(three_days_past)
# Output:
# 2021-04-25 00:51:45.964609

# We can also do equations between 2 datetime objects

birthday = datetimes(1999,9,19)
since_birth = now - birthday
print(f"it's been {since_birth.days} days since your birth")
# Output: it's been 7892 days since your birth


# Strptime:
# strptime is the module used to convert strings into Datetime objects, using the encoding used above

str_date = '2021-05-13 16:20'
format = '%Y-%m-%d %H:%M'
obj_date = datetimes.strptime(str_date,format)

print(obj_date)