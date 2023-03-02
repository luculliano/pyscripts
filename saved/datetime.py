# 1
def get_date_range(start, end):
    return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]

date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')


# 2 amount of sundays in a year
from datetime import date, datetime, timedelta


def num_of_sundays(year):
    current_date = date(year, 1, 1)
    # first sunday
    current_date += timedelta(days=6 - current_date.weekday())
    total = 0
    while current_date.year == year:
        current_date += timedelta(days=7)
        total += 1

    return total


print(num_of_sundays(2050))
