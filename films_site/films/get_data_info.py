from datetime import datetime


def get_four_days():
    first_day = datetime.today().day
    four_days = [first_day, (first_day+1) % 31, (first_day+2) % 31, (first_day+3) % 31]
    weekdays = {0: 'пн', 1: 'вт', 2: 'ср', 3: 'чт', 4: 'пт', 5: 'сб', 6: 'вс'}
    w_day = datetime.today().weekday()
    four_weekdays = [weekdays[w_day], weekdays[(w_day+1) % 7], weekdays[(w_day+2) % 7], weekdays[(w_day+3) % 7]]
    info = {}
    for item in range(4):
        info[four_days[item]] = four_weekdays[item]
    return info
