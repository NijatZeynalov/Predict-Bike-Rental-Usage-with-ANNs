#import libraries

import tensorflow as tf
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder

#import dataset
bike_df = pd.read_csv('daily_bike_sharing.csv')

#drop unimportant columns
bike_df = bike_df.drop(labels=['instant'], axis=1)
bike_df = bike_df.drop(labels=['casual', 'registered'], axis=1)

# convert day column datatype to datetime
bike_df.dteday = pd.to_datetime(bike_df.dteday, format='%m/%d/%Y')

#set index
bike_df.index = pd.DatetimeIndex(bike_df.dteday)
bike_df = bike_df.drop(labels= ['dteday'], axis=1)

#Normalizing data
X_num = bike_df[['temp','hum', 'windspeed','cnt']]
X_cat = bike_df[['season', 'yr','mnth', 'holiday','weekday','workingday','weathersit']]

#One-hot encoder
onehotencoder = OneHotEncoder()
X_cat = onehotencoder.fit_transform(X_cat).toarray()

X_num = X_num.reset_index()
X_cat = pd.DataFrame(X_cat)

#Concat numerical and characterical columns
X_all = pd.concat([X_cat, X_num], axis=1)
X_all = X_all.drop('dteday', axis = 1)

#Divide into X and y datasets
X = X_all.iloc[:,:-1].values
y = X_all.iloc[:,-1:].values

#Min max Scaler
scaler = MinMaxScaler()
y = scaler.fit_transform(y)
