from datetime import datetime, timedelta


class TimeParser:

    def __init__(self, date):
        self.date = date
        self.orig_date = date
        self.hours = datetime.strptime(TimeParser.parse_date(self.date),
                                       '%H:%M:%S').hour
        self.minutes = datetime.strptime(TimeParser.parse_date(self.date),
                                         '%H:%M:%S').minute
        self.seconds = datetime.strptime(TimeParser.parse_date(self.date),
                                         '%H:%M:%S').second

    @staticmethod
    def parse_date(date_string):
        if len(date_string.split(':')) < 3:
            date_string = date_string.split(':')
            date_string.insert(0, '0')
            return ':'.join(date_string)
        return date_string

    def __str__(self):
        return self.orig_date

    def __repr__(self):
        return self.__str__()

    def get_hours(self):
        return datetime.strptime(TimeParser.parse_date(self.date),
                                 '%H:%M:%S').hour

    def get_minutes(self):
        return datetime.strptime(TimeParser.parse_date(self.date),
                                 '%H:%M:%S').minute + \
            60 * self.get_hours()

    def get_seconds(self):
        return datetime.strptime(TimeParser.parse_date(self.date),
                                 '%H:%M:%S').second + \
            60 * self.get_minutes() + 3600 * self.get_hours()

    def __add__(self, other):
        self_time = datetime.strptime(TimeParser.parse_date(self.date),
                                      '%H:%M:%S')
        other_time = datetime.strptime(TimeParser.parse_date(other.date),
                                       '%H:%M:%S')

        res = self_time + timedelta(hours=other_time.hour,
                                    minutes=other_time.minute,
                                    seconds=other_time.second)

        return res.strftime('%H:%M:%S')


# date = TimeParser('56:56')
# date1 = TimeParser('2:57:56')
# print(date.get_hours())
# print(date.get_minutes())
# print(date.get_seconds())
# print(date + date1)
# print(TimeParser.parse_date('3:44'))
# print(TimeParser.parse_date(date.date))
# print(date.orig_date)
