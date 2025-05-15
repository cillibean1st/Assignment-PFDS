# env/bin/python 3.12
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read data
df = pd.read_csv('TaxiRideShare .csv')
df.head()
df.info()
df.describe()

# cleaning
# Remove columns with Large missing values
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
# hour
print("Hour mean", df["hour"].mean())
print("Hour median", df["hour"].median())
print("Hour min", df["hour"].min())
print("Hour max", df["hour"].max(), "\n \n")

# day
print("Day mean", df["day"].mean())
print("Day median", df["day"].median())
print("Day min", df["day"].min())
print("Day max", df["day"].max(), "\n \n")

# month
print("Month mean", df["month"].mean())
print("Month median", df["month"].median(), "\n \n")

# distance
print("Distance mean", df["distance"].mean())
print("Distance median", df["distance"].median())
print("Distance min", df["distance"].min())
print("Distance max", df["distance"].max(), "\n \n")

# temperature
print("Temperature mean", df["temperature"].mean())
print("Temperature median", df["temperature"].median())
print("Temperature min", df["temperature"].min())
print("Temperature max", df["temperature"].max(), "\n \n")

# Wind speed
print("Wind speed mean", df["windSpeed"].mean())
print("Wind Speed median", df["windSpeed"].median())
print("Wind Speed min", df["windSpeed"].min())
print("Wind Speed max", df["windSpeed"].max(), "\n \n")
