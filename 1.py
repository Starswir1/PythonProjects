from datetime import datetime, timedelta

start_time = "2024-07-07 00:00:00"
end_time = "2024-07-08 00:00:00"


def date_format_transform(start_time: str, end_time: str):
    start_time = start_time.replace("-", "").replace(":", "").replace(" ", "")
    end_time = end_time.replace("-", "").replace(":", "").replace(" ", "")
    return start_time, end_time


start_time, end_time = date_format_transform(start_time, end_time)

print(start_time)
print(end_time)
