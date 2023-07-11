from bson import Timestamp
from datetime import datetime

def create_timestamp_from_date_and_time(line, col_date, col_time):
    datetime_str = f"{line[col_date]} {line[col_time]}"
    try:
        datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        datetime_obj = datetime.strptime(datetime_str, "%m/%d/%Y %H:%M:%S")

    return Timestamp(int(datetime_obj.timestamp()), 1).as_datetime()

def create_timestamp_from_YMD(row):
    try:
        return datetime.strptime(row, "%Y-%m-%d")
    except ValueError:
        return datetime.strptime(row, "%m/%d/%Y")

def create_is_late_flag(hhmmss):
    hhmmss = {"date":"2000-01-01", "hour":hhmmss}
    hhmmss_base = {"date":"2000-01-01", "hour":"08:10:00"}
    hhmmss_arr = create_timestamp_from_date_and_time(hhmmss,"date","hour")
    hhmmss_base = create_timestamp_from_date_and_time(hhmmss_base,"date","hour")
    return hhmmss_arr > hhmmss_base
