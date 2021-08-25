import pandas
from sklearn import linear_model

df = pandas.read_csv("Filtered.csv")

X = df[['temp', 'humidity', 'fan_speed', 'elapsed_time']]
y = df['is_dry']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[68, 0, 1, 649.9999998]])

print(predictedCO2)