# env/bin/python 3.12
import numpy as np
import pandas as pd


# read data
df = pd.read_csv('TaxiRideShare .csv')
df.head()
df.info()
df.describe()



# cleaning
#Remove columns with Large missing values
df = df.drop(columns="timestamp")
df = df.drop(columns="datetime")
df = df.drop(columns="price")
# fill missing values
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

# Drop remaining empties
df = df.dropna()
print(df.head())
print(df.info())

# Measure Of central tendency


