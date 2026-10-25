from datetime import datetime

import pytz


class Time:
    def __init__(self, hour, minute, second):
        self.hour = int(hour)
        self.minute = int(minute)
        self.second = int(second)
        self.fix()

    def display(self):
        return f"{self.hour}:{self.minute}:{self.second}"

    def to_seconds(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    @classmethod
    def from_seconds(cls, seconds):
        hour = seconds // 3600
        minute = (seconds % 3600) // 60
        second = seconds % 60
        return cls(hour, minute, second)

    def sum(self, second_time):
        h_result = self.hour + second_time.hour
        m_result = self.minute + second_time.minute
        s_result = self.second + second_time.second
        result = Time(h_result, m_result, s_result)
        return result

    def sub(self, second_time):
        h_result = self.hour - second_time.hour
        m_result = self.minute - second_time.minute
        s_result = self.second - second_time.second
        result = Time(h_result, m_result, s_result)
        return result

    def change_local_time(self):
        current_time = datetime.now()
        second_timezone = pytz.timezone("America/New_York")
        second_time = current_time.astimezone(second_timezone).time()
        second_time = second_time.strftime("%H:%M:%S")
        return second_time

    def fix(self):
        if self.second >= 60:
            self.second -= 60
            self.minute += 1

        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        if self.second < 0:
            self.second += 60
            self.minute -= 1

        if self.minute < 0:
            self.minute += 60
            self.hour -= 1


h = "10"
m = "30"
s = "45"

time_1 = Time(h, m, s)
print("The Current Time is:", time_1.display())

second_time = time_1.change_local_time()
print("Current time in New York is:", second_time)

total_seconds = time_1.to_seconds()
print("Convert Current time to seconds:", total_seconds)

print("-" * 50)

first_time = input("Enter first time with this format hh:mm:ss: ")
second_time = input("Enter second time with this format hh:mm:ss: ")

first_time = first_time.split(":")
second_time = second_time.split(":")

first_h = first_time[0]
first_m = first_time[1]
first_s = first_time[2]
first_time = Time(first_h, first_m, first_s)

second_h = second_time[0]
second_m = second_time[1]
second_s = second_time[2]
second_time = Time(second_h, second_m, second_s)

sum_result_time = first_time.sum(second_time)

if second_h > first_h:
    sub_result_time = second_time.sub(first_time)
else:
    sub_result_time = first_time.sub(second_time)

print(f"First time: {first_time.display()}")
print(f"Second time: {second_time.display()}")
print(f"Sum result time: {sum_result_time.display()}")
print(f"Sub result time: {sub_result_time.display()}")
