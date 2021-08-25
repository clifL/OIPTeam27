data = {'temp': [30], 'humidity': [70], 'fan_speed':[0], 'elapsed_time':1500}
data_two = {'temp': [64], 'humidity': [3], 'fan_speed':[1], 'elapsed_time':200}
print((prediction(data))[0])
print((prediction(data_two))[0])
