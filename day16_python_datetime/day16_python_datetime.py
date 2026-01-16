from datetime import datetime, date, timedelta, time


# Q1
year = datetime.now().year
day = datetime.now().day
month = datetime.now().month
hour = datetime.now().hour
min = datetime.now().minute
timestamp = datetime.now().timestamp()

print(day, month, hour, min, timestamp)

# Q2
current_date = datetime.now().strftime("%m/%d/%y, %H:%M:%S")
print(current_date)

# Q3
str_time = "5 December, 2019"
time_from_str = datetime.strptime(str_time, "%d %B, %Y")
print(time_from_str)

# Q4
today = date(year=year, month=month, day=day)
next_year = date(year=2027, month=1, day=1)
seventies_date = date(1970, month=1, day=1)
distance_now_new_year = next_year - today
distance_now_seventies = today - seventies_date
print(distance_now_new_year)
print(distance_now_seventies)
