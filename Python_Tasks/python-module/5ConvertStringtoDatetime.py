from datetime import datetime

date_time_string = "2023-08-27 14:30:00"

date_time_format = "%Y-%m-%d %H:%M:%S"

datetime_object = datetime.strptime(date_time_string, date_time_format)


print("Datetime:", datetime_object)
