import datetime

wash_end_time = datetime.datetime.now()
wash_end_time = wash_end_time +  datetime.timedelta(seconds=120)
while True:
    print(wash_end_time)