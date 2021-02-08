import calendar


def meetup(year, month, week, day_of_week):
    week_days = list(calendar.day_name)
    c = calendar.Calendar()

    days = [d for d in c.itermonthdates(year, month) if
            d.weekday() == week_days.index(day_of_week) and d.month == month]

    if week == 'teenth':
        result = [d for d in days if 13 <= d.day <= 19][0]
    elif week == 'last':
        result = days[-1]
    else:
        try:
            result = days[int(week[0]) - 1]
        except IndexError:
            raise MeetupDayException("Incorrect meetup instructions")

    return result


class MeetupDayException(Exception):
    def __init__(self, *args):
        super().__init__(args)
