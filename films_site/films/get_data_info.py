from datetime import datetime


def get_four_days():
    first_day = datetime.today().day
    four_days = [first_day, first_day+1, first_day+2, first_day+3]
    weekdays = {0: 'пн', 1: 'вт', 2: 'ср', 3: 'чт', 4: 'пт', 5: 'сб', 6: 'вс'}
    w_day = datetime.today().weekday()
    four_weekdays = [weekdays[w_day], weekdays[w_day+1], weekdays[w_day+2], weekdays[w_day+3]]
    info = [four_days, four_weekdays]
    return info
# TODO: если не работает, то возможно все дело в днях неделях

# def get_weekdays():

    # return four_weekdays
