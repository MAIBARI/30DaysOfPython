from datetime import datetime, timedelta

# 1. Get the current day, month, year, hour, minute, and timestamp
now = datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
current_timestamp = now.timestamp()

print("Current Day:", current_day)
print("Current Month:", current_month)
print("Current Year:", current_year)
print("Current Hour:", current_hour)
print("Current Minute:", current_minute)
print("Current Timestamp:", current_timestamp)

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S"
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted Date:", formatted_date)

# 3. Today is 5 December, 2019. Change this time string to time.
time_string = "5 December, 2019"
parsed_time = datetime.strptime(time_string, "%d %B, %Y")
print("Parsed Time:", parsed_time)

# 4. Calculate the time difference between now and New Year
new_year = datetime(current_year + 1, 1, 1)
time_until_new_year = new_year - now
print("Time Until New Year:", time_until_new_year)

# 5. Calculate the time difference between 1 January 1970 and now
epoch_start = datetime(1970, 1, 1)
time_since_epoch = now - epoch_start
print("Time Since 1 January 1970:", time_since_epoch)

# 6. Example uses of the datetime module:
examples = [
    "Time series analysis",
    "To get a timestamp of any activities in an application",
    "Adding posts on a blog",
    "Scheduling and tracking events",
    "Working with timezone-aware data",
]
print("Examples of datetime usage:")
for example in examples:
    print("-", example)
