from Motor import *
import time
from DHT11 import *
from Relay import *
from Helper import *
from ReedSwitch import *

# # Testing on servomotor
turn_motor(True)
time.sleep(8)
turn_motor(False)

# Testing on DHT11
# temp_humidity = get_readings()
# temp = get_median_from_mean_iqr(temp_humidity.temp)
# humidity =get_median_from_mean_iqr(temp_humidity.humidity)
# print(temp)
# print(humidity)

# Testing on Relay - Water Pump
turn_on_water_pump()
time.sleep(8)
turn_off_water_pump()

# # Testing on Relay - Heated Fan
# turn_on_heated_fan()
# time.sleep(8)
# turn_off_heated_fan()


# # Testing on magnetic reed switch
# print(magnetic_status())
