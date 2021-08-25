def get_readings():
    import sys
    import Adafruit_DHT
    temp_humidity = TempHumidity()
    temp_humidity.humidity = []
    temp_humidity.temp = []
    count = 0
    while count <= 15:
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        if humidity is not None and temperature is not None:
            temperature = '%.2f'%(temperature)
            temperature = float(temperature)
            humidity = '%.2f'%(humidity)
            humidity = float(humidity)
            temp_humidity.humidity.append(humidity)
            temp_humidity.temp.append(temperature)
            count = count + 1
    return temp_humidity

class TempHumidity():
    temp = []
    humidity = []

    
 