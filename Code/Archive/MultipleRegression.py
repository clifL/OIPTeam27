import pandas
from sklearn import linear_model

def get_drying_time():
    df = pandas.read_csv("Filtered.csv")

    X = df[['is_dry']]
    y = df['elapsed_time']

    regr = linear_model.LinearRegression()
    regr.fit(X, y)

    elapsed_time = regr.predict([[1]])

    return elapsed_time