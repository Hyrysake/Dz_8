from datetime import date, timedelta, datetime


def get_birthdays_per_week(users_list):
    today = date.today()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    birthdays_per_week = {day: [] for day in weekdays}

    for user in users_list:
        user_birthday = user['birthday'].replace(year=today.year)
        days_until_birthday = (user_birthday - today).days

        if days_until_birthday >= 0:
            if days_until_birthday <= 6:
                day_of_week = weekdays[(today.weekday() + days_until_birthday) % 5]
                if day_of_week == 'Monday':
                    birthdays_per_week[day_of_week].append(user['name'])
                else:
                    birthdays_per_week[day_of_week].append(user['name'])

    users = {day: names for day, names in birthdays_per_week.items() if names}
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")