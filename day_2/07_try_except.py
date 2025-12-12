import my_console as mc
import datetime as dt

print('Welcome to Exception Handling')

# get the month of year from the user
month = mc.prompt_int("Month?")

# get the day of month from the user
day = mc.prompt_int("Day?")

# get the year from the user
year = mc.prompt_int("Year?")

# create a date object out of these parts
print(f"month: {month}, day: {day}, year: {year}")
d = dt.date(year,month,day)
print(f"date: {d}")

print('Bye')