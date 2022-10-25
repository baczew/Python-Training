import calendar
from datetime import date

# Print simple calendar for current month
calendar_object = calendar.TextCalendar(calendar.MONDAY)
calendar_formatted = calendar_object.formatmonth(date.today().year, date.today().month, 1, 1)
print(calendar_formatted)

# Get HTML calendar
calendar1 = calendar.HTMLCalendar(calendar.MONDAY)
html_calendar = calendar1.formatmonth(date.today().year, date.today().month)
print(html_calendar)

# Print all day names
for i in calendar.day_name:
    print(i)

# Print all month names
for i in calendar.month_name:
    print(i)

# Print all the first friday of month in 2022
print("First friday of the month is on:")
for month in range(1, 13):
    calendar_month = calendar.monthcalendar(2022, month)
    week_one, week_two = calendar_month[0], calendar_month[1]
    if week_one[calendar.FRIDAY] != 0:
        meetday = week_one[calendar.FRIDAY]
    else:
        meetday = week_two[calendar.FRIDAY]
    print(f"{calendar.month_name[month]}, {meetday}")

# Print all Fridays the 13th in the next 5 years
print("Friday the 13th going to happen on:" )
for year_add in range(1, 6):
    for month in range(1, 13):
        month_calendar = calendar.monthcalendar(date.today().year + year_add + 1, month)
        for week in range(0, 4):
            if month_calendar[week][4]==13:
                print(date(year = date.today().year + year_add + 1, month = month, day = month_calendar[week][4]).strftime("%dth of %B %Y"))
                break




