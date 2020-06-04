# Predict Bike Rental Usage with ANNs

A bicycle-sharing system is a platform where users can rent / use electric bikes that are available for shared use for a short-term price or free. Our data-set is a csv file  with information from 17,379 hours over 731 days with 16 features (information categories) for each hour. The features are:

__instant: record index__

__dteday : date__

__season : season (1:springer, 2:summer, 3:fall, 4:winter)__

__yr : year (0: 2011, 1:2012)__

__mnth : month ( 1 to 12)__

__hr : hour (0 to 23)__

__holiday : wether day is holiday or not (extracted from http://dchr.dc.gov/page/holiday-schedule)__

__weekday : day of the week__

__workingday : if day is neither weekend nor holiday is 1, otherwise is 0.__
weathersit :__

__1: Clear, Few clouds, Partly cloudy__

__2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist__

__3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds__

__4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog__

__temp : Normalized temperature in Celsius. The values are divided to 41 (max)__

__hum: Normalized humidity. The values are divided to 100 (max)__

__windspeed: Normalized wind speed. The values are divided to 67 (max)__

__casual: count of casual users__

__registered: count of registered users__

__cnt: count of total rental bikes including both casual and registered__
