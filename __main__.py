import re

from datetime import datetime


date_1 = datetime(year=1990, month=11, day=24)

users = [
    {'name': 'Bernard', 'birthday': '1992-06-14'},
    {'name': 'Linda', 'birthday': '1995/06/18'},
    {'name': 'Mark', 'birthday': '1992_03_12'},
    {'name': 'Ben', 'birthday': date_1},
    {'name': 'Britani', 'birthday': datetime(year=1997, month=12, day=29).date()},
    {'name': 'John', 'birthday': datetime(year=1996, month=1, day=12).date()},
    {'name': 'Sydney', 'birthday': datetime(year=1995, month=3, day=6).date()},
    {'name': 'Stefany', 'birthday': datetime(year=1993, month=3, day=3).date()},
    {'name': 'Brit', 'birthday': datetime(year=1992, month=9, day=21).date()},
]


# week_days = {
#     0: 'Monday',
#     1: 'Tuesday',
#     2: 'Wednesday',
#     3: 'Thurthday',
#     4: 'Friday',
#     5: 'Saturday',
#     6: 'Sunday',
# }


# function returns week day number and day name
# def get_day_of_week(birth_date):
    
#     week_days = {
#     0: 'Monday',
#     1: 'Tuesday',
#     2: 'Wednesday',
#     3: 'Thurthday',
#     4: 'Friday',
#     5: 'Saturday',
#     6: 'Sunday',
# }
#     date_list = [match.group() for match in re.finditer(r'[1-9]\d*', birth_date)]
#     parsed_date = datetime(year=int(date_list[0]), month=int(date_list[1]), day=int(date_list[2]))
#     day_number = parsed_date.weekday()
#     day_name = week_days.get(day_number)
#     return day_number, day_name


# function returns week day number
def get_day_of_week(birth_date):
    date_list = [match.group() for match in re.finditer(r'[1-9]\d*', birth_date)]
    parsed_date = datetime(year=int(date_list[0]), month=int(date_list[1]), day=int(date_list[2]))
    day_number = parsed_date.weekday()
    return day_number

print(get_day_of_week('2023/05/25'))