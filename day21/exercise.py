"""
Convert the following string dates to datetime format:
December 1th, 2015 15:30
5 June 2018 5pm
2020/9/13 00:05:06
"""

import datetime as dt

date_1 = 'December 1th, 2015 15:30'
format_1 = "%B %dth, %Y %H:%M"
# for months that are spelled out, I need to use capital B

date_2 = "5 June 2018 5pm"
format_2 = "%d %B %Y %I%p"

date_3 = "2020/9/13 00:05:06"
format_3 = "%Y/%m/%d %H:%M:%S"

datetime = dt.datetime

datetime_1 = datetime.strptime(date_1,format_1)
print(datetime_1)
# Output: 2015-12-01 15:30:00
datetime_2 = datetime.strptime(date_2,format_2)
print(datetime_2)
# Output: 2018-06-05 17:00:00
datetime_3 = datetime.strptime(date_3,format_3)
print(datetime_3)
# Output: 2020-09-13 00:05:06


"""
Using the operations between dates, find out what is the difference
in days, months and years from January 1, 2000 to today
"""

timedelta = dt.timedelta


# Definiing 2000/01/01
# Definiing now
two_thousand = datetime(2000,1,1)
now = datetime.now()
print(now)

difference = now - two_thousand
days_difference = difference.days
print(f"it's been {days_difference} days since 2000/01/01")
print(f"it's been {days_difference / 30} months since 2000/01/01")
print(f"it's been {days_difference / 365} years since 2000/01/01")
# it's been 7788 days since 2000/01/01
# it's been 259.6 months since 2000/01/01
# it's been 21.336986301369862 years since 2000/01/01


"""
Try some of the differences between datetime and dateutil.
For example:
relativedelta
parser.parse
"""
# I am not going to do this as I feel it is not really an exercise related to the topic

"""
Get all the dates from the Monday of the current month, you can use for
loop and operations between dates
"""

# Has to be in current month
# Has to be a monday

start_of_year = datetime(2021,1,1)
weekday_of_first = start_of_year.weekday()
days_since_start = now - start_of_year
days_since_start = days_since_start.days
# Format
date_format = "%Y-%m-%d"

# Create list to fill with days
months_mondays = []
for i in range(days_since_start+1):
    # Turn i into Timedelta
    # Create days of the year
    diff = timedelta(days=i)
    working_date = (start_of_year + diff)
    # if it is part of current month
    if working_date.month == now.month:
        if working_date.weekday() == 0:
            months_mondays.append(working_date.strftime(date_format))
    
print(months_mondays)
# Output:
# ['2021-04-05', '2021-04-12', '2021-04-19', '2021-04-26']

