import datetime

currentDateTimeString = datetime.datetime.today().strftime('%Y%m%d%H%M%S%f')[:-3]
print(currentDateTimeString)
year = currentDateTimeString[:4]
month = currentDateTimeString[4:6]
day = currentDateTimeString[6:8]
hour = currentDateTimeString[8:10]
minute = currentDateTimeString[10:12]
second = currentDateTimeString[12:14]

print(year, month, day, hour, minute, second)