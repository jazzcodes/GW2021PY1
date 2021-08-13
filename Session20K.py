# import datetime
import datetime as dt
today = dt.datetime.today()
print("Today:", today, type(today))

today = str(today)
print("Today Now:", today, type(today))

today = today.split()
print(today[0])
print(today[1])

today = dt.datetime.today()
tomorrow = dt.datetime(2021, 8, 14, 13, 0, 0)
print(today)
print(tomorrow)

print(tomorrow-today)

# Assignment: Explore how to format date :)