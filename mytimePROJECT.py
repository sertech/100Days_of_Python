#!python3
# Persona project the bus stop
"""
so we have a bus stop, we are working with only one bus line we have 5 buses
we have a schedule for each bus, we need to record the time the bus 
passed through the bus stop and save a record saying if the was on time, ahead of time or late
1) A dictionary will have a bus and a spected time of arrival
2) we need to create a random time + or - minutes to the arrival time
3) for each bus that pass show its result
4) we assume that all the buses pass the bus stop

KNOWLEDGE SITES:
The strftime() 
The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
Method A reference of all the legal format codes: 
https://www.w3schools.com/python/python_datetime.asp

How to store time without date in Python so it's convenient to compare?
https://stackoverflow.com/questions/36414920/how-to-store-time-without-date-in-python-so-its-convenient-to-compare

http://www.pressthered.com/adding_dates_and_times_in_python/
A timedelta object represents a duration, the difference between two dates or times.
class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
All arguments are optional and default to 0. Arguments may be integers or floats, and may be positive or negative.

"""
from datetime import datetime
from datetime import timedelta
from datetime import date


def main():
    # BUSES
    bus1 = "AAA111"
    bus2 = "BBB222"
    bus3 = "CCC333"
    bus4 = "DDD444"
    bus5 = "EEE555"

    # BUSSTOP TIMES FOR EACH BUS
    # BUS 1
    # datetime +/- timedelta OK --- datetime.time() +/- timedelta ERROR
    b1_time = datetime(2019, 12, 31, hour=22, minute=30,
                       second=0, microsecond=0, tzinfo=None)
    print(type(b1_time))  # <class 'datetime.time'>
    print(b1_time)  # 2019-12-31 22:30:00
    print(b1_time.time())  # 22:30:00
    add_minutes = timedelta(minutes=10)  # timedelta will be 10 minutes
    print((b1_time+add_minutes).time())  # 22:40:00

    # get today's date YYYY-MM-DD
    actualDate = date.today()
    print(actualDate)  # datetime.date(2019, 11, 1)

    # get today's time HH:MM:SS:MS
    todayTime = datetime.now().time()
    print(todayTime)  # 22:17:03.876384
    # format the time
    print(todayTime.strftime('%X'))  # 22:17:03

    randomMinutes = ""



if __name__ == "__main__":
    main()

"""
time formating sample
>>> print(x.strftime("%B"))
June
>>> print(x.strftime("%B %H"))
June 00
>>> print(x.strftime("%B%H"))
June00
>>>  
"""
