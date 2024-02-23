from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    today = datetime.today().date()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    birthdays = defaultdict(list)
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження цього року вже пройшов, дивимося на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days
        
        # Перевірка, чи день народження відбудеться наступного тижня
        if 0 <= delta_days <= 7:
            day_of_week = weekdays[birthday_this_year.weekday()]
            # Якщо день народження припадає на вихідний, привітання переносяться на понеділок
            if day_of_week in ['Saturday', 'Sunday']:
                day_of_week = 'Monday'
            birthdays[day_of_week].append(name)

    # Виведення результату
    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")

# Приклад використання
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 29)},
    {"name": "Kim Kardashian", "birthday": datetime(1948, 3, 1)},
    {"name": "Jill Valentine", "birthday": datetime(1976, 3, 8)}
]

get_birthdays_per_week(users)