from numpy import true_divide
from DHT11 import *
from Helper import *
from SMS import *
from Telegram import *

send_message_flag = False
learning_flag = True

def logging():
    from datetime import datetime
    import csv
    while True:
        temp_humidity = get_readings()
        temp = get_median_from_mean_iqr(temp_humidity.temp)
        humidity =get_median_from_mean_iqr(temp_humidity.humidity)
        # datetime object containing current date and time
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        # open the file in the write mode
        with open('log.csv', 'a+', encoding='UTF8', newline='') as f:
            # create the csv writer
            writer = csv.writer(f)
            # write a row to the csv file
            data = [str(temp), str(humidity), dt_string]
            writer.writerow(data)
        print("Logged: " + str(temp) + "," + str(humidity) + "," + dt_string)
    

def is_dry():
    from Motor import turn_motor
    print("Turning Servomotor (Outwards)")
    turn_motor(True)
    print("Sampling humidity and temperature")
    temp_humidity = get_readings()
    temp = get_median_from_mean_iqr(temp_humidity.temp)
    humidity =get_median_from_mean_iqr(temp_humidity.humidity)
    print("Checking if syringes are dry")
    # Placeholder - Call ML Function
    dryness = True
    print("Turning Servomotor (Inwards)")
    turn_motor(False)
    return dryness
    
try:
    if learning_flag:
        logging()
    else:
        if is_dry():
            print("Syringes are dry!")
            if (send_message_flag):
                send_sms("Drying process done. Syringes are ready to collect.", [94884381])
                send_telegram_message("Drying process done. Syringes are ready to collect.")
            print("Telegram Notification Sent!")
            print("SMS Notification Sent!")
except KeyboardInterrupt:
    print("Terminated Program")