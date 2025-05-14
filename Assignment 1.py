# env/bin/python 3.12
import numpy as np
import pandas as pd


# read data
df = pd.read_csv('TaxiRideShare .csv')
df.head()
df.info()
df.describe()



# cleaning
df = df.drop(columns="timestamp")
df = df.drop(columns="datetime")


x = df["temperature"].mean()
df["temperature"] = df["temperature"].fillna(x)

x = df["windSpeed"].mean()
df["windSpeed"] = df["windSpeed"].fillna(x)

x = df["temperatureHigh"].mean()
df["temperatureHigh"] = df["temperatureHigh"].fillna(x)

x = df["pressure"].mean()
df["pressure"] = df["pressure"].fillna(x)

x = df["temperatureMin"].mean()
df["temperatureMin"] = df["temperatureMin"].fillna(x)

x = df["temperatureMax"].mean()
df["temperatureMax"] = df["temperatureMax"].fillna(x)
df = df.dropna()
print(df.head())
print(df.info())


