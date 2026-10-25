from datetime import datetime as datetimelib


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def display_date(self):
        return f"{self.year}-{self.month}-{+self.day}"


current_date = datetimelib.now()
myday = Date(current_date.year, current_date.month, current_date.day)

print("current Date: ", myday.display_date())
