import datetime


class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def Display_time(self):
        return self.hour + ":" + self.minute + ":" + self.second


current_time = datetime.datetime.now()
formatted_current_time = current_time.strftime("%H:%M:%S")
splitted_time = formatted_current_time.split(":")


current_hour = splitted_time[0]
current_minute = splitted_time[1]
current_secound = splitted_time[2]

Clock = Time(current_hour, current_minute, current_secound)

print(Clock.Display_time())
