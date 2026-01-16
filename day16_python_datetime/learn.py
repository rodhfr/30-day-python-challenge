from datetime import datetime, date, timedelta

# dir or help commands to know available functions
# print(dir(datetime))

# focus on date, datetime, time and time delta
now = datetime.now()
print(now)

day = now.day
print(day)

yr = now.year
print(yr)

hr = now.hour
print(hr)

min = now.minute
print(min)

sec = now.second
print(sec)

timestamp = now.timestamp()
print(timestamp)

print(day, yr, hr, min)
print("timestamp", timestamp)

t = now.strftime("%H:%M:%S")
print(t)

date_string = "5 december, 2019"
print("date_string =", date_string)
date_obj = datetime.strptime(date_string, "%d %B, %Y")
print("date_obj =", date_obj)

today = date(
    year=2026,
    month=1,
    day=1,
)
new_year = date(year=2027, month=1, day=1)
time_left_for_newyr = new_year - today
print(time_left_for_newyr)

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(weeks=7, days=5, hours=3, seconds=30)
t3 = t1 - t2
print(t3)
