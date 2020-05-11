class Day(object):
    dows = {
        1: {"name": "Sunday", "ord": 1},
        2: {"name": "Monday", "ord": 2},
        3: {"name": "Tuesday", "ord": 3},
        4: {"name": "Wednesday", "ord": 4},
        5: {"name": "Thursday", "ord": 5},
        6: {"name": "Friday", "ord": 6},
        7: {"name": "Saturday", "ord": 7}
    }

    def months(self, year):
        leap_day = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        return {
            1: {"name": "January", "ord": 1, "days": 31},
            2: {"name": "February", "ord": 2, "days": 29 if leap_day else 28},
            3: {"name": "March", "ord": 3, "days": 31},
            4: {"name": "April", "ord": 4, "days": 30},
            5: {"name": "May", "ord": 5, "days": 31},
            6: {"name": "June", "ord": 6, "days": 30},
            7: {"name": "July", "ord": 7, "days": 31},
            8: {"name": "August", "ord": 8, "days": 31},
            9: {"name": "September", "ord": 9, "days": 30},
            10: {"name": "October", "ord": 10, "days": 31},
            11: {"name": "November", "ord": 11, "days": 30},
            12: {"name": "December", "ord": 12, "days": 31}
        }

    def __init__(self, year, month, day, dow):
        self.year = year
        months = self.months(year)
        self.month = months.get(month)
        self.day = day
        self.dow = self.dows[dow]

    def next(self):
        maybe_day = (self.day + 1) % (self.month["days"] + 1)
        if maybe_day == 0:
            day = 1
            maybe_month = (self.month.get("ord") + 1) % (len(
                self.months(self.year)) + 1)
        else:
            day = maybe_day
            maybe_month = self.month.get("ord")
        if maybe_month == 0:
            year = self.year + 1
            month = self.months(year).get(1)
        else:
            year = self.year
            month = self.months(year).get(maybe_month)
        maybe_dow_ord = (self.dow["ord"] + 1) % (len(self.dows) + 1)
        dow_ord = 1 if maybe_dow_ord == 0 else maybe_dow_ord

        return Day(year, month.get("ord"), day, dow_ord)


def build_calender():
    cal = [Day(1900, 1, 1, 2)]
    end = Day(2001, 1, 1, 2)
    while cal[-1].year != 2001:
        cal.append(cal[-1].next())
        print(cal[-1].year)
    return cal


def filter_sundays_first(cal):
    return [d for d in cal if d.year > 1900 and d.year < 2001 and d.day == 1 and d.dow['ord'] == 1]
