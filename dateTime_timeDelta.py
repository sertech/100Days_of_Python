#!python3
# time delta is pretty much a gap in time measure out
# to calculate things we use time delta 

from datetime import date
from datetime import datetime
from datetime import timedelta

t = timedelta(days=4, hours=10)

type(t)
#<class 'datetime.timedelta'>

t.days
#4

t.seconds # this so in timedelta the seconds is only able to go up a maximum of 1 day
#36000 this is just the 10 hours

t.hours
#Traceback (most recent call last):
    #File "<pyshell#119>", line 1, in <module> t.hours
#AttributeError: 'datetime.timedelta' object has no attribute 'hours'

t.seconds / 60 / 60  # to get t.hours  t.seconds*(1minute/60seconds)*(1hour/60minutes)
#10.0

t.seconds / 3600
#10.0


#########

eta = timedelta(hours=6)
#eta
#datetime.timedelta(seconds=21600)

today = datetime.today()

today
#datetime.datetime(2018, 2, 19, 14, 55, 19, 197404

today + eta
#datetime.datetime(2018, 2, 19, 20, 55, 19, 197404)

str(today + eta)
#'2018-02-19 20:55:19.197404'