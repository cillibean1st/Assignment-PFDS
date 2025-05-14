# env/bin/python 3.12
import numpy as np
import pandas as pd


# read data
taxi_pool_df = pd.read_csv('TaxiRideShare .csv')
taxi_pool_df.head()
taxi_pool_df.info()
taxi_pool_df.describe()



# cleaning
taxi_pool_df = taxi_pool_df.drop(columns="timestamp")
taxi_pool_df = taxi_pool_df.drop(columns="datetime")

taxi_pool_df = taxi_pool_df["source"].dropna()
