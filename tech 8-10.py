
#1
import calendar
year=2024
month=10
calendar.month (year,month)
print(calendar.calendar(year))
is_leap=calendar.isleap(year)
print(f"{year} is a leap year: {is_leap}")

"""

#2
import calendar
year=2024
month=10
first_weekday,num_days=calendar.monthrange(year,month)
print(f"First Weekday: {first_weekday}, Number of days: {num_days}")



#3
import calendar
year=2024
month=10
for day in calendar.Calendar().itermonthdays(year,month):
    print(day)


#4
import calendar
text_cal=calendar.TextCalendar(calendar.SUNDAY)
year=2024
month=10
plain_text_cal=text_cal.formatmonth(year,month)
print(plain_text_cal)


#5
from datetime import datetime,timedelta
now=datetime.now()
print(F"Current date and time: {now}")
days_in_past=5
hours_in_past=3
minutes_in_past=30

past_time=now-timedelta(days=days_in_past,hours=hours_in_past,minutes=minutes_in_past)
print(f"Past date and time(5 days,3 hours,30 minutes ago):{past_time}")

#6
import string
sentence="hello world from python"
capitalized_sentence=string.capwords(sentence)
print(capitalized_sentence)

#7
import datetime
cd=datetime.datetime.today()
print(f"Current Day={cd}")

#8
import datetime
c=datetime.date.today()
print(f"Current Day={c}")


#9
import datetime
d=datetime.datetime.now().time()
print("Current time:",d)

#10
import datetime
specific=datetime.date(2024,10,8)
print("SPECIFIC DATE:",specific)

#11
import datetime
time=datetime.time(14,30,45)
print(time)

#12
import datetime
specific_datetime=datetime.datetime(2024,10,8,14,30,45)
print(specific_datetime)

#13
import datetime
s=datetime.datetime.now().time()
print(s)


#14
import datetime
current_datetime=datetime.date.today()
formatted=current_datetime.datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)

#15
import datetime
date_string="2024-09-24 14:30:45"
parsed_data=datetime.datetime.strptime(date_string,"%Y-%m-%d %H:%M:%S")
print(parsed_data)

#16
import datetime
current_datetime=datetime.date.today()
tendays=datetime.timedelta(days=10)
date_10days_ago=current_datetime-tendays
print(date_10days_ago)
"""
