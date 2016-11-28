import datetime


class TimeParser:

    def __init__(self, date):
        self.date = date
        self.hours = datetime.datetime.strptime(self.date, '%H:%M:%S').hour
        self.minutes = datetime.datetime.strptime(self.date, '%H:%M:%S').minute
        self.seconds = datetime.datetime.strptime(self.date, '%H:%M:%S').second

    def get_hours(self):
        return datetime.datetime.strptime(self.date, '%H:%M:%S').hour

    def get_minutes(self):
        return datetime.datetime.strptime(self.date, '%H:%M:%S').minute + \
            60 * self.get_hours()

    def get_seconds(self):
        return datetime.datetime.strptime(self.date, '%H:%M:%S').second + \
            60 * self.get_minutes() + 3600 * self.get_hours()

    def __add__(self, other):
        a = datetime.timedelta(hours=self.hours,
                               minutes=self.minutes,
                               seconds=self.seconds)
        b = datetime.timedelta(hours=other.hours,
                               minutes=other.minutes,
                               seconds=other.seconds)
        return str(a + b)


date = TimeParser('1:56:56')
date1 = TimeParser('2:57:56')
print(date.get_hours())
print(date.get_minutes())
print(date.get_seconds())
print(date + date1)
