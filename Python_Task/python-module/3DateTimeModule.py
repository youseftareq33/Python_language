import datetime,pytz

####################### Date #######################
print("####################### Date #######################"+"\n")
# current date:
print("current date: ",datetime.date.now().strftime("%Y,%M,%d")) # print in specific format
print("current date: ",datetime.date.today(),"\n"+"or u can print the (year or month or day) alone")
print("year: ",datetime.date.today().year)
print("month: ",datetime.date.today().month)
print("day: ",datetime.date.today().day)
print("--------------------------------------"+"\n")
# print specific date from object date
specific_date=datetime.date(2019,10,24)
print("specific date: ",specific_date,"\n"+"or u can print the (year or month or day) alone")
print("year: ",specific_date.year)
print("month: ",specific_date.month)
print("day: ",specific_date.day)
print("--------------------------------------"+"\n")
# Unix timestamp: number of seconds between a particular date and 1970-01-01 at UTC.
print("Unix timestamp: ",datetime.date.fromtimestamp(86400)) #the 86400 is the second per day, so after 86400 the date will be 1970-01-02

print("\n\n==================================")
####################### Time #######################
print("####################### Time #######################"+"\n")
# current time:
print("current time: ",datetime.datetime.now().strftime("%H:%M:%S"),"\n"+"or u can print the (hours or minutes or seconds) alone")
print("hour: ",datetime.datetime.now().strftime("%H"))
print("minute: ",datetime.datetime.now().strftime("%M"))
print("second: ",datetime.datetime.now().strftime("%S"))
print("--------------------------------------"+"\n")
# print specific time from object time
init_time=datetime.time() # time(hour = 0, minute = 0, second = 0)
specific_time=datetime.time(10,30,55,12000) # time(hour, minute, second, microsecond) or we can write it like this .time(hour=10,minute=30,second=55,microsecond=12000)
print("initial time: ",init_time)
print("specific time: ",specific_time,"\n"+"or u can print the (hours or minutes or seconds) alone")
print("hour: ",specific_time.hour)
print("minute: ",specific_time.min)
print("second: ",specific_time.second)
print("microsecond: ",specific_time.microsecond)

print("\n\n==================================")
####################### Date and Time #######################
print("####################### Date and Time #######################"+"\n")
# current date and time:
print("current date and time: ",datetime.datetime.now(),"\n"+"or u can print the (date or time) alone like the code above")
print("--------------------------------------"+"\n")
# specific date and time:
specific_date_and_time=datetime.datetime(2021,7,22,5,40,55)
print(specific_date_and_time,"\n"+"or u can print the (date or time) alone like the code above")
print("--------------------------------------"+"\n")
# timestamp is the date and time of occurrence of an event:
print("Timestamp =", datetime.datetime.timestamp(datetime.datetime(2022, 12, 28, 23, 55, 59, 342380)))
print("--------------------------------------"+"\n")
# differance between dates or times
# differance date:
date1 = datetime.date(year = 2018, month = 7, day = 12)
date2 = datetime.date(year = 2017, month = 12, day = 23)
date_res=date1-date2
print(date1,"-",date2,"=",date_res)
# differance time:
# we cannot do this, so we can use timedelta (date and time differance)
t_delta1 = datetime.timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t_delta2 = datetime.timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t_delta_res = t_delta1 - t_delta2
print(t_delta1,"-",t_delta2,"=",t_delta_res)
print("--------------------------------------"+"\n")
# Time duration in seconds
print(datetime.timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423).total_seconds)
print("--------------------------------------"+"\n")
# timezone in Python
print("NY:", datetime.now(pytz.timezone('America/New_York')).strftime("%m/%d/%Y, %H:%M:%S"))
print("\n\n==================================")



