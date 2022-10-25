from datetime import datetime
from datetime import timedelta
from datetime import date

# Get current date and time
current_time = datetime.now()
print(f'Current date & time: {current_time}')

# Create a custom string out of any datetime object
text = current_time.strftime("Year %Y, already %d day(s) of %B are gone!")
print(text)

# Get date components
print(f"Day: {current_time.day}")
print(f"Month: {current_time.month}")
print(f"Year: {current_time.year}")
print(f"Day of the week: {current_time.weekday()}, 0-Sunday, 1 - Monday, ...")
print(f"Hour: {current_time.hour}")
print(f"Minute: {current_time.minute}")

# Adding time period to a date
print("You have got exactly 13 days, 2 hours and 15 seconds to pay my money back!")
initial_date = datetime.today()
time_given = timedelta(days=13, hours=2, minutes=0, seconds=15)
print(f"You better have my money until: {initial_date + time_given}")

# Subtract time period
date_time_135_hours_earlier = datetime.today() - timedelta(hours=135)
print(f"135 hours before was {date_time_135_hours_earlier.strftime('%d - %B - %Y')}")

# Time till next Prima Aprilis
now = datetime.now()

prima_aprilis = date(now.year, 4, 1)

if prima_aprilis < now.date():
    print("Prima aprilis is gone! You are late! %d days have gone since that time!" %(now.date() - prima_aprilis).days)
    prima_aprilis = date((now.today()).year + 1, 4, 1)
    print("But next one is in: %d days!" %(prima_aprilis - now.date()).days)
else:
    print("Prima Aprilis is in: %d days!" %(prima_aprilis-date.today()).days)
