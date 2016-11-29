from datetime import datetime, timedelta


class TimeParser:

    def __init__(self, date):
        self.date = date
        self.hours = datetime.strptime(self.date, '%H:%M:%S').hour
        self.minutes = datetime.strptime(self.date, '%H:%M:%S').minute
        self.seconds = datetime.strptime(self.date, '%H:%M:%S').second

    def get_hours(self):
        return datetime.strptime(self.date, '%H:%M:%S').hour

    def get_minutes(self):
        return datetime.strptime(self.date, '%H:%M:%S').minute + \
            60 * self.get_hours()

    def get_seconds(self):
        return datetime.strptime(self.date, '%H:%M:%S').second + \
            60 * self.get_minutes() + 3600 * self.get_hours()

    def __add__(self, other):
        self_time = datetime.strptime(self.date, '%H:%M:%S')
        other_time = datetime.strptime(other.date, '%H:%M:%S')

        res = self_time + timedelta(hours=other_time.hour,
                                    minutes=other_time.minute,
                                    seconds=other_time.second)

        return res.strftime('%H:%M:%S')

# date = TimeParser('1:56:56')
# date1 = TimeParser('2:57:56')
# print(date.get_hours())
# print(date.get_minutes())
# print(date.get_seconds())
# print(date + date1)
