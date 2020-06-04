# Predict Bike Rental Usage with ANNs

A bicycle-sharing system is a platform where users can rent / use electric bikes that are available for shared use for a short-term price or free. Our data-set is a csv file  with information from 17,379 hours over 731 days with 16 features (information categories) for each hour. The features are:

__instant:__ record index

__dteday :__ date

__season :__ season (1:springer, 2:summer, 3:fall, 4:winter)

__yr :__ year (0: 2011, 1:2012)

__mnth : month ( 1 to 12)

__hr :__ hour (0 to 23)

__holiday :__ wether day is holiday or not (extracted from http://dchr.dc.gov/page/holiday-schedule)

__weekday :__ day of the week

__workingday :__ if day is neither weekend nor holiday is 1, otherwise is 0.
__weathersit :__

__1:__ Clear, Few clouds, Partly cloudy

__2:__ Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist

__3:__ Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds

__4:__ Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog

__temp :__ Normalized temperature in Celsius. The values are divided to 41 (max)

__hum:__ Normalized humidity. The values are divided to 100 (max)

__windspeed:__ Normalized wind speed. The values are divided to 67 (max)

__casual:__ count of casual users

__registered:__ count of registered users

__cnt:__ count of total rental bikes including both casual and registered

In this project, I have used Artificial Neural Networks, not classic Machine Learning algorithms.
