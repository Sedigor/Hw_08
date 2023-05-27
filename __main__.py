import re
import random


from datetime import datetime, timedelta
from collections import defaultdict


users_names = [
    'Ethan Reynolds',
    'Caleb Anderson',
    'Benjamin Martinez',
    'Daniel Thompson',
    'Nathan Carter',
    'Matthew Rodriguez',
    'Oliver Foster',
    'William Jenkins',
    'Samuel Butler',
    'Alexander Collins',
    'Sophia Campbell',
    'Olivia Parker',
    'Ava Gonzalez',
    'Isabella Wright',
    'Mia Phillips',
    'Charlotte Turner',
    'Amelia Morgan',
    'Harper Mitchell',
    'Evelyn Nelson',
    'Abigail Rivera',
]


# Make user list with random birthday date

def make_birthday_date(user_names: list):
    users = []
    for i in range(len(user_names)):
        year = random.randint(1990, 2005)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        name = user_names[i]
        birthday = datetime(year=year, month=month, day=day)
        users.append({'name': name, 'birthday': birthday})
    return users


# assign result of 'make_birthday_date' func list to var 'users'

users = make_birthday_date(users_names)
        

# function returns week day number and day name. function can receive an datetime object or string date in format (yyyy(any symbol)m(0m)(any symbol)d(0d))

def get_day_of_week(birth_date):
    
    week_days = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thurthday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
    }
    
    if isinstance(birth_date, str):
        date_list = [match.group() for match in re.finditer(r'[1-9]\d*', birth_date)]
        parsed_date = datetime(year=int(date_list[0]), month=int(date_list[1]), day=int(date_list[2]))
    else:
        parsed_date = birth_date
    day_number = parsed_date.weekday()
    day_name = week_days.get(day_number)
    return day_number, day_name


# sometime there is no result, because user's birthdays generate randomly

def birthday_per_week(users):
    current_date = datetime.now() + timedelta(days=1)
    while current_date.weekday(): 
        current_date += timedelta(days=1)
    birthday_dict = defaultdict(list)
    monday = current_date.date()
    previous_saturday = monday - timedelta(days=2)
    friday = (current_date + timedelta(days=4)).date()
    for user in users:
        user_birthday = user['birthday'].replace(year=current_date.year).date()
        if previous_saturday <= user_birthday <= friday:
            if previous_saturday <= user_birthday <= monday:
                birthday_dict[monday].append(user['name'])
            elif user_birthday <= friday:
                birthday_dict[user_birthday].append(user['name'])
    for birthday in birthday_dict:
        week_day = get_day_of_week(birthday)[1]
        birthday_users = ', '.join(birthday_dict[birthday])
        print(f"{week_day}: {birthday_users}")
        
        
birthday_per_week(users)